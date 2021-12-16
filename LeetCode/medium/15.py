# LeetCode 15. 3Sum
# https://leetcode.com/problems/3sum/

# 세 수의 합 투포인터 활용
# 시간 복잡도 O(N^2) - 840ms

from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1  # 좌, 우 인덱스 활용
            while left < right: # 좌측이 우측 포인터와 닿으면 종료
                s = nums[i] + nums[left] + nums[right]  # s = for문의 인덱스 값 + 좌,우 포인터값 의 합
                if s < 0:       # s가 음수라는 뜻은 정렬되었을때 좌측(작은값과 더했기 때문)
                    left +=1    # 좌측 포인터 우측으로 이동
                elif s > 0:     # s가 양수일 경우는 우측(큰 값과 더했기 때문)
                    right -= 1  # 우측 포인터 좌측으로 이동
                else:           # s가 0인경우에 해당
                    ans.append((nums[i], nums[left], nums[right]))  # 정답에 해당하는 값을 배열로 ans에 추가
                    # sum이 0인 상황이고 같은값이 나올 수 있기 때문에 좌, 우 포인터값 이동시켜야함.
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1; right -= 1
                    
        return ans