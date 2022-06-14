class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        - sort the array
        - reduce problem to 2sum 
        - loop through array
        - for each number, look for pair such that the three numbers sum up to 0
        - we can use two pointers for the pair, left starting right after current number and other at end of array
        - we can calibrate sum using pointers and using sorted property of array:
            - to increase the sum, we can move left pointer to right
            - to decrease sum, we can move right pointer to left
        """
        nums.sort()
        n = len(nums)
        triplets = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                t = nums[i] + nums[l] + nums[r]
                if t < 0:
                    l += 1
                elif t > 0:
                    r -= 1
                else:
                    triplets.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return triplets