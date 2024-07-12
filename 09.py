"""给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数
是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

例如，121 是回文，而 123 不是。
 """

from typing import List


class Solution:
    def split_int(self, num: int) -> List[int]:
        num_lst = []
        while num:
            if num == 0:
                break
            num_lst.append(num % 10)
            num = int(num / 10)
        return num_lst

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            num_list = self.split_int(x)
            for i, j in zip(num_list, num_list[::-1]):
                if i != j:
                    return False
        return True


x = 0
ret = Solution().isPalindrome(x)
print(ret)


# simple way:
x = 12322
print(True if str(x) == str(x)[::-1] else False)