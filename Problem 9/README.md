# Special Pythagorean Triplet — Project Euler #9

## Problem

A **Pythagorean triplet** is a set of three natural numbers \(a<b<c\) for which

$$
a^2 + b^2 = c^2.
$$

For example,

$$
3^2 + 4^2 = 9 + 16 = 25 = 5^2.
$$

There exists **exactly one** Pythagorean triplet for which

$$
a + b + c = 1000.
$$

The task is to find the product \(abc\).

---

## Solution

My intial solution was a direct search. It iterates through integers $c$ up to $n$ (here \(n=1000\)), then $b$ up to $c$, and $a$ up to $b$, checking the two constraints

$$
a^2 + b^2 = c^2, \qquad a + b + c = 1000.
$$

Once a valid triplet is found, it prints the product $abc$.

This is slower than it needs to be, but it’s conceptually simple and works comfortably within the problem size.

### A faster alternative (Euclid’s formula)

A more efficient approach uses Euclid’s parametrisation of Pythagorean triples:

$$
a = k(m^2-n^2), \quad b = k(2mn), \quad c = k(m^2+n^2),
$$

with integers $m>n\ge 1$ and $k\ge 1$.  
Then the sum condition becomes

$$
a+b+c = 2km(m+n) = 1000 \quad \Longleftrightarrow \quad km(m+n)=500,
$$

so the search space collapses to scanning feasible \((m,n)\) (and \(k\)) rather than \((a,b,c)\).

---

## Result

The unique triplet is

$$
(a,b,c) = (200,\,375,\,425),
$$

so

$$
abc = 200\cdot 375\cdot 425 = 31{,}875{,}000.
$$

