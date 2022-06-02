class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = [False] * len(arr)
        
        def dfs(node):
            if node < 0 or node >= len(arr) or visited[node]:
                return False
            if arr[node] == 0:
                return True
            visited[node] = True
            return dfs(node - arr[node]) or dfs(node + arr[node])
        
        return dfs(start)