"""
เขียบนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""
import sys

class Solution:

    def ft_factorial(self, number: int) -> int:
        if number == 0:
            return 1
        return number * self.ft_factorial(number - 1)

    def find_tailing_zeroes(self, number: int) -> int | str:
        if number < 0:
            return "number can not be negative"
        if number > sys.maxsize:
            return "number is larger than integer max value"
        if number == 0:
            return 0
        factorial = self.ft_factorial(number)
        count = 0
        while(factorial % 10 == 0):
            count += 1
            factorial = factorial / 10
        return count

# if __name__ == "__main__":
#     number = int(input("Enter integer: "))
#     print(Solution().find_tailing_zeroes(number))
