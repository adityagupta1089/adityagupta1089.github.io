---
layout: post
title: Decision Trees

categories: ["Notes", "Machine Learning"]
date: 2019-10-14 14:59 +0530
---
# Entropy 2-class

If $\cal I$ is the set of training examples, $p_+$ ratio of posititive examples in $\cal I$ and $p_-$ negative examples then entropy which measures impurity:

$$\text{Entropy}(I) = -p_+\log_2p_+ - p_-\log _2p_-$$

This represents expected number of bits to encode the class of a randomly drawn member of $\cal I$

# Information Gain

Expected reduction in entropy due to sorting on attribute $x_i$

$$\text{Gain}({\cal I}, x_i)=\text{Entropy}(I)-\sum_{v\in\text{values}(x
_i)}\frac{|\cal I_v|}{|\cal I|}\text{Entropy}(\cal I_v)$$

- $\text{values}(x_i)$: all possible values of $x_i$
- $\cal I_v\subset \cal I$ : points in $\cal I$ that take value $v$ for $x_i$

# Mutual Information Gain & Information Gain

Mutual information is the measure of mutual dependence of two random variables.

Mutual information gain for two random variables $X$ and $Y$ is:

$$I(X;Y)=\sum_{y\in Y}\sum_{x\in X}p(x, y)\log\left(\frac{p(x,y)}{p(x)p(y)}\right)$$

In decision trees mutual information gain and information gain are synonymous:

$$I(X;Y)=H(Y)-H(Y|X)$$

# ID3 Algorithm

Recursively perform on all examples.

* For all $+$/$-$ examples return single node with corresponding label.
* Otherwise split on attribute that best classifies current set of examples.

# Decision Trees Features

- Hypothesis space is complete
- Only single hypothesis as output
- No backtracking
- Statistically based choices
- True bias hard to estimate
- Shorter trees are preferred
- Trees with high information gain near root are preferred

# Overfitting

Hypothesis $h\in \cal H$ overfits $X$ if $\exists h'$ such that:

$E(h\|X)< E(h'\|X)$ but $E_p(h)>E_p(h')$ where $p$ is the entire distribution of data.

Strategies:

- Stop when insignificant information gain
- post pruning  - subtrees/rules/
- using ensembles

# Problems

- Real values functions - sort and split on midpoints
- Alternative measures for selecting attributes - gain ratio / cost sensitive information gain
- Missing attribute values - most commomn value at node / node with same target value / probability based on descendents of node

# Advantages / Disadvantages

- Easy to explain
- No hyperparameters
- Overfitting
- Low accuracies (cf. other approaches)

# Random Forests

##  Instane Bagging / Bootstrap aggregation

- Generate $K$ different bootstrapped trainig datasets (sampling with replacement)
- Learn a decision tree on each
- Final prediction is the majority/average vote of all.

## Freature bagging

- Improved than instance bagging
- Build a decision tree using a subset of $m$ features rather than all $D$ features, typically $m\approx \sqrt D$
