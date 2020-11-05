import math



def divisors(num):
    divisors = []
    for i in range(1, math.floor(math.sqrt(num)) + 1):
        if num % i == 0:
            divisors.append(i)
            if i != num/i:
                divisors.append(num/i)
    return (divisors)


def isInt(num):
    return num == math.floor(num)

def generateVampirematrices(order):
    N = 10**order + 1
    lowerLimit = 10**(order-1)
    upperLimit = 10**order
    for a in range(10**(order - 1), 10**order ):
        for e in range(10**(order - 1), 10**order ):
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
                                yield("|%d, %d, %d|\n|%d, %d, %d|\n|%d, %d, %d|\n\n" % (a,b,c,d,e,f,g,h,i))
                        


def writeToFile(fileName, order):
    gen = generateVampirematrices(order)
    with open(fileName, 'w') as file:
        count = 0
        for line in gen:
            count += 1
            file.write(str(line))
        file.write("Total Matrices Found : " + str(count))



writeToFile("SPOOKY MATHS/vampire_matrices_2ndOrder3x3.txt", 2)