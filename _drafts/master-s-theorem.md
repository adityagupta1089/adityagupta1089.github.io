---
layout: post
title: Master's Theorem
categories: ["Notes", "Data Structures"]
mathjax: True

---

If $T(n)=aT(\lceil n/b\rceil)+O(n^d)$ for some constants $a>0,b>1,d\ge 0$ then

$$
T(n)=\begin{cases}
O(n^d)&d>\log_b a\\
O(n^d\log n)&d=\log_ba\\
O(n^{\log_ba})&d<\log_ba
\end{cases}
$$
