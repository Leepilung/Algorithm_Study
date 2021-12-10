# LeetCode - 819. Most Common Word
# Link : https://leetcode.com/problems/most-common-word/

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        count = {}
        cnt = 0
        ans = ""
        for j in "!?',;.":
            paragraph = paragraph.replace(j, " ")

        for i in paragraph.lower().split():
            if i in banned:
                continue
            elif i not in count:
                count[i] = 1
            else:
                count[i] += 1
            if count[i] > cnt:
                cnt = count[i]
                ans = i
        return ans