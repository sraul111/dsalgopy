# a program for Memoized version of nth Fibonacci number

# function to calculate nth Fibonacci number


def fib(n, lookup):

    # base case
    if n <= 1:
        lookup[n] = n

    # if the value is not calculated previously then calculate it
    if lookup[n] is None:
        lookup[n] = fib(n-1, lookup) + fib(n-2, lookup)
        #print(lookup[n])

    # return the value corresponding to that value of n
    return lookup[n]
# end of function

# Driver program to test the above function


def main():
    n = 34
    # Declaration of lookup table
    # Handles till n = 100
    lookup = [None] * 101
    print ("Fibonacci Number is ", fib(n, lookup))


if __name__ == "__main__":
    main()

