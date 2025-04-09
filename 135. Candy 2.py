class Solution:
    def candy(self, ratings: List[int]) -> int:
        helper = [1 for rate in ratings]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                helper[i] = helper[i-1] + 1
        for i in range(len(ratings)-2,-1, -1):
            if ratings[i] > ratings[i+1]:
                helper[i] = max(helper[i], helper[i+1]+1)
        sum = 0
        for candy in helper:
            sum += candy
        return sum




            

        