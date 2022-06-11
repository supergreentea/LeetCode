class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        for crs, pre in prerequisites:
            graph[crs].append(pre)
        
        on_path, explored = set(), set()
        
        def dfs(crs):
            if crs in on_path:
                return False
            if crs in explored:
                return True
            
            on_path.add(crs)
            for pre in graph[crs]:
                if not dfs(pre):
                    return False
            on_path.remove(crs)
            explored.add(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True