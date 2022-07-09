class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        mappings = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z']
        }
        
        output = []
        
        if not digits:
            return output
        
        def backtrack(index = 0, combination = []):
            if index == len(digits):
                output.append("".join(combination))
                return
            
            for letter in mappings[digits[index]]:
                combination.append(letter)
                backtrack(index + 1, combination)
                combination.pop()
        
        backtrack()
        return output