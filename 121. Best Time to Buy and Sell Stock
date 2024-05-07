class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        if size < 2:
            return 0
        else:
            buy = prices[0]
            sell = 1
            profit = 0
            while sell < size:
                if buy>prices[sell]:
                    buy = prices[sell]
                else :
                    if(prices[sell] - buy > profit):
                        profit = prices[sell] - buy
                sell += 1
            return profit

        