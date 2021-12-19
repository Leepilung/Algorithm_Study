# LeetCode 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/

# 노드구조 이해 필요함.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None
        
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
            
        return prev