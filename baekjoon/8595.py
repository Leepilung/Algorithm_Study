# BAEKJOON 8595. 히든 넘버
# https://www.acmicpc.net/problem/8595
# 브론즈 1

# 조금 어이가 없는 문제.
# 풀이 접근법 -> string 갯수가 500만이라 500만번을 일일히 탐사하는부분이 시간초과가 발생할것이라고 판단.
# 기존 풀이법 -> string 탐사하면서 숫자만 조합시키면서 가산 -> 시간초과
# 근대 문자열을 '#'으로 바꾸고 이걸 기점으로 배열을 만들었는데 이래도 배열안에 500만개가 들어가는건 같다고 생각하는데
# 풀이과정에서 전자는 시간초과, 후자는 통과하는것을 보니 단순히 문자열 500만개 탐색이랑 리스트안의 요소 500만개 탐색이랑 속도차이가 존재하는듯..(?)

# python3 / time : 632ms / Memory : 88476 KB
from string import ascii_letters
import sys

n = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

letters = ascii_letters

for i in letters:
    if i in b:
        b = b.replace(i,'#')
b = b.split('#')

sum = 0
for i in b:
    if i != '':
        sum += int(i)
print(sum)

# Pythonic한 풀이방법
# 정규식 연산 (re 모듈 사용 풀이법)
# 정규표현식 공부하기 
# https://greeksharifa.github.io/%EC%A0%95%EA%B7%9C%ED%91%9C%ED%98%84%EC%8B%9D(re)/2018/07/20/regex-usage-01-basic/

# 속도도 1/3 정도 빨라지고 코드 간결성은 비교불가인듯.

import re

n = input()
b = input()
pat = re.compile('[0-9]+')
arr = re.findall(pat, b)
print(sum(map(int, arr)))