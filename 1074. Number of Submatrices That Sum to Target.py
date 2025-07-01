class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # calculate prefix sum
        prefixSumMatrix = [[0 for _ in range(len(matrix[0]))] for i in range(len(matrix))]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                left = prefixSumMatrix[r][c-1] if c > 0 else 0
                top = prefixSumMatrix[r-1][c] if r > 0 else 0
                topleft =  prefixSumMatrix[r-1][c-1] if r > 0 and c > 0 else 0
                prefixSumMatrix[r][c] = left + top - topleft + matrix[r][c]
        
        res = 0
        for r2 in range(len(matrix)):
            for r1 in range(r2+1):
                prefixCount = {0:1}
                for c in range(len(matrix[r1])):
                    top = prefixSumMatrix[r1-1][c] if r1 > 0 else 0
                    total = prefixSumMatrix[r2][c] - top
                    diff = total - target
                    res += prefixCount.get(diff, 0)
                    prefixCount[total] = 1 + prefixCount.get(total, 0)
                    
        return res


                