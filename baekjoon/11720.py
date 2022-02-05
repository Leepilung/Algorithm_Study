# BAEKJOON 11720. 숫자의 합
# https://www.acmicpc.net/problem/11720
# 브론즈 2

# python3 / time : 68ms / Memory : 30864kb

import sys
N = int(sys.stdin.readline().strip())
nums = list(map(int,list(sys.stdin.readline().strip())))

print(sum(nums))