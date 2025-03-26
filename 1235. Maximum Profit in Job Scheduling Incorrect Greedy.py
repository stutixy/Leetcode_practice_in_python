class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = [[startTime[i],endTime[i],profit[i]] for i in range(len(profit))]
        maxDeadline = 0
        for i in range(len(endTime)):
            if maxDeadline < endTime[i]:
                maxDeadline = endTime[i]
       
        profitSeq = [-1 for i in range(maxDeadline)]
        
        jobs = sorted(jobs, key=lambda x: x[2])

        for i in reversed(range(len(jobs))):
            if profitSeq[jobs[i][1]-1] == -1 and profitSeq[jobs[i][0]] == -1:
                interval = jobs[i][1]-jobs[i][0]
                for j in range(interval):
                    profitSeq[jobs[i][1] - j -1] = jobs[i][2] 
                  
        
        profitSum = 0
        for i in range(maxDeadline):
            if profitSeq[i] != -1 and (i == 0 or profitSeq[i] != profitSeq[i-1]):
                    profitSum += profitSeq[i] 
        return profitSum


                



