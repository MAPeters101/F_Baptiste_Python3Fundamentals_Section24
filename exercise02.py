'''
Question 2
Given a sequence of points, each one with possibly different number of
dimensions, generate a list that contains the magnitude (norm) of the point.

For an n-dimensional point (therefore containing n components):

x = (x_1, x_2, ..., x_n)
this value can be computed as:

sqrt(x_1 ** 2 + x_2 ** 2 + ... + x_n **2)
Write a function that performs this calculation and returns the norm of each
point given in some sequence.

For example, if the sequence is:

data = [
    (0, 1),
    (1, 2, 3),
    (1, 3, 5, 7),
    (1, 1, 2, 3, 5, 8, 13)
]
Your function should return this list:

[1.0, 3.741657386773941, 9.16515138991168, 16.522711641858308]
(Hint: you may want to read the math module docs to see if you can find a
function in there that might help you out!)
'''