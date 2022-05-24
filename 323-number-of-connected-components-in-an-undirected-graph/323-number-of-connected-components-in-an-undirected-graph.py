class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par, rank = [i for i in range(n)], [1] * n
        
        def find(n1):
            while n1 != par[n1]:
                par[n1] = par[par[n1]] # path compression
                n1 = par[n1]
            return n1
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return 1
        
        for n1, n2 in edges:
            n -= union(n1, n2)
            
        return n