class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        G = defaultdict(list)
        for u, v, w in times:
            G[u].append((v, w))
        
        distances = { node : math.inf for node in range(1, n + 1) }
        distances[k] = 0
        
        PQ = [(0, k)]
        while PQ:
            cur_dist, cur_node = heappop(PQ)
            if cur_dist > distances[cur_node]:
                continue
            for nbr, w in G[cur_node]:
                new_dist = cur_dist + w
                if new_dist < distances[nbr]:
                    distances[nbr] = new_dist
                    heappush(PQ, (new_dist, nbr))
        
        ans = 0
        for dist in distances.values():
            if dist == math.inf:
                return -1
            ans = max(ans, dist)
        return ans