class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque([start])
        visited = set()
        while queue:
            index = queue.popleft()
            visited.add(index)
            if arr[index] == 0:
                return True
            if index - arr[index] >= 0 and index - arr[index] not in visited:
                queue.append(index - arr[index])
            if index + arr[index] < len(arr) and index + arr[index] not in visited:
                queue.append(index + arr[index])
        return False