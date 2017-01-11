from sklearn.model_selection import StratifiedKFold
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn import datasets
import numpy as np
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import itertools


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

def train_model(data, folds):

	skf = StratifiedKFold(n_splits=folds)

	Yb = data['classification']
	y = []
		
	for i in Yb:
		if i:
			y.append(1)
		else:
			y.append(0)

	y = np.array(y)
	X = data.ix[:,3:].as_matrix()
	round = 1
	accuracies = []
	sensitivities = []
	precisions = []
	fmeasures = []
	for train_index, test_index in skf.split(X, y):
		X_train, X_test = X[train_index], X[test_index]
		y_train, y_test = y[train_index], y[test_index]

		model = GaussianNB()

		y_pred = model.fit(X_train, y_train).predict(X_test)
		score = model.score(X_test, y_test)
		accuracies.append(score)


		cm = confusion_matrix(y_test, y_pred)

		#Metrics calculation
		sensitivity = cm[1][1]/(cm[1][1] + cm[1][0])
		sensitivities.append(sensitivity)
		precision = cm[1][1]/(cm[1][1] + cm[0][1])
		precisions.append(precision)
		fmeasures.append(2*(sensitivity*precision)/(precision + sensitivity))

		cm_norm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
		np.set_printoptions(precision=2)
		#plt.figure()
		#plot_confusion_matrix(cm, classes=["Não Narcisista", "Narcisista"], title='Matriz de confusão')
		#plt.show()
		
		#print("Score : ", score)
		# print(u"Rodada #{0} (score: {1:.2f})".format(round, score))
		# round = round + 1

		# print(u"Partição de treinamento: do índice #{} ao índice #{}".format(train_index[0], train_index[-1]))
		# print(u"Partição de teste: do índice #{} ao índice #{}".format(test_index[0], test_index[-1]))
		# print(u"----------------------------")

		# print(u'Matriz de Confusão Regular')
		#print(cm)
		# print(u'Matriz de Confusão Normalizada')
		# print(cm_norm)

	accuracies = np.array(accuracies)
	sensitivities = np.array(sensitivities)
	precisions = np.array(precisions)
	fmeasures = np.array(fmeasures)

	print("------------------------------------------------------------------------------------------")
	print(u"Acurácia mínimo: {0:.2f} Acurácia máximo: {1:.2f} Acurácia médio: {2:.2f} Desvio Padrão: {3:.2f}".format(accuracies.min(), accuracies.max(), accuracies.mean(), np.std(accuracies)))
	print(u"Sensibilidade mínima: {0:.2f} Sensibilidade máxima: {1:.2f} Sensibilidade média: {2:.2f} Desvio Padrão: {3:.2f}".format(sensitivities.min(), sensitivities.max(), sensitivities.mean(), np.std(sensitivities)))
	print(u"Precisão mínima: {0:.2f} Precisão máxima: {1:.2f} Precisão média: {2:.2f} Desvio Padrão: {3:.2f}".format(precisions.min(), precisions.max(), precisions.mean(), np.std(precisions)))
	print(u"F mínima: {0:.2f} F máxima: {1:.2f} F média: {2:.2f} Desvio Padrão: {3:.2f}".format(fmeasures.min(), fmeasures.max(), fmeasures.mean(), np.std(fmeasures)))
	print("------------------------------------------------------------------------------------------")

users = pd.read_csv("data/users.csv")
tweets = pd.read_csv("data/tweets.csv")

print("TWEETS : ")
train_model(tweets, 10)
print("USERS : ")
train_model(users, 10)