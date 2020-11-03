
import math


def getDivisors(number):
    divisors = []
    for i in range(1, math.floor(math.sqrt(number)) + 1):
        if number % i == 0:
            divisors.append(i)
            if i != number/i:
                divisors.append(number/i)
    return divisors



def getVampireMatrices(order):
    for a in range(10**order):
        d = 10**order + 1 - a
        if d < 10**order:
            bc = (10**order + 1)*a - a*a
            for b in getDivisors(bc):
                if b < 10**order and bc/ b < 10**order:
                    print("| {:^3} {:^3} || {:^3} {:^3} |".format(int(a), int(b), int(bc/b), int(d)))
                    # print(" ")
                    pass


getVampireMatrices(2)
