# LeetCode 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/


# 투포인터 활용 
# 시간 복잡도 O(N^2) 68ms
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0   # 물의 높이를 0으로 설정
        left, right = 0, len(height) -1    # 탐색할 좌,우 포인터의 좌표
        left_max, right_max = 0, 0      # 높이값을 담을 변수 초기화

        while left<right:   # 왼쪽 포인터가 오른쪽 포인터에 닿는순간 종료
            if height[left] < height[right]:    # 왼쪽 포인터의 높이가 오른쪽 포인터의 높이보다 작을 경우
                if left_max < height[left]:     # 동시에 왼쪽 높이의 최고값이 현재 포인터의 높이보다 작을 경우
                    left_max = height[left]     # 왼쪽 높이값을 현재 포인터 값으로 갱신
                else:
                    water += left_max - height[left]    #  현재 좌측 포인터의 높이가 높이값보다 작으면 그만큼 물이 고여있음을 의미하므로 물에 값만큼 가산
                left += 1   # 조건문 다돌고 왼쪽 탐색을 진행해야 하므로 왼쪽 인덱스에 +1 가산
            else:   # 반대로 왼쪽 포인터의 높이가 오른쪽 포인터보다 클 경우
                if right_max < height[right]:   # 오른쪽 높이의 최고값이 현재 우측 포인터의 높이보다 작을 경우
                    right_max = height[right]   # 오른쪽 높이의 최고값을 현재 우측 포인터의 높이값으로 갱신
                else:
                    water += right_max - height[right]  # 현재 포인터의 높이가 최고높이값보다 작으면 그만큼 물이 담겨있음을 의미, 물높이 가산
                right -= 1  # 우측 인덱스 이동

        return water    # 탐색 종료 반환.
