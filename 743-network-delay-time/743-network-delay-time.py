class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        G = defaultdict(list)
        for u, v, w in times:
            G[u].append((v, w))
        
        dist = { node : math.inf for node in range(1, n + 1) }
        dist[k] = 0
        PQ = [(0, k)]
        while PQ:
            cur_d, node = heappop(PQ)
            if cur_d > dist[node]:
                continue
            for nbr, w in G[node]:
                new_d = cur_d + w
                if new_d < dist[nbr]:
                    dist[nbr] = new_d
                    heappush(PQ, (new_d, nbr))
        
        ans = 0
        for d in dist.values():
            if d == math.inf:
                return -1
            ans = max(ans, d)
        return ans