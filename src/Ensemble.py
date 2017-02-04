from sklearn.ensemble import BaseEnsemble
from sklearn import tree
import numpy as np

class EnsembleClassifier(BaseEnsemble):
    def __init__(self, n_classifier=10, base_estimator="HeoffdingTree", buffer_size=1000):
        self.current_instance_number = 0
        self.n_classifier = n_classifier
        self.buffer_size = buffer_size
        self.instances_bag = []
        for i in range(0, self.n_classifier):
            self.instances_bag.append([])
        BaseEnsemble.__init__(self, base_estimator=base_estimator)

    def apply(self, X):
        if self.current_instance_number < self.buffer_size:
            # filing the batch
            for i in range(0, self.n_classifier):
                x = np.random.poisson(1)
                for j in range(0, x):
                    self.instances_bag[i].append(X)
            self.current_instance_number += 1
        else:
            # training models
            models = []
            for i in range(0, self.n_classifier):
                models.append(tree.DecisionTreeClassifier.fit(X))
            # for each instances in model bag train un model
            # return le bon
            # vider le model bag
            print(self.instances_bag)

    def fit(self, x, Y, sample_weight=None):
        pass

x = EnsembleClassifier(n_classifier=5, buffer_size=6)
x.apply(0)
x.apply(1)
x.apply(2)
x.apply(3)
x.apply(4)
x.apply(5)
x.apply(6)
