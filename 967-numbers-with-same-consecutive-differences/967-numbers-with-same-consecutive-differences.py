class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = set()
        
        def dfs(subarray):
            if len(subarray) == n:
                res.add("".join(str(i) for i in subarray))
                return
            if not subarray:
                for i in range(1, 10):
                    if i + k < 10 or i - k >= 0:
                        subarray.append(i)
                        dfs(subarray)
                        subarray.pop()
            else:
                left = subarray[-1] - k
                right = subarray[-1] + k
                if left >= 0:
                    subarray.append(left)
                    dfs(subarray)
                    subarray.pop()
                if right < 10:
                    subarray.append(right)
                    dfs(subarray)
                    subarray.pop()
        
        dfs([])
        return res