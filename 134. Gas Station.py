class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        g = 0
        totalg = 0
        start = 0
        for i in range(n):
            g += gas[i] 
            totalg += gas[i] - cost[i]
            if g<cost[i]:
                g = 0
                start = i+1
            else:
                g -= cost[i]
       
        if totalg>=0:
            return start
        return -1
