class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)
        
        max_rank = 0
        for a in range(n - 1):
            for b in range(a + 1, n):
                rank = len(graph[a]) + len(graph[b])
                if a in graph[b]:
                    rank -= 1
                max_rank = max(max_rank, rank)
        return max_rank