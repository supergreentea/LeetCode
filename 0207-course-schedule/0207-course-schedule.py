class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        G = defaultdict(list)
        onStack = [False] * numCourses
        visited = [False] * numCourses
        
        for course, prerequisite in prerequisites:
            G[prerequisite].append(course)
        
        def isCyclic(course: int):
            if onStack[course]:
                return True
            if visited[course]:
                return False
            onStack[course] = True
            visited[course] = True
            for neighbor in G[course]:
                if isCyclic(neighbor):
                    return True
            onStack[course] = False
            return False
        
        for course in range(numCourses):
            if isCyclic(course):
                return False
        
        return True