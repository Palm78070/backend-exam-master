"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def find_max_base10(self, number: int) -> int:
        if number == 0:
            return 0
        count_base = 0
        while number > 0:
            number = number // 10
            count_base += 1
        return count_base - 1

    def proceed(self, number, current_base):
        return number / 10, current_base + 1

    def number_to_thai(self, number: int) -> str:
        if number < 0:
            return "number can not less than 0"
        if number > 10_000_000:
            return "number can not more than 10_000_000"

        base = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน"]
        base10 = ["", "สิบ", "ยี่สิบ"]
        digit = ["ศูนย์", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า", "สิบ"]

        max_base = self.find_max_base10(number)
        if max_base == 7:
            return "สิบล้าน"
        if max_base == 0:
            return digit[number]

        current_base = 0
        res = ""
        while current_base <= max_base:
            current_digit = int(number % 10)
            if current_digit == 0:
                number, current_base = self.proceed(number, current_base)
                continue
            if current_base == 0 and current_digit == 1:
                res += "เอ็ด"
            elif current_base == 1 and current_digit <= 2:
                res = base10[current_digit] + res
            else:
                res = digit[current_digit] + base[current_base] + res
            number, current_base = self.proceed(number, current_base)

        return res

# if __name__ == '__main__':
#     number = int(input("Enter number: "))
#     print(Solution().number_to_thai(number))
