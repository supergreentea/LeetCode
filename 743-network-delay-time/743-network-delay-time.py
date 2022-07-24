class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        distances = { node : math.inf for node in range(1, n + 1) }
        distances[k] = 0
        
        PQ = [(0, k)]
        while PQ:
            dist, node = heappop(PQ)
            if dist > distances[node]: continue
            for nbr, w in graph[node]:
                new_dist = dist + w
                if new_dist < distances[nbr]:
                    distances[nbr] = new_dist
                    heappush(PQ, (new_dist, nbr))
        ans = 0
        for dist in distances.values():
            if dist == math.inf:
                return -1
            ans = max(ans, dist)
        return ans