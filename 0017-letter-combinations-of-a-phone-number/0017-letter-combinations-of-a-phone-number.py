class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        charMapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        combinations = []
        
        def backtrack(combination: List[int] = [], index: int = 0):
            if len(combination) == len(digits):
                combinations.append("".join(combination[:]))
                return
            for char in charMapping[digits[index]]:
                combination.append(char)
                backtrack(combination, index + 1)
                combination.pop()
        
        backtrack()
        return combinations