class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        count = 0
        for i in range(n):
            if i in visited:
                continue
            queue = deque([i])
            visited.add(i)
            while queue:
                node = queue.popleft()
                for adj in graph[node]:
                    if adj not in visited:
                        queue.append(adj)
                        visited.add(adj)
            count += 1
        return count