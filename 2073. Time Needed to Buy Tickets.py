class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        for i in range(len(tickets)):
            if i <= k:
                res += min(tickets[i], tickets[k])
            else:
                if tickets[i] >= tickets[k]:
                    res += tickets[k]-1
                else:
                    res += tickets[i]
        return res
       