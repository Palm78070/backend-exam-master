"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 5

[Example 2]
input = []
output = list can not blank
"""

class Solution:

    def find_max_index(self, numbers: list) -> int | str:
        if not numbers:
            return "list can not blank"
        index = 0
        max_num = numbers[0]
        len_numbers = len(numbers)
        for i in range(1, len_numbers):
            if not isinstance(numbers[i], (int, float)):
                return "list must contain only integer or float number"
            if numbers[i] > max_num:
                max_num = numbers[i]
                index = i
        return index

# if __name__ == "__main__":
#     # list = [1, 1.1, 2, 3.33, -123.33, 1]
#     # list = [1,2,1,3,5,6,4]
#     result = Solution().find_max_index(list)
#     print(f"result: {result}")
