class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Dict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in Dict:
                return [i, Dict[complement]]
            Dict[nums[i]] = i
        return []