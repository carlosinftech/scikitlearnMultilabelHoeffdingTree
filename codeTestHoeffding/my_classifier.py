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
		self.current  = None



	

	##Just starting an empty tree and adding the x to it. 	
	def fit(self, X, Y):
		N,self.L = Y.shape
		Y_sum = sum(Y,axis=0)
		self.j_max = argmax(Y_sum)
		return self
	def split_verification(self):
	
		return None
	##

				
	
	def partial_fit(self, x, y=None):
		if self.root is None:  
			self.root = Node()
			self.current = self.root
			self.root.update_statistics(x,y)
		self.root.update_statistics(x,y)	
		##g_Xa = self.first
		##g_Xb = self.second
		##ns = self.current.get_node_statistics()
		
		##print(g_Xa)
		##print(g_Xb)
		##compute_ ## Compute Hf bound
	
			##boolean split = split_verification(ns)
			##if split:
			## 
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


