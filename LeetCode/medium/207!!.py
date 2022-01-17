# LeetCode 207.Course Schedule
# https://leetcode.com/problems/course-schedule/

# course Schedule 선행과목리스트가 주어지면 싸이클 유무 판단하는 문제

# Runtime : 113ms(61.28%)
# Memory Usage : 15.5MB(24.95%)

# LeetCode 풀이방법
# 이해 안감.

class Solution:
    def canFinish(self, n, prerequisites):
        Graph = [[] for i in range(n)]
        degree = [0] * n
        for i, j in prerequisites:
            Graph[j].append(i)
            degree[i] += 1
        bfs = [i for i in range(n) if degree[i] == 0]
        for i in bfs:
            for j in Graph[i]:
                degree[j] -= 1
                if degree[j] == 0:
                    bfs.append(j)
        return len(bfs) == n

a = Solution().canFinish(3,[[2,0],[1,2],[1,0]])

print(a)

# 파알인 풀이법
# 마찬가지로 로직 전체가 자세히는 이해안감. 다시 볼 필요 있음.

import collections
def canFinish(numCourse, prerequisites):
    graph = collections.defaultdict(list)

    for x ,y in prerequisites:
        graph[x].append(y)

    traced = set()
    visited = set()

    def dfs(i):
        if i in traced:
            return False
        if i in visited:
            return True

        traced.add(i)

        for y in graph[i]:
            if not dfs(y):
                return False
        traced.remove(i)
        visited.add(i)

        return True

    for x in list(graph):
            if not dfs(x):
                return False
    
    return True

print(canFinish(3,[[0,2],[0,1],[1,2]]))