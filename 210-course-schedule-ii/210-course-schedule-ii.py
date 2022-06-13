class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = defaultdict(list)
        
        for crs, pre in prerequisites:
            prereqs[crs].append(pre)
        
        on_path, explored = set(), set()
        ordering = []
        
        def dfs(crs):
            if crs in on_path:
                return False
            if crs in explored:
                return True
            
            on_path.add(crs)
            for pre in prereqs[crs]:
                if not dfs(pre):
                    return False
            on_path.remove(crs)
            explored.add(crs)
            ordering.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return ordering