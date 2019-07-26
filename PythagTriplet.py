# The below solution to the Pythagorean triplet programming
# challenge leverages the fact that once one variable is known,
# the remaining system of equations, a + b + c = N and
# a^2 + b^2 = c^2 can be solved by substitution. Thus, this
# problem can be solved in O(N/3) = O(N) time without needing
# to loop through each of a, b, and c.


def pythag_triplet(N):
    """Returns the maximum product of a Pythogorean
       triplet (a, b, c) with a < b < c, a + b + c = N, and
       a^2 + b^2 = c^2. This function runs in O(N) time."""

    product = -1
    # a must be less than N/3 or a < b < c and a + b + c = N
    # cannot both be satisfied.
    for a in range(1, N / 3):
        d = N - a
        c = (pow(a, 2) + pow(d, 2)) / (2.0 * d) # compute c directly
        if c == round(c): # ensure that c is an integer solution
            b = N - a - c # compute b directly
            if a * b * c > product:
                product = a * b * c

    return product

# test program
for i in range(100):
    print(pythag_triplet(i))

