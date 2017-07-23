import time
from tco import *


def stacktracker(f):
    """ Wrapper for call stack count """

    calls = {'count': 0}

    def wrapper(*args):
        calls['count'] += 1
        print 'Call count =>', calls['count']
        result = f(*args)
        return result

    return wrapper


@stacktracker
@with_continuations()
def fibonacci(n, a=0, b=1, self=None):
    return b if n == 0 else self(n-1, a+b, a)

if __name__ == "__main__":
    import sys

    n = int(sys.argv[1])
    start_time = time.time()

    print 'Fibonacci number for', n, '=>'
    print fibonacci(n, 0, 1)

    print("--- %s seconds ---" % (time.time() - start_time))
