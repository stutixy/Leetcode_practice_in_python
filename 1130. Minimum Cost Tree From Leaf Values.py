class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = [float('inf')]
        i = 0
        sum = 0
        for num in arr:
            while len(stack) > 1 and stack[-1] < num:
                top = stack.pop()
                sum = sum + (top * min(num, stack[-1]))
                
            stack.append(num)
        
        while len(stack) > 2:
            less = stack.pop()
            greater = stack[-1]
            sum = sum + (less * greater)
        return sum  


        