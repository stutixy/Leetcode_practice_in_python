class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [nums[i] for i in range(n)] 
        suffix = [nums[i] for i in range(n)]
        answer = [0 for i in range(n)]
        for i in range(1, n):
            prefix[i] = prefix[i-1]*prefix[i]
      
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1]*suffix[i]
        
        for i in range(n):
            if i == 0:
                answer[i] = suffix[i+1]
            elif i == n-1:
                answer[i] = prefix[i-1]
            else:
                answer[i] = suffix[i+1] * prefix[i-1]

        return answer