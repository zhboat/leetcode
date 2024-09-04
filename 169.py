"""
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。
"""

from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        for i in nums:
            counter[i] += 1
            if counter[i] > len(nums) // 2:
                return i


nums = [2, 2, 1, 1, 1, 2, 2]
ret = Solution().majorityElement(nums)
print(ret)
