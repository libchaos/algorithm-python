import random

def josepheus(int_list, skip):
    skip -= 1
    idx = 0
    while len(int_list) > 0 :
        idx = (skip + idx) % len(int_list)
        print(int_list.pop(idx))

a = [random.randint(1, 9) for i in range(10)]
print(a)
josepheus(a, 3)