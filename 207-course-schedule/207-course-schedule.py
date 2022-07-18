class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for crs, pre in prerequisites:
            graph[crs].append(pre)
        
        inDegree = [0 for crs in range(numCourses)]
        
        for crs in range(numCourses):
            for pre in graph[crs]:
                inDegree[pre] += 1
        
        degZeroNodes = []
        for crs in range(numCourses):
            if inDegree[crs] == 0:
                degZeroNodes.append(crs)
        
        topOrdering = []
        
        while degZeroNodes:
            node = degZeroNodes.pop()
            topOrdering.append(node)
            for nbr in graph[node]:
                inDegree[nbr] -= 1
                if inDegree[nbr] == 0:
                    degZeroNodes.append(nbr)
        
        if len(topOrdering) < numCourses:
            return False
        
        return True
        
            