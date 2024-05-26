class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)
        maxleft = 0
        maxright = 0
        left = 0
        right = size-1
        sum = 0
        while left < right:
            if maxleft <= height[left]:
                maxleft = height[left]
            
            if maxright <= height[right]:
                maxright = height[right]

            if maxleft <= maxright:
                height[left] = maxleft-height[left]
                if height[left] < 0:
                    height[left] = 0
                sum += height[left]
                left += 1
            else:
                height[right] = maxright-height[right]
                if height[right] < 0:
                    height[right] = 0
                sum += height[right] 
                right -= 1
        return sum
        
        