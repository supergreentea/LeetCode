class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        for crs, pre in prerequisites:
            graph[pre].append(crs)
        
        instack = [False] * numCourses
        visited = [False] * numCourses
        
        def dfs(course):
            if instack[course]:
                return True
            if visited[course]:
                return False
            
            instack[course] = True
            visited[course] = True
            for neighbor in graph[course]:
                if dfs(neighbor):
                    return True
            instack[course] = False
            return False
        
        for i in range(numCourses):
            if dfs(i):
                return False
        
        return True