class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        par = [i for i in range(n)]
        rank = [1] * n
        
        def find(i):
            while i != par[i]:
                par[i] = par[par[i]]
                i = par[i]
            return i
        
        def union(i, j):
            p1, p2 = find(i), find(j)
            if p1 == p2:
                return 0
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = p1
            else:
                rank[p2] += rank[p1]
                par[p1] = p2
            return 1
        
        res = n
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    res -= union(i, j)
        
        return res