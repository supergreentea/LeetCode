class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        G = defaultdict(list)
        for u, v, w in times:
            G[u].append((v, w))
        
        min_times = { node : math.inf for node in range(1, n + 1) }
        min_times[k] = 0
        
        PQ = [(0, k)]
        while PQ:
            cur_time, cur_node = heappop(PQ)
            if cur_time > min_times[cur_node]: continue
            for nbr, w in G[cur_node]:
                new_time = cur_time + w
                if new_time < min_times[nbr]:
                    min_times[nbr] = new_time
                    heappush(PQ, (new_time, nbr))
        
        ans = 0
        for time in min_times.values():
            if time == math.inf:
                return -1
            ans = max(ans, time)
        return ans