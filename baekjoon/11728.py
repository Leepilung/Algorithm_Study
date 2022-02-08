# BAEKJOON 11728. 배열 합치기
# https://www.acmicpc.net/problem/11728
# 실버 5

# Python3 / time : 1716 ms / Memory : 218240 KB
# PyPy3 / 시간초과..

import sys

N = sys.stdin.readline()
A = list(map(int,sys.stdin.readline().split()))
B = list(map(int,sys.stdin.readline().split()))

AB = sorted(A + B)

ans = ''
for i in AB:
    ans += str(i)+' '

print(ans[:-1])