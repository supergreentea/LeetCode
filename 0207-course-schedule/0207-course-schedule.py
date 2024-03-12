class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for crs, pre in prerequisites:
            graph[pre].append(crs)
            indegree[crs] += 1
        
        zero_indegrees = []
        for crs in range(numCourses):
            if indegree[crs] == 0:
                zero_indegrees.append(crs)
        topological_ordering = []
        while zero_indegrees:
            pre = zero_indegrees.pop()
            topological_ordering.append(pre)
            for crs in graph[pre]:
                indegree[crs] -= 1
                if indegree[crs] == 0:
                    zero_indegrees.append(crs)
        
        return len(topological_ordering) == numCourses