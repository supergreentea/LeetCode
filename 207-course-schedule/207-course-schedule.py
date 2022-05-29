class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for c in range(numCourses):
            graph[c] = []
        for a, b in prerequisites:
            graph[a].append(b)
        
        def dfs(c, visited):
            if c in visited:
                return False # already on recursion stack, indicates a cycle
            
            visited.add(c)
            if graph[c] == []:
                visited.remove(c)
                return True
            
            for p in graph[c]:
                if not dfs(p, visited):
                    return False
            graph[c] = []
            visited.remove(c)
            return True
        
        for c in range(numCourses):
            if not dfs(c, set()):
                return False
        return True
            

            