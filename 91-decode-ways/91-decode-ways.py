class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        
        def get_ways(index):
            if index in memo:
                return memo[index]
            
            if index == len(s):
                return 1
            
            if s[index] == '0':
                return 0
            
            if index == len(s) - 1:
                return 1
            
            ans = get_ways(index + 1)
            if index + 1 < len(s) and int(s[index: index + 2]) <= 26:
                ans += get_ways(index + 2)
            
            memo[index] = ans
            return ans
        
        return get_ways(0)