import math



def divisors(num):
    divisors = []
    for i in range(1, math.floor(math.sqrt(num)) + 1):
        if num % i == 0:
            divisors.append(i)
            if i != num/i:
                divisors.append(num/i)
    return sorted(divisors)




def cgfh(cg_plus_fh):
    for cg in range(1, int(cg_plus_fh)):
        fh = cg_plus_fh - cg
        for c in divisors(cg):
            for f in divisors(fh):
                yield ((c), (cg//c), (f), (fh//f))

def frac(num):
    return num - math.floor(num)


for r in range(1, 99, 2):
    cg_plus_fh = (101**2 - r**2)/4
    for (c, g, f, h) in cgfh(cg_plus_fh):
        a = (101*c*g + c*g*r) / (2 * cg_plus_fh)
        b = (c*h*(r + 101)) / (2 * cg_plus_fh)
        d = (f*g*(r + 101)) / (2 * cg_plus_fh)
        e = (f*h*(r + 101)) / (2 * cg_plus_fh)
        i = (101 - r) / 2

        if (
            frac(a) == 0 and frac(b) == 0 and frac(d) == 0 and frac(e) == 0
            and 10 <= a < 100 and 10 <= b < 100 and 10 <= c < 100
            and 10 <= d < 100 and 10 <= e < 100 and 10 <= f < 100
            and 10 <= g < 100 and 10 <= h < 100 and 10 <= i < 100
        ):
            print("{{%d, %d, %d}, {%d, %d, %d}, {%d, %d, %d}}" % (a,b,c,d,e,f,g,h,i))