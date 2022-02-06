# BAEKJOON 11816. 8진수, 10진수, 16진수
# https://www.acmicpc.net/problem/11816
# 브론즈 2

# 개처럼 수동으로 푼 풀이
# Python 3 / time : 72ms / Memory : 30864 KB / 코드길이 787 B

import sys

N = sys.stdin.readline().strip()
sum = 0
mag = 1
toggle = False
if N[0] == '0':
    if N[1] == 'x':
        newN = N[2:]
        idx = -1
        oct = {'a' : 10, 'b' : 11, 'c' : 12, 'd' : 13, 'e' : 14, 'f' : 15}
        while True:
            if abs(idx) > len(newN):
                toggle = True
                break
            if newN[idx] in oct:
                sum += oct[newN[idx]] * mag
            else: sum += int(newN[idx]) * mag
            mag *= 16
            idx -= 1
    else:
        newN = N[1:]
        idx = -1
        while True:
            if abs(idx) > len(newN):
                toggle = True
                break
            sum += int(newN[idx]) * mag
            mag *= 8
            idx -=1

if toggle == True:
    print(sum)
else: print(N)


# Pythonic한 풀이

import sys

N = sys.stdin.readline().strip(); no = 10
if N[:2] == '0x':
    N = N[2:]; no = 16
elif N[0] =='0':
    N = N[1:]; no = 8

print(int(N,no))
