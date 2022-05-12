class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        count = 0
        
        for node in range(n):
            if node not in visited:
                queue = deque([node])
                visited.add(node)
                while queue:
                    nextNode = queue.popleft()
                    for adj in graph[nextNode]:
                        if adj not in visited:
                            queue.append(adj)
                            visited.add(adj)
                count += 1
                
        return count
                
                
                