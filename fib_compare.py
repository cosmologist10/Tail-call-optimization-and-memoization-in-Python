from tco import *


def stacktracker(f):
    calls = {'count': 0}

    def wrapper(*args):
        calls['count'] += 1
        print 'Call count =>', calls['count']
        result = f(*args)
        return result

    return wrapper


@stacktracker
def fibonacci(n):
    """ Regular fibonacci function illustrating call stack count """

    # Increment call stack count
    if n <= 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_i(n):
    """ Fibonacci - Iterator version """

    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b

    return b


@stacktracker
def fibonacci_tre(n, a=0, b=1):
    """ Fibonacci with tail recursion elimination """

    if n == 0:
        return b
    else:
        return fibonacci_tre(n-1, b, a+b)


@stacktracker
@with_continuations()
def fibonacci_tco(n, a=0, b=1, self=None):
    return b if n == 0 else self(n-1, b, a+b)

if __name__ == "__main__":
    import sys

    n = int(sys.argv[1])
    print 'Executing normal fibonacci for', n
    print fibonacci(n)
    print 'Executing fibonacci-tre for', n
    print fibonacci_tre(n)
    print 'Executing fibonacci-iterator for', n
    print fibonacci_i(n)
    print 'Executing fibonacci-tco for', n
    print fibonacci_tco(n)
