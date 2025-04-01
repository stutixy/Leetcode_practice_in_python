class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            newStone = abs(heapq.heappop(stones)) - abs(heapq.heappop(stones))
            if newStone > 0:
                heapq.heappush(stones, 0-newStone)
        
        if len(stones) == 1:
            return abs(stones[0])
        return 0

        