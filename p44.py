import math


def generate_pentagonal(i):
    return i*(3*i-1)/2

def is_pentagonal(i):
    res = (1 + math.sqrt(1+12*i*2)) / 6
    if res > 0 and res.is_integer():
        return True
    return False


if __name__ == '__main__':
    penta_nums = []
    for i in range(1,10000):
        penta_nums.append(generate_pentagonal(i))

    i_index = 0
    for i in penta_nums:
        i_index = i_index + 1
        for j in penta_nums[i_index:]:
            if is_pentagonal(i + j) and is_pentagonal(j - i):
                print(i,j)
                print(j - i)

