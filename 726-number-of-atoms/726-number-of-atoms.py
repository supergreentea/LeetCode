class Solution:
    def countOfAtoms(self, formula: str) -> str:
        
        def process_parentheses():
            processed_elements = []
            while stack[-1] != "(":
                processed_elements.append(process_element())
            stack.pop()
            return processed_elements
        
        def process_element():
            # get count
            count_string = ""
            while stack[-1].isdigit():
                count_string = stack.pop() + count_string
            count = int(count_string) if count_string != "" else 1
            # get element
            element = ""
            while stack[-1].islower():
                element = stack.pop() + element
            element = stack.pop() + element
            # return tuple
            return element, count
        
        stack = []
        processed_stack = [] 
        
        counts = defaultdict(int)
        
        i = 0
        while i < len(formula):
            if formula[i] == ')':
                processed_elements = process_parentheses()
                
                # get multiplier
                j = i + 1
                while j < len(formula) and formula[j].isdigit():
                    j += 1
                multiplier_string = formula[i + 1 : j]
                multiplier = int(multiplier_string) if multiplier_string != "" else 1
                i = j
                print(processed_elements)
                print(multiplier)
                
                string = ""
                for element, count in processed_elements:
                    string += element
                    multiplied = count * multiplier
                    if multiplied > 1:
                        string += str(multiplied)
                
                for c in string:
                    stack.append(c)
                
            else:
                stack.append(formula[i])
                i += 1
        
        while stack:
            element, count = process_element()
            counts[element] += count
        
        sorted_elements = sorted(counts.keys())
        
        ans = []
        for element in sorted_elements:
            ans.append(element)
            if counts[element] > 1:
                ans.append(str(counts[element]))
        
        return "".join(ans)
        
        