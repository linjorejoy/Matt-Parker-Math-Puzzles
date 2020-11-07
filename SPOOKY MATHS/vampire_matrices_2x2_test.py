
import math
import numpy as np

# a = np.array([[1,2],[2,3]])
# b = np.array([[101,202],[202,303]])

# print(a**2)
# print((b == 101*a).all())
# print(np.matmul(a,a))



def getDivisors(number):
    divisors = []
    for i in range(1, math.floor(math.sqrt(number)) + 1):
        if number % i == 0:
            divisors.append(i)
            if i != number/i:
                divisors.append(number/i)
    return divisors



def checkMatrixIsVampire(a, b, c, d, order):
    N = 10**order + 1
    arr = np.array([[a,b],[c,d]])
    return (np.matmul(arr,arr) == N*arr).all()



def getVampireMatrices(order):
    for a in range(10**(order-1), 10**order):
        d = 10**order + 1 - a
        if d < 10**order:
            bc = (10**order + 1)*a - a*a
            for b in getDivisors(bc):
                if b < 10**order and bc/ b < 10**order and 10**(order-1) < d < 10**(order) :
                    yield (int(a), int(b), int(bc/b), int(d))


def checkAllValues(order):
    gen = getVampireMatrices(order)
    count = 0
    countVampire = 0
    countNotVampire = 0
    for a,b,c,d in gen:
        count += 1
        if checkMatrixIsVampire(a,b,c,d, order):
            countVampire += 1
            print("|{} {}|\n|{} {}| is vampire\n".format(a,b,c,d))
        else:
            countNotVampire += 1
            print("|{} {}|\n|{} {}| is not vampire\n".format(a,b,c,d))
    print("Total Generated : {}\nTotal Vampire : {}\nTotal Non-Vamire : {}".format(count, countVampire, countNotVampire))


checkAllValues(3)
