"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_maps = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def fn():
            queue = [""]
            for digit in digits:
                for _ in range(len(queue)):
                    temp = queue.pop(0)
                    for i in phone_maps[digit]:
                        queue.append(temp + i)
            return queue

        return fn() if len(digits) > 0 else []


digits = "23"
ret = Solution().letterCombinations(digits=digits)
print(ret)
