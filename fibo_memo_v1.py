import time



def fib(n, _fib_cache={}):
    """ Implementation using Memoization """

    if n in _fib_cache:
        print '\t=>from cache<=', n
        return _fib_cache[n]
    else:
        _fib_cache[n] = n if n < 2 else fib(n-1) + fib(n-2)
        return _fib_cache[n]

if __name__ == "__main__":
    import sys

    n = int(sys.argv[1])
    start_time = time.time()

    print 'Fibonacci number for', n, '=>'
    print fib(n)

    print("--- %s seconds ---" % (time.time() - start_time))
