class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        
        while l < r:
            twosum = numbers[l] + numbers[r]
            if twosum > target:
                r -= 1
            elif twosum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        
        return []