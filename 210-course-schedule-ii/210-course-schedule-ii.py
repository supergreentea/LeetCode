class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        G = defaultdict(list)
        indegree = defaultdict(int)
        
        for crs, pre in prerequisites:
            G[pre].append(crs)
            indegree[crs] += 1
        
        prereqs_fulfilled = []
        for crs in range(numCourses):
            if indegree[crs] == 0:
                prereqs_fulfilled.append(crs)
        
        topological_ordering = []
        
        while prereqs_fulfilled:
            pre = prereqs_fulfilled.pop()
            topological_ordering.append(pre)
            for crs in G[pre]:
                indegree[crs] -= 1
                if indegree[crs] == 0:
                    prereqs_fulfilled.append(crs)
        
        return topological_ordering if len(topological_ordering) == numCourses else []
        
        