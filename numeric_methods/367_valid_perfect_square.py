def is_perfect_square(number: int) -> bool:
    if number == 1:
        return True
    start = 0
    end = number
    while (end - start) != 1:
        mid = (end + start) // 2
        to_check = mid * mid
        if to_check > number:
            end = mid
        elif to_check < number:
            start = mid
        else:
            return True

    return False


print(is_perfect_square(2374681))
