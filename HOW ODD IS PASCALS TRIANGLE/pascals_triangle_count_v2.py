import math
from collections import OrderedDict


def length(list) -> float:
    leng = 0
    for item in list:
        leng += 1
    return leng

def nthRowPascalsTriangle(n, upperLimit=1e308):
    term = 1
    for i in range(math.ceil( (n + 1) / 2) ):
        if term <= upperLimit:
            yield (round(term), n)
            if i != n / 2:
                yield (round(term), n)
        else:
            return
        term = (term / (i + 1))*(n - i)



def getCountAndWriteToFile(fileName, uptoRowNum, threshhold):
    with open(fileName, 'w') as file:
        file.write("Pascals Triangle Row Upto : {} with more than or equal to {} repetitions\n\n"
        .format(uptoRowNum, threshhold))
        countOfnums = OrderedDict()
        for i in range(uptoRowNum+1):
            gen = nthRowPascalsTriangle(i)
            for num, row in gen:
                if num in countOfnums and num != 1:
                    countOfnums[num].append(row)
                elif num not in countOfnums and num != 1:
                    countOfnums[num] = [row]

            # Delete numbers < current row with count < threshhold
            # write to file if numbers < current row with count >= threshhold
            if (i-2) in countOfnums:
                if length(countOfnums.get(i-2)) < threshhold:
                    countOfnums.pop(i-2)
                elif length(countOfnums.get(i-2)) >= threshhold:
                    file.write("{:>15} :\t\t".format(round(i-2)))
                    file.write("{:>4}\t\t".format(len(countOfnums[i-2])))
                    file.write("{:30}\n".format(str(countOfnums[i-2])))
                    countOfnums.pop(i-2)
        for num in countOfnums:
                if length(countOfnums.get(num)) >= threshhold and round(num) > 1:
                    file.write("{:>15} :\t\t".format(round(num)))
                    file.write("{:>4}\t\t".format(len(countOfnums[num])))
                    file.write("{:30}\n".format(str(countOfnums[num])))
    


getCountAndWriteToFile("count_upto_100000_v2.txt",100000,4)




