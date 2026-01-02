
# Problem

This problem asks the following:

Let $(F_n)_{n \geq 1}$ be the Fibonacci sequence defined by

$$F_1 = 1, \qquad F_2 = 2, \qquad
F_n = F_{n-1} + F_{n-2} \quad \text{for } n \geq 3.$$

Consider all terms of this sequence whose values do not exceed

$$N = 4\,000\,000.$$

Among these, select only the even-valued terms,
i.e., those $F_n$ such that

$$F_n \equiv 0 \pmod{2}
\quad \text{and} \quad
F_n \leq N.$$

Let these even terms be denoted by $F_{n_1}, F_{n_2}, \dots, F_{n_k}$,
where $k$ is the total number of such terms.
The task is to compute the sum

$$S = \sum_{i=1}^{k} F_{n_i},$$

that is, the sum of all even Fibonacci numbers not exceeding $4\,000\,000$.

# Solution

The solution is rather simple. My code essentially forms the Fibonacci sequence and for each new term $F_n$ tests whether $F_n \equiv 0 \pmod{2}$; if it is it is added to the running total. This gives the correct result. 
