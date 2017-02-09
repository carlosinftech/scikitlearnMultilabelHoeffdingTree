## Standard library imports
from numpy import *

##  Application specific imports
from infogainsplitmetric import InfoGainSplitMetric

"""This class creates the nodes that constucts a Hoeffding tree"""

class Node():
	def __init__(self):
		"""Default values of a Node, constructs a node"""		
		self.parent = None
		self.children = None
		self.map = None
		self.statistics = None
		self.first = 0
		self.second = 0
		self._min_frac_weight_for_two_branches_gain = 0.01
		self.INFO_GAIN_SPLIT = 1
		self._selected_split_metric = self.INFO_GAIN_SPLIT
		self._split_confidence = 0.0000001
		self._split_metric = InfoGainSplitMetric(self._min_frac_weight_for_two_branches_gain)
		self.column_name_second  = None
		self.column_name_first = None 
		self.tie_breaking = 0.05
		self.confidence = 0.95
		self.delta = 1-self.confidence
		self.n = 0
		self.number_of_classes = 0
		self.splitCondition = None
		self.activeNode = True
		self.per_column = None
	
	def setParent(self,node):
		"""Sets a node as parent"""
		self.parent = node
		
	def get_node_statistics(self):
		"""Returns the node's statistics"""
		return self.statistics

	def compute_first_second_best(self):
		"""Look in the map for get the instance per each class and per each attribute, the instances are 
		   saved in an array. Then is computed the method entropy (information gain in this case) om order 
		   to obtain the attribute with highest entropy and the second highest.
		   self.first is the attribute with highest entropy.
		   self.second is the attribute with the second highest entropy.
		"""
		metric_temp = 0
		metric_max = 0
		self.first = 0
		for key_attribute in self.map: 
			m2 = self.map[key_attribute]
			for key_class in m2:  
				column = [] 
				for key_instance in m2[key_class]:
					m3=m2[key_class]
					for count in range (0,m3[key_instance]):
						column.append(key_instance)
				metric_temp = self._split_metric.get_metric_range(column)
				if metric_max <= metric_temp:
					metric_max= metric_temp
					self.second=self.first
					self.first = metric_max
					self.column_name_second = self.column_name_first
					self.column_name_first = key_class
					self.n = len(column)

	def compute_hoeffding_bound(self, range, delta, n):
		"""Computes the hoeffding bound and returns its value"""
		return math.sqrt(((range * range) * math.log(1.0 / delta)) / (2.0 * n))
		
	def comparison_entropies_hf_bound(self):
		"""First computes the hoeffding bound with the numbers of clasess at the moment.
		   then it does the substaction of the values of self.first and self.second
		   and lastly it compares if the substraction of the entopies is greater than the hoeffding
		   bound. if so then the node must split.
		   Note: for the range of the variable, for information gain the range is log c, where c is the number of classes
		"""
		c = math.log(self.number_of_classes)
		hoeffding_bound = self.compute_hoeffding_bound(c,self.delta, self.n)
		entropy_Xa_Xb = self.first - self.second
		if (entropy_Xa_Xb > hoeffding_bound): ##tie_breaking recommended in MO
			print('split')
			self.split(self.column_name_first)
		##else:
			##print('dont split')
		
	def split(self,column_name):
		"""Process of spliting a node, for each y in the map it is created a node classified as child.
		   each child  is loaded with its belonging statistics.
		"""
		self.splitCondition = column_name
		self.children = {}
		self.activeNode = False
		previous = 0	
		for y_val in self.map:
				for j_val in self.map[y_val][column_name]:
					child = Node()
					self.children[j_val]=child
					child_map = {}
					child_statistics = {y_val:{}}
					for element in self.statistics[y_val][column_name][j_val]:			
						for k in self.map[y_val]:
							if k != self.column_name_first:
								for k_val  in  self.statistics[y_val][k]: ##add one
									if element in self.statistics[y_val][k][k_val]:
										if k not in child_statistics[y_val]:
											child_statistics[y_val] = {k:{}}
										if k_val not in child_statistics[y_val][k]:
											child_statistics[y_val][k]={k_val:1}
										else:
											child_statistics[y_val][k][k_val]+=1
					self.children[j_val].set_statistics(self.map.copy(),child_statistics.copy())
	
	##temporary Need to add the real map and statistics
	def set_statistics(self,map,statistics):
		"""For adding a map and statistics"""
		self.map = None
		self.statistics = None
	
	def update_statistics(self,x,y):
		"""This method fits the x and y, if the node is active then the statistics are updating according the values of x an y
		   It is also invoqued the methods for obtaing the first and second best 
		   if is not an active node, it goes to the child leaves and recursively is called again the method.
		"""
		self.number_of_classes = len(x[0])-1
		if self.activeNode:
			if self.statistics is None:
				self.statistics = {}
			if self.map is None:
				self.map = {}
			for i in range(len(y)):
				if str(i) not in self.map:
						self.map[str(i)] = {}
				if str(i) not in self.statistics:
						self.statistics[str(i)] = {}
				for j in range(len(x[0])-1):
					value = x[0][j]
							
					if str(j) not in self.statistics[str(i)]:
						l = []
						l.append(self.n)
						self.statistics[str(i)][str(j)]={str(value):l}
					else:
						if str(value) not in self.statistics[str(i)][str(j)]:
							l = []
							l.append(self.n)
							self.statistics[str(i)][str(j)]={str(value):l}
						else:
							self.statistics[str(i)][str(j)][str(value)].append(self.n)
							
					if str(j) not in self.map[str(i)]:
						self.map[str(i)][str(j)]={str(value):1}
					else:
						if str(value) not in self.map[str(i)][str(j)]:
							self.map[str(i)][str(j)]={str(value):1}
						else:
							self.map[str(i)][str(j)][str(value)]+=1
					
			self.compute_first_second_best()
			self.comparison_entropies_hf_bound()
		else:
			to_transfer = x[0][int(self.splitCondition)]
			x[0][int(self.splitCondition)]
			try:
				self.children[str(to_transfer)].update_statistics(x,y)
			except KeyError:
				child = Node()
				self.children[str(to_transfer)]=child
				self.children[str(to_transfer)].update_statistics(x,y)
