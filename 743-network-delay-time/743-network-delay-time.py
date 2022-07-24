class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        travel_time = [math.inf for _ in range(n + 1)]
        travel_time[k] = 0

        PQ = []
        heappush(PQ, (0, k))
        while PQ:
            delay, node = heappop(PQ)
            if delay > travel_time[node]:
                continue
            for neighbor, time in graph[node]:
                new_travel_time = travel_time[node] + time
                if new_travel_time < travel_time[neighbor]:
                    travel_time[neighbor] = new_travel_time
                    heappush(PQ, (new_travel_time, neighbor))

        max_travel_time = 0
        for node in range(1, n + 1):
            if travel_time[node] == math.inf:
                return -1
            max_travel_time = max(max_travel_time, travel_time[node])

        return max_travel_time