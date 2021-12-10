# LeetCode - 1. Two Sum
# https://leetcode.com/problems/two-sum/


# Brute Force 풀이법
# 시간복잡도 O(N^2) runtime : 4064ms

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    ans.append(i)
                    ans.append(j)
                    return ans

# enumerate 활용 풀이법
# 시간복잡도 O(N^2) runtime : 632ms

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,value in enumerate(nums):
            tmp = target - value
            
            if tmp in nums[i+1:]:
                return [nums.index(value), nums[i+1:].index(tmp) + (i+1)]

# 종결 풀이법
# 시간복잡도 O(N) -> enumerate runtime : 43ms

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i,n in enumerate(nums):
            tmp = target-n
            if tmp not in dic:
                dic[n] = i
            else:
                return [dic[tmp],i]