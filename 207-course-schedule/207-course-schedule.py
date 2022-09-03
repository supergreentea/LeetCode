class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        G = defaultdict(list)
        indegree = defaultdict(int)
        
        for crs, pre in prerequisites:
            G[pre].append(crs)
            indegree[crs] += 1
        
        top_ordering = []
        
        stack = []
        
        for crs in range(numCourses):
            if indegree[crs] == 0:
                stack.append(crs)
        
        while stack:
            pre = stack.pop()
            top_ordering.append(pre)
            for crs in G[pre]:
                indegree[crs] -= 1
                if indegree[crs] == 0:
                    stack.append(crs)
        
        return len(top_ordering) == numCourses