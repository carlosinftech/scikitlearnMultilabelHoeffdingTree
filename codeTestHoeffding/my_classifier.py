from numpy import *

from molearn.classifiers.PS import PS

from sklearn.tree import DecisionTreeClassifier

class HoeffdingTreeClassifier:

	def __init__(self):
		self.j_max = 0
		self.L = -1
		self.parent = None
		self.children = None
		self.xdata = None
		self.ydata = None

	def setParent(self,node):
		self.parent = node
	
	def compute_hoeffding_bound(self, max_value, confidence, weight):
		return math.sqrt(((max_value * max_value) * math.log(1.0 / confidence)) / (2.0 * weight))
	##Just starting an empty tree and adding the x to it. 	
	def fit(self, X, Y):
	    if !self.data:
			self.data = X
		
		self.ws,self.L = Y.shape
		h = PS(p=7,h=DecisionTreeClassifier())
		h.fit(X,Y)
		self.xpos=0
		self.H.append(h)
		self.s1=(self.ws,len(X[0]))
		self.s2=(self.ws,len(Y[0]))
		self.X_batch = zeros(self.s1)
		self.Y_batch = zeros(self.s2)
		return self

	def partial_fit(self, x, y=None):
		xb = False
		xpos = self.xpos
		self.X_batch[xpos]=x
		self.Y_batch[xpos]=y
		self.xpos = xpos + 1
		
		if xpos == self.ws-1:
			self.xpos = 0
			self.h = PS(p=7,h=DecisionTreeClassifier())
			self.h.fit(self.X_batch,self.Y_batch)
			self.H.append(self.h)
			if len(self.H)>5:
				self.H = self.H[-5:]
		return self

	def predict(self, x):
		N,D = x.shape
		H2 = zeros((len(self.H),self.L))
		for k in range(len(self.H)):
			H2[k]=self.H[k].predict(x)
		R = H2.sum(axis=0)
		R = R * float(1/float(len(self.H)))
		for k in range(len(R)):
			R[k]= 1 if R[k] >= float(0.5) else 0
		return R

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


