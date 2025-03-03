'''
Question 1
Many functions in Python deal with numbers in a half-closed intervals.

For example, range(n) returns integers in the interval [0, n).

When we deal with integers, it is very easy to include n - we simply add 1 to it.

For example, to generate integers in the range [a, b], we use range(a, b+1).

However, when it comes to real numbers there is no (mathematically speaking) "next" real number.

But for floats, remember that these are actually not real numbers, but approximations with some fixed precision - in those cases it is indeed possible to always calculate the "next" number after any given float.

Read the Python documentation for the math module, and find in there a function that will help you calculate the "next" number after some given float.

(You will need Python 3.9 and above for this)

Question 2
Given a sequence of points, each one with possibly different number of dimensions, generate a list that contains the magnitude (norm) of the point.

For an n-dimensional point (therefore containing n components):

x = (x_1, x_2, ..., x_n)
this value can be computed as:

sqrt(x_1 ** 2 + x_2 ** 2 + ... + x_n **2)
Write a function that performs this calculation and returns the norm of each point given in some sequence.

For example, if the sequence is:

data = [
    (0, 1),
    (1, 2, 3),
    (1, 3, 5, 7),
    (1, 1, 2, 3, 5, 8, 13)
]
Your function should return this list:

[1.0, 3.741657386773941, 9.16515138991168, 16.522711641858308]
(Hint: you may want to read the math module docs to see if you can find a function in there that might help you out!)

Question 3
Given an arbitrary sequence of numerical values, write a function that "analyzes" the sequence by generating print outputs of:

number of elements
number of unique elements
the min
the max
the mean
the standard deviation
all the modes (if there are more than one)
the 25th, 50th, and 75th percentiles
For example, given this list of numbers:

data = [
    61, 35, 99, 100, 75, 94, 88, 14, 21, 39, 53, 25, 87, 84,
    81, 55, 86, 18, 69, 44, 16, 33, 66, 52, 70, 52, 95, 45,
    94, 35, 68, 70, 52, 53, 30, 87, 79, 51, 92, 72, 55, 40,
    15, 74, 86, 87, 91, 70, 45, 37
]
For calculations that result in floats, display only 3 digits after the decimal point for those result.

Your function should print information such as this to the console:

count: 50
unique count: 38
min: 14
max: 100
mean: 60.800
std dev: 25.283
modes: [87, 52, 70]
25th percentile: 39.750
median: 63.500
75th percentile: 86.000
'''