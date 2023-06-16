"""Написать функцию, кoторая принимает два числа в качестве аргумента и посчитает наименьшее общее кратное
 для этих чисел"""
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
print(gcd(12, 18))

def lcm(a, b):
    return a * b // gcd(a, b)
print(lcm(12, 18))