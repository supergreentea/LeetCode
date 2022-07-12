class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n
        
        def find(a):
            while a != par[a]:
                par[a] = par[par[a]]
                a = par[a]
            return a
        
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
        
        components = n
        
        for a, b in edges:
            components -= union(a, b)
        
        return components