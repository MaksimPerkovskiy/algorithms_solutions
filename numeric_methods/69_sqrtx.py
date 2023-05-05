# Solution for https://leetcode.com/problems/sqrtx/


def mySqrt(x: int) -> int:
    if x in (0, 1):
        return x
    low = 0
    high = x
    while (high - low) != 1:
        mid = (high + low) // 2
        to_check = mid * mid
        if to_check > x:
            high = mid
        elif to_check < x:
            low = mid
        else:
            return mid
    return low


print(mySqrt(10002))
