# LeetCode 328. Odd Even Linked List
# https://leetcode.com/problems/odd-even-linked-list/

# 반복 구조 이용
# Runtime : 40ms(82.85%)
# Memory Usage : 16.3MB(83.42%)

# 공간 복잡도 및 시간 복잡도에 제약 사항이 있던 문제. 내부 함수 사용등은 오프라인 코딩 테스트에서 불이익 가능성 있음.
# 

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            if head is None:
                return None
            
            odd = head # 홀
            even = head.next # 짝
            even_head = head.next
            
            while even and even.next:
                odd.next = odd.next.next    # 홀수 2칸 이동
                even.next = even.next.next  # 짝수 2칸 이동
                odd, even = odd.next, even.next # 이동 시킨 홀, 짝으로 위치값 갱신
                
            odd.next = even_head    # 짝수나 짝수의 다음이 뭐가됐떤 None값일 경우 홀수의 마지막을 짝수 노드와 연결
            return head