class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        if len(colors) == 1:
            return 0
            
        needed_time = 0
        
    
        prev_color = colors[0]
        max_time = neededTime[0]
        curr_sum = max_time
        
        index = 1
        while index < len(neededTime):
            if colors[index] != colors[index - 1]:
                needed_time += curr_sum - max_time
                curr_sum = max_time = neededTime[index]
            else:
                curr_sum += neededTime[index]
                max_time = max(max_time, neededTime[index])
            index += 1
        needed_time += curr_sum - max_time
        
        return needed_time
            
            