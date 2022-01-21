# LeetCode 787. Cheapest Flights Within K Stops
# https://leetcode.com/problems/cheapest-flights-within-k-stops/

# n(노드 갯수), flights 배열, src(시작점), dst(목적지), k(경유지점)
# 경유 지점 k개를 경유하는 가격을 리턴

import collections
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        if src == dst: return 0
        graph, visited = collections.defaultdict(list), collections.defaultdict(lambda: float('inf'))
        for u, v, p in flights:
            graph[u] += [(v, p)]    # graph에 u번에서 v번으로 가는데 드는 비용이 p이다 라는 값 저장
    
        Queue = [(src, -1, 0)]  # 시작지점, 경유지점(-1), cost = 0으로 Queue에 대입
        
        while Queue:
            pos, k, cost = Queue.pop(0)
            if pos == dst or k == K: continue # 시작지점(pos) == 목적지 or 경유지점 == 경유지점(K)인 경우 continue
            for nei, p in graph[pos]:   # 시작지점에 해당하는 graph의 값에서 2개 인자(목적지 nei, 비용 p) 뽑아옴.
                if cost + p >= visited[nei]:    # cost = 0, cost에 비용 p를 더한 값이 visited[nei] 방문리스트[목적지]의 값보다 크면 진행
                    continue
                else:                   # cost = 0, cost에 비용 p를 더한 값이 visited[nei] 방문리스트[목적지]의 값보다 작으면 
                    visited[nei] = cost+p   # visited[목적지]의 값을 = cost+p한 값으로 갱신       
                    Queue += [(nei, k+1, cost+p)]   # Queue에 해당 목적지, 경유지점(초기값 -1)에 +1한 값, 비용으로 cost+p 값 다시 넣어줘서 while문 반복.
                
        return visited[dst] if visited[dst] < float('inf') else -1  #만약 visited[dst] 의 값이 'inf'보다 작은 경우 visted[dst]값 리턴. 아닌경우 경로가 없는 것에 해당하므로 -1 리턴

a = Solution(object).findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,1)
print(a)