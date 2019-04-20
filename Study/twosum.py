# -*- coding: utf-8 -*-
# @File  : twosum.py
# @Author: 郭迎辉
# @Time  : 2018/12/6/00611:24
# @Desc  :
class Solution(object):
    def twoSum(self, nums, target):
        first = 0
        second = 0
        for i in nums:
            for j in nums:
                if i + j == target:
                    first = i
                    second = j
        return second, first
if __name__ == "__main__":
    solution = Solution()
    j ,i = solution.twoSum([1, 3, 4, 5, 13], 16)
    print(j, i)