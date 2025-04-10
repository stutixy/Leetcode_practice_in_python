class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set([word for word in wordDict])
        dp = [None for letter in s]

        def dfs(start):
            if start == len(s):
                return True
            if dp[start] is not None:
                return dp[start] 
            
            isBreakable = False
            for i in range(start, len(s)):
                if s[start:i+1] in words:
                    isBreakable = dfs(i+1)
                    if isBreakable:
                        dp[start] = isBreakable
                        return True
            dp[start] = isBreakable
            return isBreakable
        
        return dfs(0)




        
        