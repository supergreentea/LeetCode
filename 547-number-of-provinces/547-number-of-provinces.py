class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        
        parent = [i for i in range(n)]
        rank = [1] * n
        
        num_provinces = n
        
    
        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]] # path compression
                node = parent[node]
            return node
        
        # time complexity is reverse ackerman function of n, which is < 5 for practical values of n
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
        
        for city_a in range(n - 1):
            for city_b in range(city_a + 1, n):
                if isConnected[city_a][city_b]:
                    num_provinces -= union(city_a, city_b)
        
        return num_provinces
        
                