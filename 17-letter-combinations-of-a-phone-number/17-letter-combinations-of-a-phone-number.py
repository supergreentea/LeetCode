class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        output = []
        
        if not digits:
            return output
        
        digits_to_letters = { '2': ["a", "b", "c"], '3': ["d", "e", "f"], '4': ["g", "h", "i"], '5': ["j", "k", "l"], '6': ["m", "n", "o"], '7' : ["p", "q", "r", "s"], '8': ["t", "u", "v"], '9': ["w", "x", "y", "z"] }
        
        def backtrack(index = 0, stringbuilder = []):
            if index == len(digits):
                output.append("".join(stringbuilder))
                return
            
            digit = digits[index]
            
            for letter in digits_to_letters[digit]:
                stringbuilder.append(letter)
                backtrack(index + 1, stringbuilder)
                stringbuilder.pop()
            
        backtrack()
        return output