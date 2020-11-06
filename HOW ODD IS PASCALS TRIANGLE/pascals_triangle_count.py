# import numpy as np
# import math
from collections import OrderedDict

def length(list) -> float:
    leng = 0
    for item in list:
        leng += 1
    return leng

def nthRowPascalsTriangle(n, upperLimit=1000000000):
    term = 1
    for i in range(n + 1):
        if term <= upperLimit:
            yield (round(term), n)
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
    # dictionary = OrderedDict()
    dictionary = getCountsUntilRow(rowNum, threshhold)
    orderedDictionary = OrderedDict(dictionary)

    with open(fileName,'w') as file:
        for num in orderedDictionary:
            if length(orderedDictionary.get(num)) >= threshhold and round(num) > 1:
                file.write("{:>15} :\t\t".format(round(num)))
                file.write("{:>4}\t\t".format(len(orderedDictionary[num])))
                file.write("{:30}\n".format(str(orderedDictionary[num])))


# writeToFile("HOW ODD IS PASCALS TRIANGLE/count_upto_25000.txt",25000, 3)
gen = nthRowPascalsTriangle(3003)

for num in gen:
    print(num)

