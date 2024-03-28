class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #time: O(4 ^ len(digits))
        #space: O(len((digits)))
        
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
        
        def backtrack(digitIndex: int = 0, combination: List[str] = []) -> None:
            if len(combination) == len(digits):
                answer.append("".join(combination))
                return
            digit = digits[digitIndex]
            for letter in digitToLetters[digit]:
                combination.append(letter)
                backtrack(digitIndex + 1, combination)
                combination.pop()
        
        backtrack()
        return answer