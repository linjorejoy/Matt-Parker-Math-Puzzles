import math

def getHalfDivisors(number):
    divisors = []
    for i in range(1, math.floor(math.sqrt(number)) + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors


def isPseudoVampireSet(num1, num2):
    if(sorted(str(num1) + str(num2)) == sorted(str(num1*num2))):
        return True
    return False

def isVampireSet(num1, num2):
    if(sorted(str(num1) + str(num2)) == sorted(str(num1*num2)) and len(str(int(num1))) == len(str(int(num2))) ):
        return True
    return False

def printPseudoVampireNumbers(fromNumber, uptoNumber):
    for i in range(fromNumber, uptoNumber + 1):
        for j in getHalfDivisors(i):
            if isPseudoVampireSet(j, i/j):
                print("{:>5.0f} x {:>5.0f} = {:>10}".format(j, i/j, i))
                pass
            pass

def printVampireNumbers(fromNumber, uptoNumber):
    for i in range(fromNumber, uptoNumber + 1):
        for j in getHalfDivisors(i):
            if isVampireSet(j, i/j):
                print("{:>5.0f} X {:>5.0f} = {:>10}".format(j, i/j, i))
                pass
            pass


printPseudoVampireNumbers(1,1000000)
print("."*10)
# printVampireNumbers(1,1000000)