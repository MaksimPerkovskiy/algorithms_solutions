"""
Solution for generating primes task.
Task: to write a function that generates prime numbers up to a user-specified.
"""
from math import sqrt
import sys
from functools import wraps
from typing import ParamSpec, TypeVar, Callable


RT = TypeVar('RT')
P = ParamSpec('P')


class Solution:
    def generate_primes(self, max_value: int) -> list[int]:
        numbers_lst = self._initialize_list_of_bools(max_value=max_value)
        numbers_lst = self._cross_out_multiples(numbers_lst=numbers_lst, max_value=max_value)
        return self._load_result(numbers_lst=numbers_lst)

    def _initialize_list_of_bools(self, max_value: int) -> list[bool]:
        numbers_lst = [True for _ in range(max_value+1)]
        numbers_lst[0] = numbers_lst[1] = False
        return numbers_lst

    def _cross_out_multiples(self, numbers_lst: list[bool], max_value: int) -> list[bool]:
        limit = sqrt(max_value)
        i = 2
        while i <= limit:
            if numbers_lst[i]:
                j = i 
                while j * i < max_value + 1:
                    numbers_lst[i * j] = False
                    j += 1
            i += 1
        return numbers_lst

    def _load_result(self, numbers_lst: list[bool]) -> list[int]:
        return [index for index, value in enumerate(numbers_lst) if value]    


def test(func: Callable[P, RT]) -> Callable[P, RT]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> RT:
        res = func(*args, **kwargs)
        print(f"Test {func.__name__} passed.")
        return res
    return wrapper


class TestGeneratePrimes:
    @test
    def test_for_13(self) -> None:
        max_value = 13
        res = Solution().generate_primes(max_value=max_value)
        assert res == [2, 3, 5, 7, 11, 13]
    
    @test
    def test_for_15(self) -> None:
        max_value = 15
        res = Solution().generate_primes(max_value=max_value)
        assert res == [2, 3, 5, 7, 11, 13]
    
    @test
    def test_for_1(self) -> None:
        max_value = 1
        res = Solution().generate_primes(max_value=max_value)
        assert res == []
    
    @test
    def test_for_2(self) -> None:
        max_value = 2
        res = Solution().generate_primes(max_value=max_value)
        assert res == [2]
    
    @test
    def test_for_3(self) -> None:
        max_value = 3
        res = Solution().generate_primes(max_value=max_value)
        assert res == [2, 3]


class TestExhaustive:
    @test
    def test_verify_prime_list(self) -> None:
        for i in range(2, 501):
            self._verify_primes(Solution().generate_primes(max_value=i))
    
    def _verify_primes(self, primes_list: list[int]) -> None:
        for number in primes_list:
            self._verify_prime(number=number)
    
    def _verify_prime(self, number: int) -> None:
        factor = 2
        while factor < number:
            assert number % factor != 0
            factor += 1


def run_test_case(test_case: object) -> None:
    for method_name in dir(test_case):
        if method_name[:4] == "test":
            method = getattr(test_case, method_name)
            method()


def run_tests():
    run_test_case(test_case=TestGeneratePrimes())
    run_test_case(test_case=TestExhaustive())


def run_script():
    res = Solution().generate_primes(15)
    print(f"Result: {res}")


if __name__ == "__main__":
    if "--test" in sys.argv:
        run_tests()
    else:
        run_script()
