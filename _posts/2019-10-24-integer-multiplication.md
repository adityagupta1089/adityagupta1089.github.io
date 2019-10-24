---
layout: post
title: Integer Multiplication
categories:
- Notes
- Data Structures
mathjax: true
date: 2019-10-24 20:32 +0530
---
To multiply $x$ and $y$, split them into left and right halves which are $n/2$ bits long.


$$
\begin{align}
x&=2^{n/2}x_L+x_R\\
y&=2^{n/2}y_L+y_R\\
xy&=(2^{n/2}x_L+x_R)(2^{n/2}y_L+y_R)\\
&=2^nx_Ly_L+2^{n/2}(x_Ly_R+x_Ry_L)+x_Ry_R\\
x_Ly_R+x_Ry_R&=(x_L+x_R)(y_L+y_R)-x_Ly_L-x_Ry_R
\end{align}
$$


Additional and multiplication by power of 2 takes linear time. We only need to calculate $x_Ly_L$, $x_Ry_R$ and $(x_L+x_R)(y_L+y_R)$ which we can calculate recursively.

$T(n)=3T(n/2)+O(n)\implies T(n)=O(n^{\log_23})=O(n^{1.59})$ 