class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        string_builder = []
        for s in strs:
            string_builder.append(str(len(s)))
            string_builder.append("#")
            string_builder.append(s)
        return "".join(string_builder)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        output = []
        start = 0
        while start < len(s):
            i = start
            while s[i] != '#':
                i += 1
            string_length = int(s[start : i])
            output.append(s[i + 1 : i + 1 + string_length])
            start = i + 1 + string_length
        return output
        
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))