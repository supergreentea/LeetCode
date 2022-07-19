class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        G = defaultdict(list)
        indegree = defaultdict(int)
        
        for crs, pre in prerequisites:
            G[pre].append(crs)
            indegree[crs] += 1
        
        zero_indegree = []
        for crs in range(numCourses):
            if indegree[crs] == 0:
                zero_indegree.append(crs)
        
        top_ordering = []
        
        while zero_indegree:
            pre = zero_indegree.pop()
            top_ordering.append(pre)
            for crs in G[pre]:
                indegree[crs] -= 1
                if indegree[crs] == 0:
                    zero_indegree.append(crs)
        
        return top_ordering if len(top_ordering) == numCourses else []