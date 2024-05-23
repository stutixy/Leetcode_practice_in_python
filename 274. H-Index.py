class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        temp = [0 for _ in range(n + 1)] 
        
        for i,v in enumerate(citations):
            if v > n:
                temp[n] += 1 
            else:
                temp[v] += 1
        
        count = 0

        for i in range(n, -1, -1):
            count += temp[i]
            if count >= i:
                return i
        return 0 