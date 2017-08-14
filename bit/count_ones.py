def count_ones(n):
    if n < 0:
        return
    counter = 0
    while n:
        counter += n & int('1', 2)
        n >>= int('1', 2)
    return counter


