class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counts = [0] * 1001
        for num in arr1:
            counts[num] += 1
        
        i = 0
        for num in arr2:
            while counts[num] > 0:
                arr1[i] = num
                i += 1
                counts[num] -= 1
        
        for num in range(1001):
            while counts[num] > 0:
                arr1[i] = num
                i += 1
                counts[num] -= 1
            
        return arr1
                