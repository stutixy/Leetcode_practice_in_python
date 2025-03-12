class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n= len(s)
        if n < len(t):
            return ""

        map = [0]*(128)
        for i in range(len(t)):
            map[ord(t[i])] += 1

        l = 0
        start = 0
        end = 0
        r = 0
        count = len(t)
        minlen = float('inf')
        
        for r in range(n):
            if map[ord(s[r])] > 0:
                count -= 1
            map[ord(s[r])] -= 1
           
            while count == 0:
                if minlen > r-l+1:
                    start = l
                    end = r+1
                    minlen = r-l+1
                   
                map[ord(s[l])] += 1
                if  map[ord(s[l])] > 0:
                    count += 1
                l += 1
        return s[start :end]
            