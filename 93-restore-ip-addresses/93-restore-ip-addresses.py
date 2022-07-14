class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        output = []
        
        if len(s) < 4:
            return output
        
        def valid_substring(string):
            if not string:
                return False
            if string[0] == '0':
                return len(string) == 1
            number = int(string)
            return number > 0 and number <= 255
        
        def backtrack(index, builder, dots):
            if dots == 3:
                substring = s[index:]
                if valid_substring(substring):
                    builder.append(substring)
                    output.append(".".join(builder))
                    builder.pop()
                    return
            for i in range(1, 4):
                substring = s[index : index + i]
                if valid_substring(substring):
                    builder.append(substring)
                    backtrack(index + i, builder, dots + 1)
                    builder.pop()
        
        backtrack(0, [], 0)
        return output