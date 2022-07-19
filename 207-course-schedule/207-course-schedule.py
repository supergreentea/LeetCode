class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # build adjacency list
        G = defaultdict(list)
        indegree = defaultdict(int)
        
        for crs, pre in prerequisites:
            G[pre].append(crs)
            indegree[crs] += 1
        
        # collect courses with zero prerequisites
        zero_indegree = []
        for crs in range(numCourses):
            if indegree[crs] == 0:
                zero_indegree.append(crs)
        
        top_ordering = []
        
        while zero_indegree:
            pre = zero_indegree.pop()
            top_ordering.append(pre)
            
            # decrease degree for dependencies
            for crs in G[pre]:
                indegree[crs] -= 1
                if indegree[crs] == 0:
                    zero_indegree.append(crs)
        
        # if we are not able to get all courses into the topological ordering then there was a cycle
        return len(top_ordering) == numCourses
        
        