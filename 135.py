"""
n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。

你需要按照以下要求，给这些孩子分发糖果：

每个孩子至少分配到 1 个糖果。
相邻两个孩子评分更高的孩子会获得更多的糖果。
请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目 。
"""

from typing import List


### 抄作业了，不算过，需要理解贪心算法
class Solution:
    def candy(self, ratings: List[int]) -> int:
        len_ratings = len(ratings)
        left = [1] * len_ratings
        right = left[:]
        print(left, right)
        for i in range(1, len_ratings):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
        count = left[-1]
        for i in range(len_ratings - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1
            count += max(left[i], right[i])
        return count


candy = [1, 2, 2]
ret = Solution().candy(candy)
print(ret)
