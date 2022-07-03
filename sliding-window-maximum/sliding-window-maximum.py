class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque() # indices
        output = []
        l = r = 0
        while r < len(nums):
            # pop smaller values from queue
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)
            
            # remove left value from window
            if l > queue[0]:
                queue.popleft()
            
            if r >= k - 1: # window is at least size k
                output.append(nums[queue[0]])
                l += 1
            r += 1
        return output
            
        