def reverses(array, a, b):
    while a < b:
        array[a], array[b] = array[b], array[a]
        a += 1
        b -= 1

def rotate(nums, k):
    n = len(nums)
    k = k % n
    reverses(nums, 0, n-k-1)
    reverses(nums, n-k, n-1)
    reverses(nums, 0, n-1)
    return nums


if __name__ == '__main__':
    nums = [i for i in range(1, 8)]
    k = 3
    print(rotate(nums, k))