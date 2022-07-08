class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = { 1 : set(["()"]) }
        
        if n == 1:
            return combinations[1]
        
        for i in range(2, n + 1):
            combinations[i] = set()
            for j in range(1, i // 2 + 1):
                first_set = combinations[j]
                second_set = combinations[i - j]
                
                for first_combination in first_set:
                    for insert_index in range(len(first_combination) + 1):
                        for second_combination in second_set:
                            new_combination = first_combination[:insert_index] + second_combination + first_combination[insert_index:]
                            combinations[i].add(new_combination)
        for c in combinations.values():
            print(len(c))
                        
        return combinations[n]