# BAEKJOON 11653. 소인수분해
# https://www.acmicpc.net/problem/11653
# 실버 5
# 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.


# 에라토스테네스의 체 이용 풀이.
# pypy3 / time : 1304ms / Memory : 225624KB

def prime_list(n):
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:        
            for j in range(i+i, n, i): #
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]

import sys
N = int(sys.stdin.readline().strip())
prime_number = prime_list(N)
prime_number.append(N)

while True:
    if N == 1:
        break
    for i in prime_number:
        if N % i == 0:
            N /= i
            print(i)
            break

# 초간단 풀이..
# pypy3 / time : 228ms / Memory : 124504KB 

N=int(input())
d=2
while N>1:
    if not N%d:
        print(d)
        N=N//d
    else: d+=1