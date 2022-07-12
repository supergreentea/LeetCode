class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        closed_to_open = {
            ']' : '[',
            ')' : '(',
            '}' : '{'
        }
        
        for c in s:
            if c in closed_to_open:
                if stack and stack[-1] == closed_to_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return not stack
        