import math
import numpy as np


def divisors(num):
    divisors = []
    for i in range(1, math.floor(math.sqrt(num)) + 1):
        if num % i == 0:
            divisors.append(i)
            if i != num/i:
                divisors.append(num/i)
    return (divisors)


def checkMatrixIsVampire(a, b, c, d, e, f, g, h, i, order):
    N = 10**order + 1
    arr = np.array([[a,b,c],[d,e,f],[g,h,i]])
    return (np.matmul(arr,arr) == N*arr).all()

def isInt(num):
    return num == math.floor(num)

def generateVampirematrices(order):
    N = 10**order + 1
    lowerLimit = 10**(order-1)
    upperLimit = 10**order
    for a in range(lowerLimit, upperLimit ):
        for e in range(lowerLimit, upperLimit ):
            i = N - a - e
            if(i > 0):
                for c in divisors(a * i):
                    g = a * i / c
                    if(isInt(g)):
                        for d in divisors(e*g):
                            h = e * g / d
                            f = i * d / g
                            b = c * e / f
                            if(isInt(h) and isInt(f) and isInt(b)
                            and lowerLimit <= a < upperLimit
                            and lowerLimit <= b < upperLimit
                            and lowerLimit <= c < upperLimit
                            and lowerLimit <= d < upperLimit
                            and lowerLimit <= e < upperLimit
                            and lowerLimit <= f < upperLimit
                            and lowerLimit <= g < upperLimit
                            and lowerLimit <= h < upperLimit
                            and lowerLimit <= i < upperLimit
                            ):
                                yield (int(a) ,int(b) ,int(c) ,int(d) ,int(e) ,int(f) ,int(g) ,int(h) ,int(i))
                        


def checkAllValues(order):
    gen = generateVampirematrices(order)
    count = 0
    countVampire = 0
    countNotVampire = 0
    for a,b,c,d,e,f,g,h,i in gen:
        count += 1
        if checkMatrixIsVampire(a, b, c, d, e, f, g, h, i, order):
            countVampire += 1
            # print("|{} {} {}|\n|{} {} {}|\n|{} {} {}| is vampire\n".format(int(a), int(b), int(c), int(d), int(e), int(f), int(g), int(h), int(i)))
        else:
            countNotVampire += 1
            # print("|{} {} {}|\n|{} {} {}|\n|{} {} {}| is vampire\n".format(int(a), int(b), int(c), int(d), int(e), int(f), int(g), int(h), int(i)))
        if count % 10000 == 0:
            print("Total Generated : {}\nTotal Vampire : {}\nTotal Non-Vamire : {}".format(count, countVampire, countNotVampire))
            print("Approx Total Completed : {} % ->{} ".format( (a-10**(order-1))*100/(10**order-10**(order-1)),a))
    print("Total Generated : {}\nTotal Vampire : {}\nTotal Non-Vamire : {}".format(count, countVampire, countNotVampire))
    print("Approx Total Completed : {} % ->{} ".format( (a-10**(order-1))*100/(10**order-10**(order-1)),a))



checkAllValues(2)
