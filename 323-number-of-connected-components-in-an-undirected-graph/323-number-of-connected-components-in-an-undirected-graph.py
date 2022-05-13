class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()
        count = 0
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        for i in range(n):
            if i not in visited:
                count += 1
                visited.add(i)
                queue = deque([i])
                while queue:
                    node = queue.popleft()
                    for adj in graph[node]:
                        if adj not in visited:
                            queue.append(adj)
                            visited.add(adj)
        return count
        
                    