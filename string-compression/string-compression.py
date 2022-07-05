class Solution:
    def compress(self, chars: List[str]) -> int:
        slow = fast = 0
        
        while fast < len(chars):
            count = 1
            
            chars[slow] = chars[fast] # we can overwrite slow because len(str(count)) <= count
            
            while fast + 1 < len(chars) and chars[fast] == chars[fast + 1]:
                count += 1
                fast += 1
            
            # here, fast is pointing to a new character
            
            if count > 1:
                for c in str(count):
                    chars[slow + 1] = c
                    slow += 1
            
            slow += 1 # slow is pointing to directly after the count of previous character
            fast += 1
        
        return slow # slow should be at index after last count was processed