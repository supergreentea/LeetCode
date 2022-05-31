class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        par = [i for i in range(n)]
        rank = [1] * n
        
        def find(i):
            while i != par[i]:
                par[i] = par[par[i]]
                i = par[i]
            return i
        
        def union(a, b):
            p1, p2 = find(a), find(b)
            if p1 == p2:
                return 0
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return 1
        
        for a, b in edges:
            n -= union(a, b)
        
        return n