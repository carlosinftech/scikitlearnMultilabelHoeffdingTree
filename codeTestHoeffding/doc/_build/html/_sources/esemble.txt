
ENSEMBLE METHOD
==================

**class Bagging()**
This class is to create a an ensemble method based on bagging for streaming data
This implementation is based on Oza and Russell's Online Bagging Models.

**Parameters:**
n_classifier: Number of different classifiers used for bagging
base_estimator: Base Estimator of the Ensemble Method, such as HoeffdingTree, DecisionTreeClassifier,
buffer_size: Number of streaming instances kept by the buffer as a mini-batch.

**fit(self, x, Y, sample_weight = None):** 
This method is to train the streaming data.

**predict (self, X):**
predict label of X. This predict function uses Majority Vote to emit the result.
