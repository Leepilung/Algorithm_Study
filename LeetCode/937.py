# LeetCode - 937. Reorder Data in Log Files
# Link : https://leetcode.com/problems/reorder-data-in-log-files/

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter , digit = [],[]
        for log in logs:
            if log.split()[1].isdigit():
                digit.append(log)
            else:
                letter.append(log)
        letter.sort(key=lambda x:(x.split()[1:],x.split()[0]))
        return letter + digit