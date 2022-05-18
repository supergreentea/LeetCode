class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        visited = set()
        count = 0
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(i):
            visited.add(i)
            for adj in graph[i]:
                if adj not in visited:
                    dfs(adj)

        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        
        return count