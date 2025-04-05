class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}
        def dfs(p1,p2):
            if p1 == len(text1) or p2 == len(text2):
                return 0

            if (p1,p2) in cache:
                return cache[(p1,p2)]

            if text1[p1] == text2[p2]:
                cache[(p1,p2)] = 1+dfs(p1+1, p2+1)
                return cache[(p1,p2)]
            cache[(p1,p2)] = max(dfs(p1+1, p2), dfs(p1, p2+1))
            return cache[(p1,p2)]
        
        return dfs(0,0)




