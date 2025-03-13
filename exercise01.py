'''
Question 1
Many functions in Python deal with numbers in a half-closed intervals.

For example, range(n) returns integers in the interval [0, n).

When we deal with integers, it is very easy to include n - we simply add 1 to
it.

For example, to generate integers in the range [a, b], we use range(a, b+1).

However, when it comes to real numbers there is no (mathematically speaking)
"next" real number.

But for floats, remember that these are actually not real numbers, but
approximations with some fixed precision - in those cases it is indeed possible
to always calculate the "next" number after any given float.

Read the Python documentation for the math module, and find in there a function
that will help you calculate the "next" number after some given float.

(You will need Python 3.9 and above for this)
'''