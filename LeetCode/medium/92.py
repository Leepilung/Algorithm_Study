# LeetCode 92. Reverse Linked List II
# https://leetcode.com/problems/reverse-linked-list-ii/

# 특정 인덱스의 노드구조를 역순으로 재정렬 하는 문제

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        root = start = ListNode(None)   # 임의의 루트노드 생성
        root.next = head    # 루트 노드의 next를 head로 초기화
        
        for _ in range(left-1): # left -1번만큼 start를 start.next값으로 바꿔줌(이동)
            start = start.next
        end = start.next    # end 값을 start.next에 저장 end값은 계속해서 바꿔줌.
        
        # 반복하면서 노드를 차례로 뒤집는 구문
        for _ in range(right - left):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        
        # root = ListNode{val: None,  next: ListNode{val: 4, next: ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 5, next: None}}}}}
        return root.next