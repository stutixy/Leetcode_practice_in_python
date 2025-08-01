class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def countPairs(prod):
            pairs = 0 
            
            for num in nums1:
                
                l = 0
                r = len(nums2)-1
                if num < 0:
                    m = len(nums2)
                    while l<=r:
                        mid = (l+r)//2
                        if nums2[mid]*num > prod:
                            l = mid + 1
                        else:
                            m = mid
                            r = mid - 1 
                    pairs += len(nums2)- m
                elif num > 0:
                    m = -1
                    while l<=r:
                        mid = (l+r)//2
                        if nums2[mid]*num > prod:
                            r = mid - 1
                        else:
                            m = mid
                            l = mid + 1
                    pairs += (m + 1)
                else :
                    if prod >= 0:
                        pairs += len(nums2)
            return pairs
        
        l, r = -int(1e10), int(1e10)
        res = 0
        while l < r:
            mid = (l+r) // 2
            pairs = countPairs(mid)
            if pairs < k:
                l = mid + 1
            else:
                r = mid
        return r

        


