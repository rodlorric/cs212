import timeit
# --------------
# User Instructions
#
# Write a function, inverse, which takes as input a monotonically
# increasing (always increasing) function that is defined on the 
# non-negative numbers. The runtime of your program should be 
# proportional to the LOGARITHM of the input. You may want to 
# do some research into binary search and Newton's method to 
# help you out.
#
# This function should return another function which computes the
# inverse of the input function. 
#
# Your inverse function should also take an optional parameter, 
# delta, as input so that the computed value of the inverse will
# be within delta of the true value.

# -------------
# Grading Notes
#
# Your function will be called with three test cases. The 
# input numbers will be large enough that your submission
# will only terminate in the allotted time if it is 
# efficient enough. 

def slow_inverse(f, delta=1/128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def f_1(y):
        x = 0
        while f(x) < y:
            x += delta
        # Now x is too big, x-delta is too small; pick the closest to y
        return x if (f(x)-y < y-f(x-delta)) else x-delta
    return f_1 

def inverse(f, delta = 1/128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def f_1(y):
        start = x = 0
        end = y/2
        while f(x) < y:
            x = (end - start) / 2.0
            end = x
            start += delta
            x = start
        return x if (f(x)-y < y-f(x-delta)) else x-delta
    return f_1

def faster_inverse(f, delta=1/128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def f_1(y):
        lo, hi = find_bounds(f, y)
        return binary_search(f, y, lo, hi, delta)
    return f_1

def find_bounds(f, y):
    "Find values lo, hi such that f(lo) <= y <= f(hi)"
    # Keep doubling x until f(x) >= y; that's hi;
    # and lo will be either the previous or 0.
    x = 1.
    while f(x) < y:
        x = x * 2.
    lo = 0 if (x == 1) else x/2.
    return lo, x

def binary_search(f, y, lo, hi, delta):
    "Given f(lo) <= y <= f(hi), return x such that f(x) is within delta of y."
    # Continually split the region in half
    while lo <= hi:
        x = (lo + hi) / 2.
        if f(x) < y:
            lo = x + delta
        elif f(x) > y:
            hi = x - delta
        else: 
            return x
    return hi if (f(hi) - y < y - f(lo)) else lo

def square(x): return x*x
sqrt = inverse(square)
slow_sqrt = slow_inverse(square)
fast_sqrt = faster_inverse(square)
print sqrt(1000000000)
print slow_sqrt(1000000000)
print fast_sqrt(1000000000)