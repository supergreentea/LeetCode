class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        travel_time = [math.inf for _ in range(n + 1)]
        travel_time[k] = 0
        max_travel_time = 0
        visited = set()

        PQ = []
        heappush(PQ, (0, k))
        while PQ:
            delay, node = heappop(PQ)
            visited.add(node)
            for neighbor, time in graph[node]:
                if neighbor in visited:
                    continue
                new_travel_time = travel_time[node] + time
                if new_travel_time < travel_time[neighbor]:
                    travel_time[neighbor] = new_travel_time
                    heappush(PQ, (new_travel_time, neighbor))
                    max_travel_time = max(max_travel_time, new_travel_time)

        return max(travel_time[1:]) if len(visited) == n else -1