# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left:int, right:int) ->str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
            # left를 만족시켰으니까 +1부터 유효, right는 인덱스까지 부분문자를 잡아야 right-1까지 출력
            
        if len(s) < 2 or s == s[::-1]:
            return s
        
        result = ''
        for i in range(len(s) -1):
            result = max(result, expand(i,i+1),expand(i,i+2),key=len)
                                  # 짝수 포인터,  홀수 포인터
        return result   
