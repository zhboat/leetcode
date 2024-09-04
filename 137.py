"""

给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。

你必须设计并实现线性时间复杂度的算法且使用常数级空间来解决此问题。

"""


from typing import List
from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 不符合空间复杂度
        counter = Counter(nums)
        for k, v in counter.items():
            if v == 1:
                return k

nums = [0,1,0,1,0,1,99]
ret = Solution().singleNumber(nums)
print(ret)