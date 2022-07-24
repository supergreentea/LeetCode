class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        G = defaultdict(list)
        for u, v, w in times:
            G[u].append((v, w))
        D = { node : math.inf for node in range(1, n + 1) }
        D[k] = 0
        PQ = [(0, k)]
        while PQ:
            dist, node = heappop(PQ)
            if dist > D[node]:
                continue
            for nbr, w in G[node]:
                new_dist = dist + w
                if new_dist < D[nbr]:
                    D[nbr] = new_dist
                    heappush(PQ, (new_dist, nbr))
        ans = 0
        for dist in D.values():
            if dist == math.inf:
                return -1
            ans = max(ans, dist)
        return ans