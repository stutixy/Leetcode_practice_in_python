class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        res = []
        curr = []
        def dfs(i):
            if i == len(s):
                finalString = " ".join(curr)
                res.append(finalString)
                return
            for j in range(i, len(s)):
                subString = s[i:j+1]
                if subString in wordSet:
                    curr.append(subString)
                    dfs(j+1)
                    curr.pop()
        dfs(0)
        return res

        
