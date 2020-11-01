import numpy as np
from itertools import permutations 


def possible(ref_array, array, len, flags):
    isPossible = True
    for i in range(len):
        flag = 0
        for j in range(len):
            if ref_array[j] == array[(i+j)%len]:
                flag += 1

            if flag == flags:
                return False
    return isPossible




def main(n, flags):
    global ref_array
    ref_array = np.arange(n) + 1
    count = 0
    for arr in permutations(np.arange(n)+1):
        # print(arr)
        if possible(ref_array, arr, n, flags):
            count += 1
            print(arr)

    print("Total possibilities with {} flags is {}".format(flags, count))


ref_array = []


main(7,2)
