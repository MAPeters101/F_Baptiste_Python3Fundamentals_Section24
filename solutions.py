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

Solution
The function we are interested in is called nextafter.

Let's see how it works when we use it with 1 and get the next number (towards 10 for example):

import math
e = math.nextafter(1, 10)
e
Hopefully when you read the documentation, you also saw references to math.inf.

We'll actually circle back to this in a later section of this course, but you should now be aware that the IEEE standard does allow for a special representation of "infinite" floats.

We can create these floats using math.inf:

a = math.inf
a
As you can see the string representation is "inf", but this is a float:

type(a)
This means that we can also use it when we use the nextafter function without worrying about what to use as the "towards" number if we always just want to go right on the number scale:

e = math.nextafter(1, math.inf)
e
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

Solution
We can certainly do this the "hard" way by manually calculating each norm.

For example, given some point:

x = (1, 2, 3)
We can calculate it's norm this way:

norm_x = math.sqrt(x[0] ** 2 + x[1] ** 2 + x[2] ** 2)
norm_x
3.7416573867739413
The problem is that we have "hard coded" the formula - if our point looks like this:

y = (1, 1, 2, 3, 5, 8, 13)
We have to modify our formula. So, our approach is not generic enough.

We could write a small helper function to do this more generically for us:

def norm(pt):
    sum_ = 0
    for coord in pt:
        sum_ += coord ** 2
    return math.sqrt(sum_)
Now we can call this function on any sized point:

norm(x)
3.7416573867739413
norm(y)
16.522711641858304
We can actually simplify our function by using a comprehension:

def norm(pt):
    return math.sqrt(sum(coord ** 2 for coord in pt))
norm(x)
3.7416573867739413
norm(y)
16.522711641858304
Now that we have this function created, we can write a function that generates the norm for every point in some given sequence such as the one provided in the question:

data
[(0, 1), (1, 2, 3), (1, 3, 5, 7), (1, 1, 2, 3, 5, 8, 13)]
def gen_norms(data):
    return [norm(pt) for pt in data]
gen_norms(data)
[1.0, 3.7416573867739413, 9.16515138991168, 16.522711641858304]
The math module actually has a function called hypot which does exactly what our norm function does.

This function however, requires the individual coordinates be passed as positional arguments - so we need to unpack the tuple into positional arguments:

In other words, for the point (1, 1) we have to pass the coordinates this way:

math.hypot(1, 1)
1.4142135623730951
If we have a tuple containing (1, 1), then we can call the hypot function this way:

t = (1, 1)
math.hypot(*t)
1.4142135623730951
And for example:

math.hypot(*x)
3.741657386773941
math.hypot(*y)
16.522711641858308
We can now re-write our second function this way:

def gen_norms(data):
    return [math.hypot(*pt) for pt in data]
gen_norms(data)
[1.0, 3.741657386773941, 9.16515138991168, 16.522711641858308]
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
Solution
We already know about the min and max functions that are built-in.

We can use the len function to calculate the number of elements in the sequence.

For the number of unique elements, we can transform our data into a set first, and obatin the len of that set.

Furthermore the statistics module provides functions such as:

mean
stdev
quantiles
multimode
Let's write a function that will perform all these calculations and print this analysis.

import statistics as stats

def describe(data):
    num_elements = len(data)
    num_unique_elements = len(set(data))
    min_ = min(data)
    max_ = max(data)
    mean = stats.mean(data)
    stdev = stats.stdev(data)
    multi_mode = stats.multimode(data)
    quartiles = stats.quantiles(data, n=4)

    print(f'count: {num_elements}')
    print(f'unique count: {num_unique_elements}')
    print(f'min: {min_}')
    print(f'max: {max_}')
    print(f'mean: {mean:.3f}')
    print(f'std dev: {stdev:.3f}')
    print(f'modes: {multi_mode}')
    print(f'25th percentile: {quartiles[0]:.3f}')
    print(f'median: {quartiles[1]:.3f}')
    print(f'75th percentile: {quartiles[2]:.3f}')

describe(data)
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