class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        output = []
        
        graph = defaultdict(list)
        
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        on_stack, visited = set(), set()
        
        def dfs(crs):
            if crs in on_stack:
                return False
            if crs in visited:
                return True
            
            on_stack.add(crs)
            for pre in graph[crs]:
                if not dfs(pre):
                    return False
            on_stack.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return output