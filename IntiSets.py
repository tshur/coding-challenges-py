#
# File:        IntiSets.py
# Created by:  Tim Shur
# Date:        2/21/17
#
# Description: This program calculates the sum of all numbers in the Inti Set
#              of n between a and b. That is, this program sums all of the numbers
#              that are relatively prime (co-prime) to n. First, this program finds
#              a list of the distinct prime factors of n and then checks each number
#              between a and b to see if they are also divisible by one of these
#              factors. If a number is not divisible by any of these factors, then it
#              is co-prime to n, so it is included in the sum total.
#
# Big-O complexity: O(q * (b - a) * f), where q is the number of queries, (b - a) is
#              the interval, and f is the number of distinct prime factors of n. From
#              the internet, I got that f <= log(n) / log(log(n)), and is on average
#              log(log(n)). Thus, each query runs in just over O(n).
#

import math
import itertools


def prime_factors(n):
    """Returns a list of the prime factors of n

    :param n: integer to factor into primes
    :return: list of prime factors of n
    """
    factors = []
    f = 2  # current factor to check
    while n > 1:
        if f > math.floor(pow(n, 0.5)):  # no factors above sqrt(n) besides n
            f = n
        if n % f == 0:
            #  insert only one copy of each factor
            if len(factors) == 0 or factors[-1] != f:
                factors.append(f)
            n //= f  # integer division to divide the factor from n
        else:
            f += 1   # check the next possible factor
    return factors   # n has at most log(n)/log(log(n)) distinct primes (internet)


def inti_sum(n, a, b):
    """Sums all numbers co-prime to n between a and b

    :param n: number to compute inti_sum of
    :param a: lower bound of range
    :param b: upper bound of range
    :return: sum of numbers i co-prime to n with a <= i <= b
    :bigO: (b - a) * log(n)/log(log(n))
    """
    assert(1 <= a <= b <= n <= 1012)  # restrictions in problem statement
    factors = prime_factors(n)
    total = 0
    for num in range(a, b + 1):  # check each number in range
        for factor in factors:
            if num % factor == 0:  # i is not co-prime to n
                break
        else:  # all factors have been checked; num is co-prime to n
            total += num
    return total % 1000000007  # modulo not necessary since largest sum smaller than 1000000007


q = int(input("Please enter the number of queries to be computed: "))
queries = []  # list to store lists of arguments [N A B]

# read and extract each query into a list of arguments
for _ in itertools.repeat(None, q):  # do not need the iterator variable
    query = [int(arg) for arg in input("Enter arguments N A B: ").split()]
    queries.append(query)

# calculate and print the inti_sum for each set of arguments
for query in queries:
    print(inti_sum(query[0], query[1], query[2]))
