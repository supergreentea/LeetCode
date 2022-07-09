class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def valid(parenthesis):
            stack = []
            for c in parenthesis:
                if c != ')':
                    stack.append(c)
                else:
                    if stack and stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
            return not stack
        
        output = []
        
        def backtrack(parenthesis = ""):
            if len(parenthesis) == 2 * n:
                if valid(parenthesis):
                    output.append(parenthesis)
                return
            backtrack(parenthesis + "(")
            backtrack(parenthesis + ")")
        
        backtrack()
        return output