from numpy import *

from molearn.classifiers.PS import PS

from sklearn.tree import DecisionTreeClassifier

from infogainsplitmetric import InfoGainSplitMetric

from node import Node



class HoeffdingTreeClassifier:

	def __init__(self):
		self.root = Node()
		j_max = 0


		
	def fit(self, X, Y):
		N,self.L = X.shape
		for i in range(N-1):
			self.partial_fit([X[i]],[Y[i]])
		return self
				
	
	def partial_fit(self, x, y=None):
		if self.root is None:  
			self.root = Node()
		self.root.update_statistics(x,y)	
		return self

	def predict(self, X):
		c= self.root.predict(X)
		return c




