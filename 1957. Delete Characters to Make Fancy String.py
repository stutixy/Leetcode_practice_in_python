class Solution:
    def makeFancyString(self, s: str) -> str:
        res = [s[0]]
        count  = 1
        for i in range(1,len(s)):
            if s[i-1] == s[i]:
                count += 1
            else:
                count = 1
            if count <= 2:
                res.append(s[i])
        return "".join(res)

        