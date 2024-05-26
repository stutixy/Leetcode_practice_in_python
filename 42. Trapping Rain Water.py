class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)
        maxleft = [height[i] for i in range(size)]
        maxright = [height[i] for i in range(size)]

        for i in range(1, size):
            maxleft[i] = max(maxleft[i-1], maxleft[i])

        for i in range(size-2, -1, -1):
            maxright[i] = max(maxright[i+1], maxright[i])
        sum = 0
        for i in range(size):
            height[i] = min(maxleft[i], maxright[i]) - height[i]
            if height[i]<0:
                height[i] = 0
            sum += height[i]
        return sum
        
        