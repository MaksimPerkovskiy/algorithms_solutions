# Solution for https://leetcode.com/problems/powx-n/

def myPow(x: float, n: int) -> float:
    if n < 0:
        n = abs(n)
    elif n == 0:
        return 1

    result = 1
    while n > 0:
        current_bit = n % 2
        if current_bit == 1:
            result *= x
            x *= x
        else:
            x *= x
        n = int(n / 2)    

    if n < 0:
        result = 1 / result

    return result


print(myPow(2, 1))
