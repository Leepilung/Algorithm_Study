# LeetCode 110. Balanced Binary Tree
# easy
# https://leetcode.com/problems/balanced-binary-tree/

# Runtime : 68ms (54.35%)
# Memory Usage : 18.9MB (47.72%)

# 이진트리가 높이 균형(Height Balanced)를 이루는지 판별하는 문제.
# 높이 균형은 모든 노드의 서브 트리간의 높이 차이가 1 이하인 것을 의미한다.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 재귀구조로 맨 아래 노드까지 파고들어간 후 None 값은 자연스레 0으로 리턴,
# 재귀구조 끝나고 부모노드로 돌아올 때마다 해당 값의 차이가 -1보다 안크면 리턴 받은값에서 +1씩 가산해줌

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if not root:
                return 0
            
            left = check(root.left)
            right = check(root.right)
            
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left,right) + 1
        
        return check(root) != -1
