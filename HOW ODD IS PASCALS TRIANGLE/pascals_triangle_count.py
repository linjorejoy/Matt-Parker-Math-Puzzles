# import numpy as np
# import math
from collections import OrderedDict

def length(list) -> float:
    leng = 0
    for item in list:
        leng += 1
    return leng

def nthRowPascalsTriangle(n, upperLimit=1000000):
    term = 1
    for i in range(n + 1):
        if term <= upperLimit:
            yield (term, n)
        term = (term / (i + 1))*(n - i)


def getCountsUntilRow(rowNum, threshhold):
    countOfnums = OrderedDict()
    for i in range(rowNum):
        gen = nthRowPascalsTriangle(i)
        for num, row in gen:
            if num in countOfnums and num != 1:
                countOfnums[num].append(row)
            else:
                countOfnums[num] = [row]
        # Delete numbers < current row with count < threshhold
        for number in range(i):
            if i in countOfnums:
                if length(countOfnums.get(i)) < threshhold:
                    countOfnums.pop(i)
    
    return countOfnums


def writeToFile(fileName, rowNum, threshhold):
    dictionary = OrderedDict()
    dictionary = getCountsUntilRow(rowNum, threshhold)

    with open(fileName,'w') as file:
        for num in dictionary:
            if length(dictionary.get(num)) >= threshhold and round(num) > 1:
                file.write("{:>20} : ".format(round(num)))

                file.write(str(dictionary[num]))
                file.write("\n")


writeToFile("HOW ODD IS PASCALS TRIANGLE/count_upto_1500.txt",1500, 3)
