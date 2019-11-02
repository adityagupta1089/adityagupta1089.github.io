---
layout: post
title: Closest Pair of Points
categories:
- Notes
- Algorithms
date: 2019-11-02 20:34 +0530
---
# The divide-and-conquer algorithm

We need to find the closest pair of points in a set $Q$ of $n\ge 2$ points. Brute force will take $\Theta(n^2)$ time.

Each recursive call takes as input a subset $P\subseteq Q$ and arrays $Z$ and $Y$ each of which contains all the points o fhte input subset $P$. Points in $X$ are sorted on their $x$-coordinates monotonically increasing and $Y$ is sorted on monotonically increasing $y$-coordindate.

If $\vert P\vert\le 3$ we use brute force method otherwise:

-  **Divide**: Find a vertical line $l$ that bisects the point set $P$ intro two sets $P_L$ and $P_R$ such that $\vert P_L\vert =\lceil \vert P\vert /2\rceil$, $\vert P_R\vert =\lfloor \vert P\vert /2\rfloor$. Divide $X$ into $X_L$ and $X_R$. Similarly $Y$ into $Y_L$ and $Y_R$.
- **Conquer**: Make two recursive calls one in $P_L$ and other one $P_R$ for closest pair of point. Let the closest-pair distances returned be $\delta_L$ and $\delta_R$ respectively and let $\delta=\min(\delta_L, \delta_R)$
- **Combine**: The closest pair is either (i) the pair with $\delta$ or   (ii) a pair of point with one in $P_L$ and one in $P_R$ whose distance is less than $\delta$
    - Create $Y'$ which is the array $Y$ with all points in $2\delta$-wide vertical strip around $l$ 
    - For each point $p$ in $Y'$ try to find points in $Y'$ that are withing $\delta$ units of $p$. Only $7$ points in $Y'$ that follow $p$ need to be considered. Compute distance from $p$ to each of these 7 points and keep track of the closest-pair distance $\delta'$ found over all pairs of points in $Y'$. 
    - Return pair of point with smallest distance $\delta'$ or $\delta$.

## Why only 7 points?

![]({{site.baseurl}}/images/closestpair.png)

Suppose $p_L\in P_L$ and $p_R\in P_R$ have distance less than $\delta$. $p_L$ and $p_R$ should be individually less than $\delta$ distance from $l$. They are also within $\delta$ distance of each other vertically. So they must be in $\delta\times 2\delta$ rectangle as shown.

 Consider a $\delta\times\delta$ square forming the left half of a $\delta\times 2\delta$ rectangle, since all points withing $P_L$ are atleast $\delta$ apart, atmost 4 points in $P_R$ can reside withing the $\delta\times \delta$ square. Similarly 4 for right side and total 8 points.

Therefore we need to only check next 7 points.

## Time Complexity

$T(n)=2T(n/2)+O(n)\implies O(n\log n)$

