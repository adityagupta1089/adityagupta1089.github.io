---
layout: post
title: Strassen Matrix Multiplication
categories:
- Notes
- Algorithms
date: 2019-10-27 00:16 +0530
---
The product of two $n\times n$ matrices $X$ and $Y$ which takes $O(n^3)$

$$X=\begin{bmatrix}A&B\\C&D\end{bmatrix}$$

$$Y=\begin{bmatrix}E&F\\G&H\end{bmatrix}$$

is 
$$
XY=\begin{bmatrix}A&B\\C&D\end{bmatrix}\begin{bmatrix}E&F\\G&H\end{bmatrix}=\begin{bmatrix}AE+BG&AF+BH\\CE+DG&CF+DH\end{bmatrix}
$$


here $T(n)=8T(n/2)+O(n^2)\implies O(n^3)$

Strassen gave:

$$
XY=\begin{bmatrix}P_5+P_4-P_2+P_6&P_1+P_2\\P_3+P_4&P_1+P_5-P_3-P_7\end{bmatrix}
\$$

where

$$\begin{align}
P_1&=A(F-H)&P_5&=(A+D)(E+H)\\
P_2&=(A+B)H&P_6&=(B-D)(G+H)\\
P_3&=(C+D)E&P_7&=(A-C)(E+F)\\
P_4&=D(G-E)\\
\end{align}
$$

The new running time is $T(n)=7T(n/2)+O(n^2)$ which by the master theorem works out to be $O(n^{\log_27})\approx O(n^{2.81})$