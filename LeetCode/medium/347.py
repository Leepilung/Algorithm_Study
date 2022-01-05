# LeetCode 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/

# k번 이상 등장하는 요소를 추출하라.

# Runtime : 206ms (5.17%)
# Memory Usage : 18.6MB (85.00%)
# 딕셔너리 정렬 개념 정리 사이트 : https://kkamikoon.tistory.com/138

import collections
import operator
from typing import Collection, List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else: dic[i] += 1
        
        sdict = sorted(dic.items(), key=operator.itemgetter(1),reverse=True)
        ans = []
        for i in range(k):
            ans.append(sdict[i][0])
        
        return ans

# Counter를 이용한 음수 순 추출 방법



# Pitonic한 방법
# 상위 k번만큼의 요소를 추출하기 위해, 힙에 넣고 빼는 작업을 자동으로 하는 함수가 있다.
# Counter에는 most_common()이라는 빈도 수가 높은 순서대로 아이템을 추출하는 기능이 있다.

nums = [1,1,1,2,2,3]
k = 2

collections.Counter(nums).most_common(k)

# 실행 시 [(1,3),(2,2)] 출력

list(zip(*collections.Counter(nums).most_common(k)))[0]
# >> 실행시 (1,2) 출력.

# Runtime : 151ms (14.88%)
# Memory Usage : 18.6MB (95.55%)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]
