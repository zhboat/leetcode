"""
给你一个正整数数组 nums 和一个整数 k 。

一次操作中，你可以将数组的最后一个元素删除，将该元素添加到一个集合中。

请你返回收集元素 1, 2, ..., k 需要的 最少操作次数 。

"""

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums_len, nums_set = len(nums), set()
        for i in range(nums_len - 1, -1, -1):
            if nums[i] <= k:
                nums_set.add(nums[i])
                if len(nums_set) == k:
                    return nums_len - i


nums = [3, 3, 5, 1, 2]
k = 3
result = Solution().minOperations(nums, k)
print(result)
