# LeetCode 66. Plus One
# https://leetcode.com/problems/plus-one/
# 12/18 테스트 문제
# 별도의 정리가 필요없는 문제.

# 시간복잡도 O(N), Runtime : 24ms(2.42%), Memory Usage : 14.3 MB(85.82%)
# 문자열 합치고 숫자 가산 -> map 활용해서 바꾸는걸로 풀이
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tmp = ''
        for i in digits:
            tmp += str(i)

        tmp = list(map(int, str((int(tmp) +1))))

        return tmp