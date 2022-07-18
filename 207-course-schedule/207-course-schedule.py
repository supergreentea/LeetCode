class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        G = defaultdict(list)
        indegree = defaultdict(int)
        
        for crs, pre in prerequisites:
            G[pre].append(crs)
            indegree[crs] += 1
        
        print(indegree)
        print(G)
        
        zero_degree = []
        for crs in range(numCourses):
            if indegree[crs] == 0:
                zero_degree.append(crs)
        print(indegree[3])
        
        print(zero_degree)
        
        top_ordering = []
        while zero_degree:
            pre = zero_degree.pop()
            top_ordering.append(pre)
            for crs in G[pre]:
                indegree[crs] -= 1
                if indegree[crs] == 0:
                    zero_degree.append(crs)
        print(indegree)
        print(top_ordering)
        
        return len(top_ordering) == numCourses