class Solution:
    def climbStairs(self, n: int) -> int:
        if n<1:
            return 0
        if n==1:
            return 1
        
        way1Stepback = 1
        way2Stepback = 1
        currentway = 0
        for i in range(2, n+1):
            currentway = way1Stepback + way2Stepback
            way2Stepback = way1Stepback
            way1Stepback = currentway
            
        return currentway


        