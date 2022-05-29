class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for c in range(numCourses):
            graph[c] = []
        for a, b in prerequisites:
            graph[a].append(b)
        
        visited = set()
        def dfs(c):
            if c in visited:
                return False # already on recursion stack, indicates a cycle
            if graph[c] == []:
                return True            
            visited.add(c)

            for p in graph[c]:
                if not dfs(p):
                    return False
            graph[c] = []
            visited.remove(c)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
            

            