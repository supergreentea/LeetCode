class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Union find
        """
        
        parent = [i for i in range(n)]
        rank = [1] * n
        
        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]] # path compression
                node = parent[node]
            return node
        
        def union(node1, node2):
            component1, component2 = find(node1), find(node2)
            if component1 == component2:
                return 0
            if rank[component1] > rank[component2]:
                parent[component2] = component1
                rank[component1] += rank[component2]
            else:
                parent[component1] = component2
                rank[component2] += rank[component1]
            return 1
        
        components = n
        
        for a, b in edges:
            components -= union(a, b)
        
        return components