# LeetCode - 125. Valid Palindrome
# Link : https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = []
        for i in s.lower():
            if i.isalnum():
                string.append(i)
        while len(string) > 1:
            if string.pop(0) != string.pop():
                return False
        return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = ''.join(filter(str.isalnum, s))
        return i.lower() == i.lower()[::-1]