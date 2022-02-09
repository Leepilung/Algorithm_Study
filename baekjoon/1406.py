# 1406. 에디터
# https://www.acmicpc.net/problem/1406
# 실버3

# 개삽질한 문제 고찰점 : index slice (ex : strings[:5])와 같은 연산은 무조건 O(N) POP의 경우에도 알고있었듯이 인덱스 넣으면 무조건 O(N)
# 경계값 넣을경우 크기가 너무커서 O(N)에 가까운 연산 무조거 시간초과 -> 무조건 O(1)의 풀이로 풀어야함.
# 시간 초과만 5번정도 난듯.
# Python3 / time : 356ms / Memory : 41280 KB

import sys
strings = list(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
tmp = []


for i in range(M):
    command = sys.stdin.readline().split()
    if command[0] == "P":
        strings.append(command[1])
    elif command[0] == 'L' and strings != []:
        tmp.append(strings.pop())
    elif command[0] == 'D' and tmp != []:
        strings.append(tmp.pop())
    elif command[0] == 'B' and strings != []:
        strings.pop()

ans = ''.join(strings + list(reversed(tmp)))

print(ans)