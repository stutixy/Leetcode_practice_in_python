class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:

        def isSubSeq(sub):
            subtimesk = sub*k
            j = 0
            for i in range(len(s)):
                if s[i] == subtimesk[j]:
                    j += 1
                if j == len(subtimesk):
                    break
            return j == len(subtimesk)

        q = deque()
        q.append("")
        res = ""
        freq = {}
        for c in s:
            freq[c] = 1 + freq.get(c,0)
            
        for c in freq:
            if freq[c] < k:
                freq[c] = 0

        while q:
            temp = q.popleft()
            for c in freq:
                if freq[c] == 0:
                    continue
                curr = temp + c
                if isSubSeq(curr):
                    q.append(curr)
                    if len(curr) > len(res) or curr > res:
                        res = curr
        return res
                     




        