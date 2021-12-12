# LeetCode 561. Array Partition I
# https://leetcode.com/problems/array-partition-i/

# 개 오지는 풀이
from typing import List
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        return sum(sorted(nums)[::2])

# 일반적인 풀이
class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        ans = 0
        for i in range(0, len(nums)-1, 2):
            ans += nums[i]
        return ans