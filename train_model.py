from sklearn.model_selection import StratifiedKFold
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn import datasets
import numpy as np
from sklearn.metrics import confusion_matrix


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
		# print(u"Rodada #{0} (score: {1:.2f})".format(round, score))
		# round = round + 1

		# print(u"Partição de treinamento: do índice #{} ao índice #{}".format(train_index[0], train_index[-1]))
		# print(u"Partição de teste: do índice #{} ao índice #{}".format(test_index[0], test_index[-1]))
		# print(u"----------------------------")

		# print(u'Matriz de Confusão Regular')
		# print(cm)
		# print(u'Matriz de Confusão Normalizada')
		# print(cm_norm)

	scores = np.array(scores)
	print(u"Score mínimo: {0:.2f} Score máximo: {1:.2f} Score médio: {2:.2f}".format(scores.min(), scores.max(), scores.mean()))


users = pd.read_csv("data/users.csv")
tweets = pd.read_csv("data/tweets.csv")

print("TWEETS : ")
train_model(tweets, 10)
print("USERS : ")
train_model(users, 10)