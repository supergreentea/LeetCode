class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        min_times = { node : math.inf for node in range(1, n + 1) }
        min_times[k] = 0
        
        PQ = [(0, k)]
        while PQ:
            cur_time, node = heappop(PQ)
            if cur_time > min_times[node]:
                continue
            for nbr, time in graph[node]:
                new_time = min_times[node] + time
                if new_time < min_times[nbr]:
                    min_times[nbr] = new_time
                    heappush(PQ, (new_time, nbr))
        
        print(min_times)
        
        ans = 0
        for time in min_times.values():
            if time == math.inf:
                return -1
            ans = max(ans, time)
        return ans