class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:\
        #time: O(N + M) 
        #space: O(N + M)
        
        graph = defaultdict(list)
        
        indegrees = defaultdict(int)
        
        for crs, pre in prerequisites:
            graph[pre].append(crs)
            indegrees[crs] += 1
        
        zeroIndegrees = []
        
        for crs in range(numCourses):
            if indegrees[crs] == 0:
                zeroIndegrees.append(crs)
        
        topologicalOrdering = []
        while zeroIndegrees:
            crs = zeroIndegrees.pop()
            topologicalOrdering.append(crs)
            for neighbor in graph[crs]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    zeroIndegrees.append(neighbor)
        return len(topologicalOrdering) == numCourses