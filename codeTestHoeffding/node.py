class Node():
	def __init__(self):
		self.parent = None
		self.children = None
		self.map = None
		self.statistics = None
	
	def setParent(self,node):
		self.parent = node
		
	def get_node_statistics(self):
		return self.statistics
	
	
	##it only receives one row
	def update_statistics(self,att,classes):
		if self.map is None:
			self.map = {}
		for i in range(len(classes)):
			if 'class'+str(i) not in self.map:
					self.map['class'+str(i)] = {} 
			for j in range(len(att)):
				value = att[j]
				if 'attribute'+str(j) not in self.map['class'+str(i)]:
					self.map['class'+str(i)]['attribute'+str(j)]={str(value):1}
				else:
					if str(value) not in self.map['class'+str(i)]['attribute'+str(j)]:
						self.map['class'+str(i)]['attribute'+str(j)]={str(value):1}
					else:
						self.map['class'+str(i)]['attribute'+str(j)][str(value)]+=1
		##print(self.map)

