class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_left = 0
        dp = [0]
        for c in s:
            if c == 'b':
                b_left += 1
                dp.append(dp[-1])
            else:
                dp.append(min(b_left, dp[-1] + 1))
        return dp[-1]