class Solution:
    def maxPerformance(self, n: int, s: List[int], e: List[int], k: int) -> int:
        mod = 10**9 + 7
        perform = [(e[i],s[i]) for i in range(len(s))]
        perform.sort(key = lambda x : x[0])
        minHeap = []
        sum = 0
        res = 0
        for i in range(len(perform)-1, -1, -1):
            ef = perform[i][0]
            sp = perform[i][1]
            sum += sp
            sub = 0
            if len(minHeap) == k:
                sub = heapq.heappop(minHeap)
            sum -= sub
            heapq.heappush(minHeap, sp)
            res = max(res, sum*ef)
        return res % mod
        




            
