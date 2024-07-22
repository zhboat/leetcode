"""

给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

 
"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9 and i == 0:
                digits[i] = 0
                if i == 0:
                    digits = [1] + digits
            else:
                digits[i] += 1
                break

        print(digits)
        return digits


digits = [1, 2, 3]
result = Solution().plusOne(digits)
print(result)
