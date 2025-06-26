class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        s = s[::-1]
        cur = 0
        ans = 0
        for i in range(len(s)):
            p = int(s[i])
            cur += p * pow(2, i)
            if cur <= k:
                ans += 1
                continue
            if p == 0:
                ans += 1
        return ans 