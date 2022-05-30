class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        
        visited = set()
        
        def dfs(c):
            if graph[c] == []:
                return True # course has no prerequisites
            
            if c in visited:
                return False # course already on recursion stack so there is cycle
            
            visited.add(c)
            for p in graph[c]:
                if not dfs(p):
                    return False
            
            graph[c] = []
                
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True
        