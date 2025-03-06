class Solution:
    def climbStairs(self, n: int) -> int:
        twoStepBack = 1
        oneStepBack = 1
        currentStep = oneStepBack
        n -= 1
        while n!= 0:
            currentStep = twoStepBack + oneStepBack
            twoStepBack = oneStepBack
            oneStepBack = currentStep
            n -= 1
        return currentStep
    
        