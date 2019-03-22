# Uses python3
def calc_fib(n):
    """
    #   recursive implementation -> slow
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)
    """

    #   Fast algorithm
    if (n <= 1):
        return n

    fib_0 = 0
    fib_1 = 1
    for i in range(1,n):
        fib_1, fib_0 = fib_0 + fib_1, fib_1
    return fib_1
 
n = int(input())
print(calc_fib(n))
