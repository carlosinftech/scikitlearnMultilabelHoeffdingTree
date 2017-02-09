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
		self.root = None
		j_max = 0
		L = -1
		self._min_frac_weight_for_two_branches_gain = 0.01
		self.INFO_GAIN_SPLIT = 1
		self._selected_split_metric = self.INFO_GAIN_SPLIT
		self._split_confidence = 0.0000001
		self._split_metric = InfoGainSplitMetric(self._min_frac_weight_for_two_branches_gain)
		self.current  = None
	
	def fit(self, X, Y):
		""" Just starting an empty tree and adding the x to it. """
		N,self.L = Y.shape
		Y_sum = sum(Y,axis=0)
		self.j_max = argmax(Y_sum)
		return self
	def split_verification(self):
	
		return None			
	
	def partial_fit(self, x, y=None):
		""" constructs the root node if has not been created, fills the statistics of the root node
		    in the case there is already a root node, then it is been called the update statistic 
		    for the node.
		"""
		if self.root is None:  
			self.root = Node()
			self.current = self.root
			self.root.update_statistics(x,y)
		self.root.update_statistics(x,y)	
		return self

	def predict(self, X):
		""" for calling the prediction of the node """
		N,D = X.shape
		Y = zeros((N,self.L))
		Y[:,self.j_max] = 1
		#Y = self.node.predict(X)
		return Y

class MajorityLabel:

	def __init__(self):
		j_max = 0
		L = -1

	def fit(self, X, Y):
		N,self.L = Y.shape
		Y_sum = sum(Y,axis=0)
		self.j_max = argmax(Y_sum)
		return self

	def partial_fit(self, X, Y=None):
		return self

	def predict(self, X):
		N,D = X.shape
		Y = zeros((N,self.L))
		Y[:,self.j_max] = 1
		return Y


