class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        minHeap = []
        heapMax = 0

        for n in nums:
            og = n
            while n%2 == 0:
                n //= 2
            minHeap.append((n, max(og, 2*n)))
            heapMax = max(heapMax, n)

        heapq.heapify(minHeap)
        res = float('inf')
        while len(minHeap) == len(nums):
            n, og = heapq.heappop(minHeap)
            res = min(res, heapMax-n)
            if n != og:
                heapq.heappush(minHeap, (n*2, og))
                heapMax = max(heapMax, n*2)
        return res









        