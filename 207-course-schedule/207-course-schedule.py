class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        
        # courses visited on dfs stack
        visited = set()
        
        def dfs(course):
            if course in visited: # cycle
                return False
            if graph[course] == []:
                return True # no prerequisitees or prerequisites can be finished
            
            visited.add(course) # add course to dfs stack
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            graph[course] = []
            visited.remove(course) # course no longer on dfs stack
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True