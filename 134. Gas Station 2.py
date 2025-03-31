class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        minFuel = float('inf')
        minIndex = 0
        fuelAvailable = 0

        for i in range(len(gas)):
            if minFuel > fuelAvailable:
                minFuel = fuelAvailable
                minIndex = i
            fuelAvailable += gas[i]
            fuelAvailable -= cost[i]
        if fuelAvailable >= 0:
            return minIndex
        return -1

        