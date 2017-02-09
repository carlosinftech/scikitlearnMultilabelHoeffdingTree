from numpy import *
from infogainsplitmetric import InfoGainSplitMetric

class Node():
	def __init__(self):
		self.parent = None
		self.children = None
		self.map = None
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
		self.parent = node
		
	

	def compute_first_second_best(self):
		metric_temp = 0
		metric_max = 0
		self.first = 0
		for key_class in self.per_column:  
			column = [] 
			for instance in self.per_column[key_class]:
				for count in range (0,self.per_column[key_class][instance]):
					column.append(instance)
			metric_temp = self._split_metric.get_metric_range(column)
			if metric_max <= metric_temp:
				metric_max= metric_temp
				self.second=self.first
				self.first = metric_max
				self.column_name_second = self.column_name_first
				self.column_name_first = key_class
				self.n = len(column)
	
	##range of a variable 
	##(e.g., for a probability the range is one, and for an information gain the range is log c, where c is the number of classes
	def compute_hoeffding_bound(self, range, delta, n):
		return math.sqrt(((range * range) * math.log(1.0 / delta)) / (2.0 * n))
	

	
	def comparison_entropies_hf_bound(self):
	##number of rows of r
		##just for info gain
		c = math.log(self.number_of_classes)
		hoeffding_bound = self.compute_hoeffding_bound(c,self.delta, self.n)
		entropy_Xa_Xb = self.first - self.second
		if (entropy_Xa_Xb > hoeffding_bound): ##tie_breaking recommended in MO
			print('split')
			##self.split()
		else:
			print('dont split')
	

	def reset_statistics(self):
		self.active_node = False
		self.map = None
		self.per_column = Node
	
	def set_statistics(self,map):
		##TODO
		##Compute columns
		self.map = map
	
	
	def split(self):
		self.splitCondition = self.column_name_first
		self.children = {}
		previous = 0
		for y_val in self.map:
			for j in self.map[y_val]:
				for j_val in self.map[y_val][j]:
					
					if j_val not in self.children:
						child = Node()
						self.children[j_val]=child
					map2 = self.map[y_val][j][j_val].copy()
					self.children[j_val].set_statistics(map2)
		##for key_attribute in self.map: 
			##m = self.map[key_attribute][self.column_name_first]
			##for key_instance in m:
				##child = Node()
				##pass statistics to child
				##self.children[key_instance] = child
				
		
	
		
		##print ginis 
	##it only receives one row
	##class is represented by i
	##attribute is represented by j
	##value of attribute is represented by the ones and increased every time
	##structure of the map is attribute, class1 and class2 
	##fixme str y 0 0 
	def update_statistics(self,x,y):
		self.number_of_classes = len(x[0])-1
		y_val=y[0][0]
		
		if self.map is None:
			self.map = {}
		
		if self.per_column is None:
			self.per_column = {}
		
		if y_val not in self.map:
			self.map[y_val] = {}
		
		for j in range(len(x[0])-1):
			value1 = x[0][j]
			if j not in self.map[y_val]:
				self.map[y_val][j] = {}
			if value1 not in self.map[y_val][j]:
				self.map[y_val][j][value1]={}
			
			if j not in self.per_column:
				self.per_column[j] = {}
			if value1 not in self.per_column[j]:
				self.per_column[j][value1]=1
			else:
				self.per_column[j][value1]+=1
			
			for k in range(j+1,len(x[0])-1):
				value2 = x[0][k]
				if k not in self.map[y_val][j][value1]:
					self.map[y_val][j][value1][k]={}
				if value2 not in self.map[y_val][j][value1][k]:
					self.map[y_val][j][value1][k][value2]=1
				else:
					self.map[y_val][j][value1][k][value2]+=1					
		##print('update')
		self.compute_first_second_best()
		##print('first_second')
		self.comparison_entropies_hf_bound()
		##print('coparison')
		
