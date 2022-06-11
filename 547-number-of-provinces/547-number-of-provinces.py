class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        par = [i for i in range(n)]
        rank = [1] * n
        
        num_provinces = n
        
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
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return 1
        
        for i in range(n - 1):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    num_provinces -= union(i, j)
        
        return num_provinces