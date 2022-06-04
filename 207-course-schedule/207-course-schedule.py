class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        for a, b in prerequisites:
            graph[a].append(b)
        
        visited = set()
        def dfs(course):
            if graph[course] == []:
                return True # no prerequisites for this course
            if course in visited:
                return False # cycle detected
            
            visited.add(course)
            for p in graph[course]:
                if not dfs(p):
                    return False
            graph[course] = []
            return True
        
        for i in range(0, numCourses):
            if not dfs(i):
                return False
        
        return True