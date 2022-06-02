class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        
        for road in roads:
            a, b = road[0], road[1]
            graph[a].add(b)
            graph[b].add(a)
        
        max_rank = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                rank = len(graph[i]) + len(graph[j])
                if i in graph[j]:
                    rank -= 1
                max_rank = max(max_rank, rank)
        
        return max_rank
            
        
        