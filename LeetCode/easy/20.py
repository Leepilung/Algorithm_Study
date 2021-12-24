# LeetCdoe 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

# Runtime : 28ms(85.91%)
# Memory Usage : 14.4MB(36.29%)

class Solution:
    def isValid(self, s: str) -> bool:
        check = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                    check.append(i)
            else:
                if len(check) == 0 and (i == ')' or i == '}' or i == ']'):
                    return False
                if i == ')' and check[-1] == '(':
                    check.pop()
                    continue
                if i == '}' and check[-1] == '{':
                    check.pop()
                    continue
                if i == ']' and check[-1] == '[':
                    check.pop()
                    continue
                else:   return False

        if len(check) == 0:
            return True
        else : return False