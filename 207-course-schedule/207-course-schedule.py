class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        # build graph
        for crs, pre in prerequisites:
            graph[crs].append(pre)
        
        # build indegree list
        in_degree = [0 for crs in range(numCourses)]
        for crs in graph:
            for pre in graph[crs]:
                in_degree[pre] += 1
        
        zero_indegree_courses = []
        for crs in range(numCourses):
            if in_degree[crs] == 0:
                zero_indegree_courses.append(crs)
        
        topological_ordering = []
        
        while zero_indegree_courses:
            crs = zero_indegree_courses.pop()
            topological_ordering.append(crs)
            for pre in graph[crs]:
                in_degree[pre] -= 1
                if in_degree[pre] == 0:
                    zero_indegree_courses.append(pre)
        
        return len(topological_ordering) == numCourses
            