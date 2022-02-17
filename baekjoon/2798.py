# BAEKJOON 2798. 블랙잭
# https://www.acmicpc.net/problem/2798


import sys
A, B = map(int, sys.stdin.readline().split())
cards = list(map(int,sys.stdin.readline().split()))
result = 0 

for i in range(A):
    for j in range(i+1,A):
        for k in range(j+1,A):
            maxCard = cards[i]+cards[j]+cards[k]
            if maxCard > B:
                continue
            else :
                result = max(result, maxCard)

print(result)