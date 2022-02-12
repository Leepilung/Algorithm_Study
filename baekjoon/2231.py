# BAEKJOON 2231. 분해합
# https://www.acmicpc.net/problem/2231
# 브론즈 2

# Python3 / time : 4428 ms / Memory : 30864 KB
import sys

# N = int(sys.stdin.readline())
# n = 1
# newN = 1
# toggle = False
# for i in range(1,N+1):
#     idx = 0
#     newN = i
#     while True:
#         if idx == len(str(i)):
#             break
#         else:
#             newN += int(str(i)[idx])
#             idx += 1
#     if newN == N:
#         print(i)
#         toggle = True
#         break

# if toggle == False:
#     print(0)

# ----------------------------

# 좀더 간결하고 빠른 풀이.
# Python3 / time : 1196 ~1224 ms / Memory 30864 KB

N = int(sys.stdin.readline())
toggle = False
for i in range(N):
    if sum(map(int,str(i))) + i == N:
        print(i)
        toggle = True
        break

if toggle == False:
    print(0)
