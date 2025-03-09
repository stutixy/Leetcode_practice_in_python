class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n<=1:
            return n
        map = [0]*(128)
        l = 0
        r = 0
        maxlen = 0
        for r in range(n):
            map[ord(s[r])] += 1
            while map[ord(s[r])] > 1:
                map[ord(s[l])] -= 1
                l += 1

            maxlen = max(maxlen, r-l+1)
        return maxlen






        