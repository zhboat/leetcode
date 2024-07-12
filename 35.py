"""给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # TODO: optimized to O(log n)
        count = 0
        while nums:
            if count == len(nums) or target <= nums[count]:
                break
            if target == nums[count] or nums[count - 1] <= target <= nums[count]:
                break
            count += 1
        return count


nums = [1, 3, 5, 6]
target = 7
print(Solution().searchInsert(nums=nums, target=target))
