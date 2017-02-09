HOEFFDING TREES's Node code
================================
.. automodule:: node
:members: 


**class Node():**
This class creates the nodes that constucts a Hoeffding tree.

**def __init__(self):**
Default values of a Node, constructs a node.

**def setParent(self,node):
Sets a node as parent

**def get_node_statistics(self):**
Returns the node's statistics
**def compute_first_second_best(self):**
Look in the map for get the instance per each class and per each attribute, the instances are saved in an array. Then is computed the method entropy (information gain in this case) in order  to obtain the attribute with highest entropy and the second highest self.first is the attribute with highest entropy.self.second is the attribute with the second highest entropy.

**def compute_hoeffding_bound(self, range, delta, n):**
Computes the hoeffding bound and returns its value"
def comparison_entropies_hf_bound(self):
First computes the hoeffding bound with the numbers of clasess at the moment.then it does the substaction of the values of self.first and self.second and lastly it compares if the substraction of the entopies is greater than the hoeffding bound. if so then the node must split. Note: for the range of the variable, for information gain the range is log c, where c is the number of classes.

**def split(self,column_name):**
Process of spliting a node, for each y in the map it is created a node classified as child. Each child  is loaded with its belonging statistics.

**def set_statistics(self,map,statistics):**
For adding a map and statistics
**def predict(self, x):**
For generate the prediction based on the previus updated statistics.

**def update_statistics(self,x,y):**
This method fits the x and y, if the node is active then the statistics are updating according the values of x an y. It is also invoqued the methods for obtaing the first and second best if is not an active node, it goes to the child leaves and recursively is called again the method.


