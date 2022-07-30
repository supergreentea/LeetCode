class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(graph)
        
        
        def backtrack(node = 0, path = [0]):
            if node == n - 1:
                res.append(path.copy())
                return
            
            for nbr in graph[node]:
                path.append(nbr)
                backtrack(nbr, path)
                path.pop()
        
        backtrack()
        return res