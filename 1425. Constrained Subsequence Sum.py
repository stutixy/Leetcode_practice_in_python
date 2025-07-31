class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        maxHeap = []
        res = float('-inf')
        for i in range(len(nums)):
            while maxHeap and i - maxHeap[0][1] > k:
                heapq.heappop(maxHeap)
            curr = nums[i]
            if maxHeap:
                curr = max(-maxHeap[0][0] + nums[i], curr)
            res = max(res, curr)
            heapq.heappush(maxHeap, (-curr, i))
        return res





            