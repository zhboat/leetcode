"""
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

 

说明：

为什么返回数值是整数，但输出的答案是数组呢？

请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
"""

from typing import List
from collections import defaultdict


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        left = 2

        for right in range(2, len(nums)):
            if nums[left - 2] != nums[right]:
                nums[left] = nums[right]
                left += 1
        return left


nums = [1, 2 ,3]
ret = Solution().removeDuplicates(nums)
print(ret)
