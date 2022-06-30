class Solution:
    def compress(self, chars: List[str]) -> int:
        slow = fast = 0
        
        while fast < len(chars):
            count = 1
            chars[slow] = chars[fast]
            
            while fast + 1 < len(chars) and chars[fast + 1] == chars[fast]:
                count += 1
                fast += 1
            
            
            if count > 1:
                for c in str(count):
                    chars[slow + 1] = c
                    slow += 1
            
            slow += 1
            fast += 1
        
        return slow
            
            