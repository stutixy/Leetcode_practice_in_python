class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        w = abs(k)
        ans = [0]*len(code)
        sum = 0
        n = len(code)

        if k < 0:
            start = n-1
            end = n-1
            sum = 0
            while start >= 0:
                i = (start + 1) % n
                
                l = 0
                if end > start:
                    l = start - end - n + 1
                else:
                    l = start - end + 1

                if l <= w:
                    sum += code[end]
                    end -= 1
                else:
                    ans[i] = sum
                    sum -= code[start]
                    start -= 1
        elif k > 0:
            start = 0
            end = 0
            sum = 0
            while start < n:
                i = (start - 1 + n) % n
                end = end % n

                l = 0

                if end < start:
                    l = end + n - start + 1
                else:
                    l = end - start + 1

                if l <= w:
                    sum += code[end]
                    end += 1
                else:
                    ans[i] = sum
                    sum -= code[start]
                    start += 1
        return ans

        