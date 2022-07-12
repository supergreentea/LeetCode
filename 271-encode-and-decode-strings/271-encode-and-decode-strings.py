class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return ''.join(f'{len(s)}:{s}' for s in strs)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        output = []
        i = 0
        while i < len(s):
            colon = s.index(':', i)
            count = int(s[i : colon])
            output.append(s[colon + 1 : colon + 1 + count])
            i = colon + 1 + count
        
        return output
        
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))