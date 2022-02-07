# BAEKJOON 1269. 대칭 차집합
# https://www.acmicpc.net/problem/1269
# 자연수가 주어지고 이를 리스트로 바꿔서 값을 출력시켜야 함.

# Python3 / time : 332ms / Memory : 87564 KB

import sys

N = sys.stdin.readline()
A = list(map(int,sys.stdin.readline().split()))
B = list(map(int,sys.stdin.readline().split()))

AB = list(set(A)-set(B))
BA = list(set(B)-set(A))

sum = 0
sum = sum +len(AB) +len(BA)
print(sum)