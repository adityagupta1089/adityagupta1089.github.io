---
layout: post
title: Splay Trees

categories:
- Notes
- Data Structures
---
Self-adjusting binary trees that work in $O(\log n)$ amortized time bound. The operation performed is the _splay_ operation. 

For a splay operation at node x: ($p(x)$ is the parent of $x$)

- **Case (a):** If $x$ has a parent but no grandparent we rotate at $p(x)$.
- **Case (b):** If $x$ has a grandparent and both $x$ and $p(x)$ are both left or right childrenn, we rotate at $p^2(x)$ and then at $p(x)$.
- **Case (c):** If $x$ has a grandparent and $x$ is a left and $p(x)$ is a right child, or vice versa, we rotate at $p(x)$ and then at the new parent of $x$.

![]({{site.url}}{{site.baseurl}}/images/splaytree1.png)

This moves $x$ to the root of the tree while rearranging the rest of the original path to $x$.

We perform a splay operation during each access or update operation. Using amortized time analysis for $m$ operations total time taken is $O(m\log n)$ or $O(\log n)$ amortized time per operation.

# Amortized Time Analysis

TODO