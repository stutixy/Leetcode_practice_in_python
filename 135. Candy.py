class Solution:
    def candy(self, ratings: List[int]) -> int:
        size = len(ratings)
        candy = [1 for i in range(size)]
        for i in range(1, size):
            if ratings[i-1] < ratings[i]:
                candy[i] = candy[i-1] + 1
       
        for i in range(size-2, -1, -1):
            if ratings[i] > ratings[i+1] and candy[i]<=candy[i+1]:
                candy[i] = candy[i+1] + 1
        sum = 0
        for i in range(size):
            sum += candy[i]
        
        
            
        return sum
        