class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(list)
        
        # build adjacency list representation of directed graph
        for crs, prereq in prerequisites:
            prereqs[crs].append(prereq)
            
        on_path, explored = set(), set()
        
        def dfs(crs):
            if crs in on_path: # cycle
                return False
            if crs in explored: # already explored
                return True
            
            on_path.add(crs)
            for pre in prereqs[crs]:
                if not dfs(pre):
                    return False
            on_path.remove(crs)
            explored.add(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True
        
        