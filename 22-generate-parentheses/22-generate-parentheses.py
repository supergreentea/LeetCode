class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        output = []
        
        def valid(parenthesis):
            stack = []
            for char in parenthesis:
                if char == ')':
                    if stack and stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(char)
            return not stack
                
        
        def backtrack(length = 0, parenthesis = ""):
            if length == 2 * n:
                if valid(parenthesis):
                    output.append(parenthesis)
                return
            backtrack(length + 1, parenthesis + "(")
            backtrack(length + 1, parenthesis + ")")
        
        backtrack()
        return output