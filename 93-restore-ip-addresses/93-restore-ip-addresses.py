class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        output = []

        def valid(string):
          if not string:
            return False
          if string[0] == "0":
            return len(string) == 1
          integer = int(string)
          return integer >= 0 and integer <= 255

        def backtrack(index = 0, address = [], dots_placed = 0):
          if dots_placed == 3:
            if valid(s[index:]):
              address.append(s[index:])
              output.append(".".join(address))
              address.pop()
              return

          for i in range(1, 4):
            if index + i < len(s):
              substring = s[index : index + i]
              if valid(substring):
                address.append(substring)
                backtrack(index + i, address, dots_placed + 1)
                address.pop()

        backtrack()
        return output