class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        par = [i for i in range(n)]
        rank = [1] * n
        
        def find(i):
            while par[i] != i:
                par[i] = par[par[i]] 
                i = par[i]
            return i
        
        def union(a, b):
            rootA, rootB = find(a), find(b)
            if rootA == rootB:
                return 0
            if rank[rootA] > rank[rootB]:
                par[rootB] = rootA
                rank[rootA] += rank[rootB]
            else:
                par[rootA] = rootB
                rank[rootB] += rank[rootA]
            return 1
        
        res = n
        for a, b in edges:
            res -= union(a, b)
        return res