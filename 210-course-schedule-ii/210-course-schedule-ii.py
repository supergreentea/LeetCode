class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        G = defaultdict(list)
        for crs, pre in prerequisites:
            G[pre].append(crs)
        
        print(G)
        
        indegree = [0 for crs in range(numCourses)]
        for crs in G:
            for pre in G[crs]:
                indegree[pre] += 1
        
        print(indegree)
        
        zero_degrees = []
        
        for crs in range(numCourses):
            if indegree[crs] == 0:
                zero_degrees.append(crs)
                
        print(zero_degrees)
        
        top_ordering = []
        
        while zero_degrees:
            crs = zero_degrees.pop()
            top_ordering.append(crs)
            for pre in G[crs]:
                indegree[pre] -= 1
                if indegree[pre] == 0:
                    zero_degrees.append(pre)
        
        return top_ordering if len(top_ordering) == numCourses else []