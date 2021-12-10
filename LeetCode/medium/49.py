# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/

from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            key = tuple(sorted(i))  # 키값 튜플로 저장
            dic[key] = dic.get(key, []) + [i]   # 벨류값 원형(Anagram)으로 저장

        return dic.values()