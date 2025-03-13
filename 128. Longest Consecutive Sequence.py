class Solution(object):
    def longestConsecutive(self, nums):
        n = len(nums)
        numSet = set([nums[i] for i in range(n)])
        maxNum = 0
        while len(numSet) != 0:
            num = numSet.pop()
            count = 1
            back = num-1
            forward = num+1
            while back in numSet:
                count += 1
                numSet.remove(back)
                back -= 1
            while forward in numSet:
                count += 1
                numSet.remove(forward)
                forward += 1
            
            maxNum = max(count, maxNum)      
        return maxNum

        