---
layout: post
title: "Supervised Learning"
date: Monday, 14 October 2019

categories: ["Notes", "Machine Learning"]
---
Given a set $(x,y)$ need to estimate $f(x)=y$ .

Terms:

* Feature $x_i$ - property of object to be classified
* Instance $x=\begin{pmatrix}x_1&x_2&x_3&\ldots\end{pmatrix}$ - features of an object
* Instance Space $\cal I$ - space of all possible instances
* Class $\cal Y$ - categorical feature of an object
* Example $(x,y)$ - instance with membership
* Training Set $X = {}_{i=1}^N\{x_i,y_i\}$
* Target Concept $\cal C$ - correct expression of class.
* Concept Class - Space of all possible concepts
* Hypothesis $h :x\mapsto\{0,1\}$ - Approximation to target concept
* Hypothesis class $\cal H$ - Space of all possible hypothesis
* Learning Goal - Find $h\in\cal H$ that closely approximates $\cal C$ (possible $\cal C\not\in H$)

Errors:

* Empirical: $E(h\|X) = \frac 1N\sum_{t=1}^N 1(h(x_t)\ne y_t)$
* Generalization: instances not in $X$
* True: instances in $\cal I$
* Most specific and general hypothesis $\cal S$ and $\cal G$ covering fewest and most instances. 
* Version space - between $\cal S$ and $\cal G$