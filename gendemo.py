def g(n):
    print('enter g with ', n)
    i = 0
    while i < n:
        yield i
        print('after yield')
        i += 1
    print('after while')
