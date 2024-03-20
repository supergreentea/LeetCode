class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digitToLetters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        answer = []
        
        def backtrack(digitIndex: int, combination: List[str]) -> None:
            if len(combination) == len(digits):
                answer.append("".join(combination[:]))
                return
            for letter in digitToLetters[digits[digitIndex]]:
                combination.append(letter)
                backtrack(digitIndex + 1, combination)
                combination.pop()
        
        backtrack(0, [])
        return answer