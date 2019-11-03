---
layout: post
title: Count Good Substrings (Codeforces Problem 451D)
categories: ["Programming"]

---

This solution is for [this](https://codeforces.com/problemset/problem/451/D) problem where we need to find number of substrings for a given string $s$ such that when we merge consecutive equal characters to a single character, it is a palindrome which we call as good substring. The given string only has $a$ and $b$ characters. We need to separately calculate even and odd length strings.

We will represent the solution using an element $(e, o)$ (where $e,o\in\mathbb Z^+$) of a [commutative ring](https://en.wikipedia.org/wiki/Commutative_ring) $R$ with two binary operators ($+$) and ($\cdot$ ) defined as:

- $(e_1,o_1)+(e_2,o_2)=(e_1+e_2,o_1+o_2)$
- $(e_1,o_1)\cdot(e_2,o_2)=(e_1\cdot e_2+o_1\cdot o_2,e_1\cdot o_2+e_2\cdot o_1)$
- Additive identity $(0,0)$, Additive inverse $(-e, -o)$
- Multiplicative identity $(1,0)$

We can verify the rest of the properties easily.

For this we note that the given string will contain alternating $a$'s and $b$'s. Let their count be $n_1, n_2, n_3$ and so on until $n_m$.

If we take only $a$'s or $b$'s we will get always a palindrome. Let the total ways to select consecutive $a$'s from $n$ $a$'s be $\lambda(n)\in R$. For this we also define $\mu(n)$ which counts only those substrings which include the last letter (e.g. $\mu(1)=(0,1)$). We see that when calculating $\mu(n)$ we can use $\mu(n-1)$, For even we just add the last character $a$ to all odd ones and similarly for odd we add $a$ to even ones, additionally we have a singleton $a$. So if $\mu(n-1)=(e,o)$ then $\mu(n)=(o,e+1)$. More formally $\mu(n)=\mu(n-1)\mu(1)+\mu(1)$, because total ways for $n$, $\mu(n)$ equals total ways for $n-1$, $\mu(n-1)$ times total ways for additional length $1$ character, $\mu(1)$ plus the case of singleton character which is not covered because $\mu(n-1)$ does not count empty strings.

We note that $\lambda (n)=\sum_{i=1}^n\mu(i)$ which means counting substrings ending at position $i$'s.

Now, we need to consider palindromes of type $a^{(n_1)}b^{(n_2)}a^{(n_3)}b^{(n_4)}\ldots a^{(n_m)}$. If we take any two odd $i$ we will get a palindrome starting and ending at $i$, similarly for even $i$. We also define $\theta(n)$ to be the ways of including a substring of length $n$, which is $(1,0)$ if $2\mid n$ and $(0,1)$ otherwise. 

An example for total count in case of odd $i$'s then becomes:

- $\mu(n_1)\theta(n_2)\mu(n_3)$ for $n_1$ and $n_3$
- $\mu(n_1)\theta(n_2+n_3+n_4)\mu(n_5)$ for $n_1$ and $n_5$ 
- and so on...

i.e. $\displaystyle S(m)=\sum_{i, j\in\{1,3,5,7\ldots m\},i<j}\mu(n_i)\theta\left(\sum_{k=i+1}^{j-1}n_k\right)\mu(n_j)$.

We calculate this using a dynamic programming method. For calculating $S(m)$, suppose $S(m-2)$ is already calculated, then we only have terms to add with $\mu(n_m)$. We maintain a sum (let's assume $m$ to be odd for simplicity) 

$$
\begin{align}T(m)&=\mu(n_1)\theta(n_1+n_2+...n_{m-1})\\&+\mu(n_3)\theta(n_4+n_5+...n_{m-1})\\&+...\\&+\mu(n_{m-2})\theta(n_{m-1})\end{align}
$$

We note that $T(m)=T(m-2)\theta(n_{m-1}+n_{m-2})+\mu(n_{m-2})\theta(n_{m-1}))$ where we have used $\theta(a+b)=\theta(a)\theta(b)$.

So we can easily calculate $S(m)=S(m-2)+T(m)\mu(n_m)$.

So we can calculate in linear time $S(m)$ for even and odd $i$'s (in one of the case it will be $S(m-1)$). Then we can add $\sum\lambda(n_i)$ to get the final solution.

