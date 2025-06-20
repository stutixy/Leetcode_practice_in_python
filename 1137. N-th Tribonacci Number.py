class Solution:
    def tribonacci(self, n: int) -> int:
        a = 0
        b = 1
        c = 1

        if n == 0:
            return a
        elif n <3:
            return b
        res = 0
        for i in range(2,n):
            res = a + b + c
            a = b
            b = c 
            c = res
        return res
