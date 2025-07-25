# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        len = mountainArr.length()
        l = 1
        r = len - 2
        peak = 0
        while l <= r:
            mid = (l+r) // 2
            left = mountainArr.get(mid-1) 
            curr = mountainArr.get(mid) 
            right = mountainArr.get(mid+1) 

            if left < curr < right:
                l = mid + 1
            elif left > curr > right:
                r = mid - 1
            else:
                peak = mid
                break

        l = 0
        r = peak - 1

        while l <= r:
            mid = (l+r) // 2
            curr = mountainArr.get(mid) 
            if curr < target:
                l = mid + 1
            elif curr > target:
                r = mid - 1
            else:
                return mid

        l = len-1
        r = peak

        while l >= r:
            mid = (l+r) // 2
            curr = mountainArr.get(mid) 
            if curr > target:
                r = mid + 1
            elif curr < target: 
                l = mid - 1
            else:
                return mid
            
        return -1
        

            
        class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if not stack or stack[-1].swapcase() != s[i]:
                stack.append(s[i])
            elif stack :
                stack.pop()
        return "".join(stack)
        