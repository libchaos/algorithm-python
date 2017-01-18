def radixSort(a, n):
    rl = [[] for _ in xrange(10)] 

    for i in xrange(n):
        t = 10 ** i
        for j in xrange(len(a)):
            rl[a[j] / t % 10].append(a[j])
        k = 0

        for r in rl:
            for x in r:
                a[k] = x
                x += 1
            del r[:]


if __name__ == '__main__':
    from random import shuffle
    data = range(10)
    shuffle(data)

    print data
    radixSort(data, 5)
    print data