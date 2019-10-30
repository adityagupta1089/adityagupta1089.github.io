---
layout: post
title: String Matching
categories:
- Notes
- Algorithms
date: 2019-10-31 00:42 +0530
---
# Formalization:

- Text: $T[1..n]$
- Pattern: $P[1..m]$ ($m\le n$)
- elements of $P$ and $T$ are characters drawn from a finite alphabet $\Sigma$.
- $\Sigma^*$ denotes the set of all finite-length string using $\Sigma$
- $\varepsilon\in \Sigma ^*$ emptry string
- $x y$ denotes concatenation of $x$ and $y$
- $w\sqsubset x$: $w$ is a prefix of $x$, i.e. $x=wy$ for some $y\in \Sigma^*$
- $w\sqsupset x$: $w$ is a suffix of $x$, i.e. $x=yw$ for some $y\in \Sigma^*$
- $P_k$ is the $k$-character prefix $P[q..k]$

# Comparison of Algorithms:

| Algorithm          | Preprocessing time | Matching Time |
| ------------------ | ------------------ | ------------- |
| Naive              | 0                  | $O((n-m+1)m)$ |
| Rabin-Karp         | $\Theta(m)$        | $O((n-m+1)m)$ |
| Finite Automaton   | $O(m\vert \Sigma\vert)$     | $\Theta(n)$   |
| Knuth-Morris-Pratt | $\Theta(m)$        | $\Theta(n)$   |
| Z-Algorithm | 0 | $\Theta(m+n)$ |

# Rabin-Karp algorithm
Based on certain assumptions its average-case running time is better.

Let us assume $\Sigma=\{0,1,2,\ldots,d\}$. Let $p$ denote the interpretation of $P[1..m]$ as a radix-d number. Similarly let $t_s$ denote the interpretatin of $T[s+1\ldots s+m]$ for $s\in \{0,1,\dots n-m\}$. Now $t_s=p\iff T[s+1\ldots s+m]=P[1..m]$. 

We can compute $p$ in $\Theta(m)$ using Horner's rule

$p=P[m]+10(P[m-1]+10(P[m-2]+\ldots))$

Similarly 

$t_{s+1}=10(t_s-10^{m-1}T[s+1])+T[s+m+1]$

where we can calculate $10^{m-1}$ in $O(\lg m)$.

For string matching we work with $\mathbb Z_q$ where $q$ is a prime such that $dq$ fits inside a computer word. However $t_{s} \equiv p\pmod q$ doesn't imply that $t_s=p$, but $t_s\not\equiv p\mod q\implies t_s\neq p$. So we additionaly check explicity string equality.

In worst case it could be $\Theta((n-m+1)m)$ when all shifts are valid.

In average case we expect only $c$ shifts to be valid, then matching time is $O((n-m+1)+cm)=O(n+m)$ plus time required to process spurious hits. We can expect the number of spurious hits to be $O(n/q)$ since $t_s\equiv p\pmod q$ with probability $1/q$. This makes the expected matching time to be $O(n)+O(m(\nu+n/q))$ where $\nu$ is number of valid shifts. This is $O(n)$ if $\nu=O(1)$ (expected number of valid shifts is small) and $q\ge m$ ($q$ larger than the length of pattern)

# Finite Automata

## Definition

A finite automaton $M(Q, q_0, A, \Sigma, \delta)$ where 

- $Q$: states, 
- $q_0\in Q$: start state, 
- $A\subseteq Q$: accepting states,
- $\Sigma$: input alphabet
- $\delta:Q\times \Sigma\mapsto Q$: transition function 

$M$ induces a function $\phi:\Sigma^*\mapsto Q$ (final-state function) such that $\phi(w)$ is the state $M$ ends up in after scanning the string $w$. $M$ accepts a string $w$ iff $\phi(w)\in A$.

$\phi(\varepsilon)=q_0$

$\phi(wa)=\delta(\phi(w), a)\text{ for }w\in\Sigma^*, a\in \Sigma$

## String-matching automata

For $P$ we generate a string-matching automaton in a preprocessing step.

For this we define an auxilary function $\sigma:\Sigma^*\mapsto\{0,1,\ldots,m\}$, the suffix function corresponding to $P$. $\sigma(x)$ is the length of the longest prefix of $P$ that is also a suffix of $x$.

$\sigma(x)=\max\{k: P_k \sqsupset x\}$

We have $\sigma(x)=m\iff P\sqsupset x$, also $x\sqsubset y\implies \sigma(x)\le \sigma(y)$ from definition.

We define **string-matching automaton** as:

- $Q=\{0,1,\ldots,m\}$, $q_0=0$, $A=\{m\}$
- $\delta(q, a)=\sigma(P_qa)$ is the longest prefix of pattern $P$ that has matched the text string $T$ so far.

We consider most recently read characters of $T$. For $T_i=P_j$, $P_j\sqsupset T_i$. 

Let $q=\phi(T_i)$. We design $\delta$ such that at $q$, $P_q\sqsupset T_i$ and $q=\sigma(T_i)$. Therefore $\phi(T_i)=\sigma(T_i)$.

If the automaton is in state $q$ and reads the next characters $T[i+1]=a$, then we want the transition to lead to the state corresponding to the longest prefix of $P$ that is a suffix of $T_ia$, i.e. $\sigma(T_ia)$.

Because $P_q$ is the longest prefix of $P$ that is a suffix of $T_i$ , i.e. $P_q=\sigma(T_i)$ we also have the longest prefix of $P$ that is a suffix of $T_ia$ is not only $\sigma(T_ia)$ but also $\sigma(P_qa)$.

- If $a=P[q+1]$, $\delta(q, a)=q+1$.
- If $a\neq P[q+1]$ we find a smaller prefix of $P$ that is also a suffix of $T_i$.

# Kunth-Morris-Pratt Algorithm

Given a pattern $P[1..m]$, the **prefix function** for the pattern $P$ is the function $\pi:\{1,2,\ldots, m\}\mapsto\{0,1,\ldots, m-1\}$ such that

$\pi[q]=\max\{k:k<q\wedge P_k\sqsupset P_q\}$

i.e. $\pi[q]$ is the length of the longest prefix of $P$ that is a proper suffix of $P_q$.

For matching:

- Scan the text $T$ from left to right starting with $q=0$ (number of characters matched is $0$ initially):
    - If next character doesn't match, i.e. $P[q+1]\neq T[i]$, then $q\leftarrow\pi[q]$
    - If next character matches, i.e. $P[q+1]=T[i]$, then $q\leftarrow q+1$
    - If $q=m$, pattern is found, and set $q\leftarrow\pi[q]$

For computing prefix-function:

- $\pi[1]\leftarrow0$ by definition

- Scan the pattern $P$ from left to right starting from $q=2$:
    - If next character doesn't match, i.e. $P[k+1]\ne P[q]$, then $k\leftarrow\pi[k]$
    - If next character matches, i.e. $P[k+1]=P[q]$, then $k\leftarrow k+1$.
    - Set $\pi[q]\leftarrow k$

# Z-Algorithm

The algorithm produces an array $Z$  where $Z[i]$ denotes the length of the longest substring starting from $S[i]$ which is also a prefix of $S$. We refer to prefix-substrings as substrings which are also prefix.

As we iterate over the letters in the string we maintain an interval $[L, R]$ which is the interval with maximum $R$ such that $1\le L\le i\le R$ and $S[L\ldots R]$is a prefix-substring (if no such inteval exists $L=R=-1$)

Now suppose we have correct interval $[L, R]$ for $i-1$ and for all values of $Z$ upto $i-1$, we will compute  $Z[i]$ and new $[L, R]$ by following steps:

- $i>R$: 
    - there is not a prefix-substring of $S$ that starts before $i$ and ends at $\ge i$. We would have taken that interval instead.
    - Set $[L,R]$ to $[i,i]$ and start comparing $S[0...]$ to $S[i...]$ and $Z[i]=R-L+1$.
- $i\le R$:
    - Let $k=i-L$. We know that $Z[i]\ge \min (Z[k], R-i+1)$
    - $Z[k]<R-i+1$:
        - $Z[i]=Z[k]$
    - $Z[k]\ge R-i+1$:
        - Update $[L,R]$ to $[i,R]$ and start comparing $S[R+1...]$ to $S[k+1...]$

For pattern matching we use Z-algorithm on string $P\Phi T$ where $\Phi$ matches nothing Then indices with $Z[i]=m$ correspond to matches in $T$ of $P$.

