"""

给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，它们分别含有 n 和 m 个元素。请你计算以下两个数值：

answer1：使得 nums1[i] 在 nums2 中出现的下标 i 的数量。
answer2：使得 nums2[i] 在 nums1 中出现的下标 i 的数量。
返回 [answer1, answer2]。

 
"""

from typing import List
from itertools import zip_longest


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        fn = lambda x, y: sum(i in x for i in y)
        return [fn(set(nums2), nums1), fn(set(nums1), nums2)]

        # simple case:
        ret = [0, 0]
        for i, j in zip_longest(nums1, nums2):
            if i in nums2:
                ret[0] += 1
            if j in nums1:
                ret[1] += 1
        return ret


nums1 = [2, 3, 2]
nums2 = [1, 2]
ret = Solution().findIntersectionValues(nums1, nums2)
print(ret)
