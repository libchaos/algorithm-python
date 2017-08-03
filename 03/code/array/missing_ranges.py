def misssing_ranges(nums, lo, hi):
    res = []
    start = lo
    for num in nums:
        if num < start:
            continue
        if num == start:
            num += 1
            continue
        res.append(get_range(start, num-1))
        start = num + 1
    if start <= hi:
        res.append(get_range(start, hi))
    return res

def get_range(n1, n2):
    if n1 == n2:
        return str(n1)
    else:
        return str(n1) + '->' + str(n2)