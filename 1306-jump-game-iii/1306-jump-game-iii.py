class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque([start])
        visited = set([start])
        while queue:
            index = queue.popleft()
            if arr[index] == 0:
                return True
            left = index - arr[index]
            right = index + arr[index]
            if left >= 0 and not left in visited:
                queue.append(left)
                visited.add(left)
            if right < len(arr) and not right in visited:
                queue.append(right)
                visited.add(right)
        
        return False