##standard library imports
from numpy import *
##Application specific imports
from molearn.classifiers.PS import PS
from sklearn.tree import DecisionTreeClassifier
from infogainsplitmetric import InfoGainSplitMetric
##local imports
from node import Node

class HoeffdingTreeClassifier:
	""" This class classifies a Hoeffding Tree and initializate its structure. """
	def __init__(self):
		""" Constructor of the class, contains essential parameters for the 
		    hoeffding tree creation.
		"""
		self.root = Node()
		j_max = 0
	
	def fit(self, X, Y):
		""" Just starting an empty tree and adding the x to it. """
		N,self.L = X.shape
		for i in range(N-1):
			self.partial_fit([X[i]],[Y[i]])
		return self
			
	
	def partial_fit(self, x, y=None):
		""" constructs the root node if has not been created, fills the statistics of the root node
		    in the case there is already a root node, then it is been called the update statistic 
		    for the node.
		"""
		if self.root is None:  
			self.root = Node()
		self.root.update_statistics(x,y)	
		return self

	def predict(self, X):
		""" for calling the prediction of the node """
		c= self.root.predict(X)
		return c

