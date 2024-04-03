class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        answer = [0] * N
        stack = []
        
        for day, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                prevDay = stack.pop()
                answer[prevDay] = day - prevDay
            stack.append(day)
        
        return answer