# PolynomialSequenceSolver
Finds the general term of any sequence that can be represented as a polynomial (arithmetic, quadratic, cubic and beyond!)

# Inspiration
I wanted an online tool that could easily create a general rule for a quadratic sequence, and wasn't able to find any online apart from WolframAlpha's sequence widget.
Online tools which find the general term of sequences are usually for either arithmetic and geometric sequences.
A few days ago I came across the WolframAlpha widget which when inputted with at most 5 terms of a sequence, could construct a general rule. It worked for arithmetic, quadratic and cubic sequences.

However, I was interested in how it worked and wanted to make my own program that would be able to create a general rule for ANY sequence that can be expressed as a polynomial (sequences wherein the `n`th difference is constant).

More formally, I wanted to construct the function ![](https://latex.codecogs.com/svg.image?p(x)%20=%20an%5E0%20&plus;%20bn%5E1%20&plus;%20cn%5E2...) where ![](https://latex.codecogs.com/svg.image?n%20%5Cin%20%5Cmathbb%7BR%7D) with a degree `d` when given `d+2` input output pairs of the function.

# How does it work?
Firstly, the program determines the degree of the polynomial by looking at which difference is constant. The `n`th difference being constant usually means that a polynomial with a degree `n` can be created in order to model the sequence.


After getting the degree of the polynomials, a system of equations can be constructed and linear algebra can be used in order to solve these system of equations.

This can be best explained via the use of an example.

Knowing that ![](https://latex.codecogs.com/svg.image?p(x)%20=%20an%5E2%20&plus;%20bn%20&plus;%20c) and the sequence is `[2, 5, 9]`, we can say that:

![](https://latex.codecogs.com/svg.image?a1%5E2&plus;b1%5E1&plus;c1%5E0%20=%202)

![](https://latex.codecogs.com/svg.image?a2%5E2&plus;b2%5E1&plus;c2%5E0%20=%205)

![](https://latex.codecogs.com/svg.image?a3%5E2&plus;b3%5E1&plus;c3%5E0%20=%209)

We can convert this to a dot product:


![](https://latex.codecogs.com/svg.image?%5Cbegin%7Bpmatrix%7D1%5E2&1%5E1&1%5E0%5C%5C2%5E2&2%5E1&2%5E0%5C%5C3%5E2&3%5E1&3%5E0%5C%5C%5Cend%7Bpmatrix%7D%5Cbegin%7Bpmatrix%7Da%5C%5Cb%5C%5Cc%5Cend%7Bpmatrix%7D%20=%5Cbegin%7Bpmatrix%7D2%5C%5C5%5C%5C9%5Cend%7Bpmatrix%7D%20)

Therefore,

![](https://latex.codecogs.com/svg.image?%5Cbegin%7Bpmatrix%7Da%5C%5Cb%5C%5Cc%5Cend%7Bpmatrix%7D%20=%5Cbegin%7Bpmatrix%7D2%5C%5C5%5C%5C9%5Cend%7Bpmatrix%7D%20%5Cbegin%7Bpmatrix%7D1%5E2&1%5E1&1%5E0%5C%5C2%5E2&2%5E1&2%5E0%5C%5C3%5E2&3%5E1&3%5E0%5C%5C%5Cend%7Bpmatrix%7D%5E%7B-1%7D%20)

or,
![](https://latex.codecogs.com/svg.image?X=A%5E%7B-1%7DB)

The cool thing is that this applies in general, when the pattern is cubic, `A` and `B` can be extended vertically to add another equation, and `A` can be extended horizontally to add another term to each equation.

In code, `A` can be represented as a 2D array which can be constructed by performing a ![](https://latex.codecogs.com/svg.image?O(n%5E2)) loop over each index, and then over each power, and  then evaluating the exponentiation.

`B` can simply be constructed by looping over the output of the function (looping over the sequence itself)

Finally, the dot product and inverse can be evaluated using the help of `numpy` to get `X`.
