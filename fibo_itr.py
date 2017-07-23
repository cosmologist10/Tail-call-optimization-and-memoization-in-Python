import time


def fibonacci_i(n):
    """ Fibonacci - Iterator version """

    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b

    return b


if __name__ == "__main__":
    import sys

    n = int(sys.argv[1])
    start_time = time.time()

    print 'Fibonacci number for', n, '=>'
    print fibonacci_i(n)

    print("--- %s seconds ---" % (time.time() - start_time))
