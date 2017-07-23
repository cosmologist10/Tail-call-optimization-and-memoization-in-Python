import time


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
    """ Fibonacci sequence using recursion """

    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

if __name__ == "__main__":
    import sys

    n = int(sys.argv[1])

    start_time = time.time()

    print 'Fibonacci number for', n, '=>'
    print fibonacci(n)

    print("--- %s seconds ---" % (time.time() - start_time))
