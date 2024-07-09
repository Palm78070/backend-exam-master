"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""
import sys

class Solution:
    #Rules
    # 1.Certain numerals reapeat(add together) max to 3 times
    # 2.V, L, D can not be repeated
    # 3.Only I,X,C can be used as subtractive numerals and can have 6 combinations IV, IX, XL, XC, CD, CM
    # 4.GreaterNumSmallerNum: Greater number + Smaller number ex. VI = 5 + 1
    # 5.SmallerNumGreaterNum: Smaller number + Greater number ex. IV = 5 - 1
    # 6.GreaterNumSmallerNumGreaterNum: Greater number + (Smaller number - Greater number) ex. XIV = 10 + (5 - 1)
    # 7.No roman numeral for 0

    def find_max_base(self, number: int) -> int:
        if number == 0:
            return 0
        count_base = 0
        while number > 0:
            number = number // 10
            count_base += 1
        return count_base - 1

    def convert_to_roman(self, number: int, roman_map) -> tuple:
        if number in roman_map:
            return True, roman_map[number]
        if number in range(2, 4):
            return True, "I" * number
        if number in range(6, 9):
            return True, "V" + ("I" * (number - 5))
        if number in range(20, 40):
            return True, "X" * (number // 10)
        if number in range(60, 90):
            return True, "L" + ("X" * ((number - 50) // 10))
        if number in range(200, 400):
            return True, "C" * (number // 100)
        if number in range(600, 900):
            return True, "D" + ("C" * ((number - 500) // 100))
        if number > 1000:
            if number // 1000 > 10:
                return False, f"{number // 1000}M"
            return True, "M" * (number // 1000)
        return False, ""

    def number_to_roman(self, number: int) -> str:
        if number > sys.maxsize:
            return "number exceed max size of int"
        if number < 0:
            return "number can not less than 0"
        if number == 0:
            return "No roman numeral for 0"
        #I=1, V=5, X=10, L=50, C=100, D=500, M=1000

        #roman_map
        roman_map = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
            4: "IV",
            9: "IX",
            40: "XL",
            90: "XC",
            400: "CD",
            900: "CM"
        }

        max_base = self.find_max_base(number)

        res = ""
        # for current_base in range(0, max_base + 1):
        #     # print(f"{(int(number % 10)) * (10 ** current_base)}")
        #     _, roman_num = self.convert_to_roman(int(number % 10) * (10 ** current_base), roman_map)
        #     res = roman_num + res
        #     number /= 10

        for current_base in range(max_base, -1, -1):
            # Calculate the value of the current digit
            digit_value = (number // (10 ** current_base)) * (10 ** current_base)
            number %= 10 ** current_base
            _, roman_num = self.convert_to_roman(digit_value, roman_map)
            res += roman_num

        return res

# if __name__ == '__main__':
#     number = int(input("Enter number: "))
#     print(Solution().number_to_roman(number))
