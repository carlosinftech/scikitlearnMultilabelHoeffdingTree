from numpy import *

from molearn.classifiers.PS import PS

from sklearn.tree import DecisionTreeClassifier

from infogainsplitmetric import InfoGainSplitMetric

from node import Node



class HoeffdingTreeClassifier:

	def __init__(self):
		self.root = None
		j_max = 0
		L = -1
		##Infogain stuff
		self._min_frac_weight_for_two_branches_gain = 0.01
		self.INFO_GAIN_SPLIT = 1
		self._selected_split_metric = self.INFO_GAIN_SPLIT
		self._split_confidence = 0.0000001
		self._split_metric = InfoGainSplitMetric(self._min_frac_weight_for_two_branches_gain)
		


	
	def compute_hoeffding_bound(self, max_value, confidence, weight):
		return math.sqrt(((max_value * max_value) * math.log(1.0 / confidence)) / (2.0 * weight))
	
	##Just starting an empty tree and adding the x to it. 	
	def fit(self, X, Y):
		N,self.L = Y.shape
		Y_sum = sum(Y,axis=0)
		self.j_max = argmax(Y_sum)
		return self

	def partial_fit(self, x, y=None):
		if self.root is None:
			self.root = Node()
		metric_max = self._split_metric.get_metric_range(x)
		self.root.update_statistics(x,y)
		return self

	def predict(self, X):
		N,D = X.shape
		Y = zeros((N,self.L))
		Y[:,self.j_max] = 1
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


