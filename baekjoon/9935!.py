# BAEKJOON 9935. 문자열 폭발
# 골드 4
# https://www.acmicpc.net/problem/9935

# Python3 / time : 364ms / Memory : 42044 KB

import sys

string = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()

tmp = []
last = bomb[-1]
length = len(bomb)

for i in string:
    tmp.append(i)
    if i == last and ''.join(tmp[-length:]) == bomb:
        del tmp[-length:]

answer = ''.join(tmp)

if answer == '':
    print('FRULA')
else:
    print(answer)