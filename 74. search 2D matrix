class Solution(object):
    def searchMatrix(self, matrix, target):
        row = 0
        col = len(matrix[row])-1
        totalrows = len(matrix)
        
        while row < totalrows and col > -1 :
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return False
        

