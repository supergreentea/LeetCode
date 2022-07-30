class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        
        n = len(graph)
        
        def backtrack(node, path):
            if node == n - 1:
                res.append(path.copy())
                return
            
            for nbr in graph[node]:
                path.append(nbr)
                backtrack(nbr, path)
                path.pop()
            
        backtrack(0, [0])
        
        return res