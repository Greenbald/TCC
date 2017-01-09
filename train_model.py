from sklearn.model_selection import StratifiedKFold
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

skf = StratifiedKFold(n_splits=10)
tweets = pd.read_csv("data/tweets.csv")

Yb = tweets['classification']
y = []
	
for i in Yb:
	if i:
		y.append(1)
	else:
		y.append(0)

y = np.array(y)
X = tweets.ix[:,3:].as_matrix()

# y = iris.target
# X = iris.data

#print(X[[0,1,2,3,4,5,6,7,8,9]])


# skf.get_n_splits(X, y)
round = 1
scores = []
for train_index, test_index in skf.split(X, y):
	X_train, X_test = X[train_index], X[test_index]
	y_train, y_test = y[train_index], y[test_index]

	model = GaussianNB()

	y_pred = model.fit(X_train, y_train).predict(X_test)
	score = model.score(X_test, y_test)
	scores.append(score)


	cm = confusion_matrix(y_test, y_pred)
	cm_norm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
	np.set_printoptions(precision=2)
	print(u"Rodada #{0} (score: {1:.2f})".format(round, score))
	round = round + 1

	print(u"Partição de treinamento: do índice #{} ao índice #{}".format(train_index[0], train_index[-1]))
	print(u"Partição de teste: do índice #{} ao índice #{}".format(test_index[0], test_index[-1]))
	print(u"----------------------------")

	print(u'Matriz de Confusão Regular')
	print(cm)
	print(u'Matriz de Confusão Normalizada')
	print(cm_norm)

scores = np.array(scores)
print(u"Score mínimo: {0:.2f} Score máximo: {1:.2f} Score médio: {2:.2f}".format(scores.min(), scores.max(), scores.mean()))

# Exibe todas as figuras
plt.show()