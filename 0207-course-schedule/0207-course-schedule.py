class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        G = defaultdict(list)
        indegrees = defaultdict(int)
        for crs, pre in prerequisites:
            G[pre].append(crs)
            indegrees[crs] += 1
        
        zeroIndegrees = []
        for crs in range(numCourses):
            if indegrees[crs] == 0:
                zeroIndegrees.append(crs)
        topologicalOrdering = []
        while zeroIndegrees:
            pre = zeroIndegrees.pop()
            topologicalOrdering.append(pre)
            for neighbor in G[pre]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    zeroIndegrees.append(neighbor)
        return len(topologicalOrdering) == numCourses
                    
                    