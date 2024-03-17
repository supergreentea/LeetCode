class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        answers = [0] * N
        stack = []
        
        for day, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prevDay = stack.pop()
                answers[prevDay] = day - prevDay
            stack.append(day)
        
        return answers