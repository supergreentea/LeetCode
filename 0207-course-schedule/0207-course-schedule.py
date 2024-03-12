class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        G = defaultdict(list)
        for crs, pre in prerequisites:
            G[pre].append(crs)
        
        visited = [False] * numCourses
        inStack = [False] * numCourses

        def dfs(pre):
            if inStack[pre]:
                return True
            if visited[pre]:
                return False
            
            visited[pre] = True
            inStack[pre] = True
            for crs in G[pre]:
                if dfs(crs):
                    return True
            inStack[pre] = False
            return False
        
        for i in range(numCourses):
            if dfs(i):
                return False
        
        return True
