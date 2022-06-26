class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2' : ["a", "b", "c"],
            '3' : ["d", "e", "f"],
            '4' : ["g", "h", "i"],
            '5' : ["j", "k", "l"],
            '6' : ["m", "n", "o"],
            '7' : ["p", "q", "r", "s"],
            '8' : ["t", "u", "v"],
            '9' : ["w", "x", "y", "z"]
        }
        
        output = []
        
        if not digits:
            return output
        
        def backtrack(index, combination):
            if index == len(digits):
                output.append("".join(combination))
                return
            
            for char in mapping[digits[index]]:
                combination.append(char)
                backtrack(index + 1, combination)
                combination.pop()
        
        backtrack(0, [])
        
        return output
                