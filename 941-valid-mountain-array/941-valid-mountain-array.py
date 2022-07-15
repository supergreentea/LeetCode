class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
            if len(arr) < 3:
                return False
            
            if arr[1] <= arr[0]:
                return False
            
            i = 1
            while arr[i] > arr[i - 1] and i < len(arr) - 1: # find peak first
                i += 1

            i -= 1

            if i >= len(arr) - 1:
                return False

            while i + 1 < len(arr):
                if arr[i + 1] >= arr[i]:
                    return False
                i += 1
    
            return True