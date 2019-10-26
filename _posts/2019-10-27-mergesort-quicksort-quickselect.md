---
layout: post
title: Mergesort, Quicksort and Quickselect
categories:
- Notes
- Algorithms

date: 2019-10-27 00:05 +0530
---
# Mergesort

Split the list into 2 halves, recursively sort each half and then merge the two sorted sublists. For merging $x[1..k]$ and $y[1..l]$ into $z[1..k+l]$. The first element of $z$ is smaller of $x[1]$ and $y[1]$ and rest can be constrcuted recrusively.

$$
\begin{align}
\text{mergesort}(a[1..n]) =&\text{merge}(\text{mergesort}(a[1..\lfloor n/2\rfloor]),\\&\quad\text{mergesort}(a[\lfloor n/2\rfloor+1...n]))\\
\text{merge}(x[1..k],y[1..l])=&\begin{cases}x[1]\circ\text{merge}(x[2..k],y[1..l])&x[1]\le y[1]\\y[1]\circ\text{merge}(x[1..k],y[2..l])&\text{otherwise}\end{cases}
\end{align}
$$

Time Complexity $T(n)=2T(n/2)+O(n)\implies O(n\log n)$

# Quicksort & Quickselect

Select a pivot $v$ (pick randomly). Split the array into three categories: elements smaller than $v$, those equal to $v$ and those greater than $v$. Call these $S_L$, $S_v$, and $S_R$ respectively. Recursively sort the array.

Time complexity: $O(n^2)$ worst case. $O(n\log n)$ best and average case.

For selecting the $k^{\rm th}$ element:
$$
\text{selection}=
\begin{cases}
\text{selection(S_L, k)}&k\le |S_L|\\
v &|S_L|<k\le|S_L|+|S_v|\\
\text{selection}(S_R, k-|S_L|-|S_v|)&k>|S_L|+|S_v|
\end{cases}
$$
Time complexity: $T(n)=T(n/2)+O(n)\implies O(n)$