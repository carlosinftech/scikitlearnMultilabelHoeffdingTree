
Welcome to ENSEMBLES OF MULTI-LABEL HOEFFDING TREES's documentation!
====================================================================

A Hoeffding tree is an incremental, anytime decision tree induction algorithm that is capable of learning from massive data streams, assuming that the distribution generating examples does not change over time. Hoeffding trees exploit the fact that a small sample can often be enough to choose an optimal splitting attribute. This idea is supported mathematically
by the Hoeffding bound, which quantifies the number of observations (in our case, examples) needed to estimate some statistics within a prescribed precision (in our case, the goodness of an attribute).

Contents:
==================

.. toctree::
   :maxdepth: 2
   
   hoeffdingTreeNode
   hoeffdingTreeClass
   multilabel
   esemble



