from numpy import *
from infogainsplitmetric import InfoGainSplitMetric

class Node():
	def __init__(self):
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
	
	def setParent(self,node):
		self.parent = node
		
	def get_node_statistics(self):
		return self.statistics
	
	
	##def sort_examples(self,x,y):
		
	##def split_node(self, x, y):
		
	
	

	def compute_first_second_best(self):
		##self.compute_first_second_best(x)
		metric_temp = 0
		metric_max = 0
		self.first = 0
		for key_attribute in self.map: ## y
			##print("y",key_attribute)
			m2 = self.map[key_attribute]
			for key_class in m2:   ##x
				##print("x",key_class)
				column = [] 
				for key_instance in m2[key_class]:
					m3=m2[key_class]
					##print("instance",key_instance)
					##print("value",m3[key_instance])
					for count in range (0,m3[key_instance]):
						##print(key_instance)
						column.append(key_instance)
				metric_temp = self._split_metric.get_metric_range(column)
				if metric_max <= metric_temp:
					##print("metric_temp",metric_temp)
					metric_max= metric_temp
					self.second=self.first
					self.first = metric_max
					self.column_name_second = self.column_name_first
					self.column_name_first = key_class
					self.n = len(column)
			##print("y",key_attribute,"first",self.column_name_first)
			##print("y",key_attribute,"second",self.column_name_second)
	
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
		else:
			print('dont split')
		
		
	
		
		##print ginis 
	##it only receives one row
	##class is represented by i
	##attribute is represented by j
	##value of attribute is represented by the ones and increased every time
	def update_statistics(self,x,y):
		self.number_of_classes = len(x[0])-1
		if self.map is None:
			self.map = {}
		for i in range(len(y)):
			if str(i) not in self.map:
					self.map[str(i)] = {} 
			for j in range(len(x[0])-1):
				value = x[0][j]
				if str(j) not in self.map[str(i)]:
					self.map[str(i)][str(j)]={str(value):1}
				else:
					if str(value) not in self.map[str(i)][str(j)]:
						self.map[str(i)][str(j)]={str(value):1}
					else:
						self.map[str(i)][str(j)][str(value)]+=1
		self.compute_first_second_best()
		self.comparison_entropies_hf_bound()
		
