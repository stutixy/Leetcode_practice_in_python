func kthSmallestProduct(nums1 []int, nums2 []int, k int64) int64 {
    l,r := -int64(1e10), int64(1e10)
    res := int64(0)
    for l <= r {
        mid := int64((l+r)/2)
        pairs := count(nums1, nums2, mid)
        if pairs < k {
            l = mid+1
        } else {
            res = mid
            r = mid - 1
        }
    }
     return res
}

func count(nums1 []int, nums2 []int, prod int64) int64 {
    pairs := 0
    for _,v := range nums1 {
        n := len(nums2)
        l := 0
        r := n - 1
        if v < 0 {
            m := n
            for l <= r {
                mid := ((l+r)/2)
                if int64(nums2[mid] * v) > prod {
                    l = mid + 1
                } else {
                    m = mid
                    r = mid - 1
                }
            } 
            pairs += (n-m)
        } else if v > 0 {
            m := -1
            for l <= r {
                mid := int((l+r)/2)
                if int64(nums2[mid] * v) > prod {
                    r = mid - 1
                } else {
                    m = mid
                    l = mid + 1
                }
            } 
            pairs += (m+1)
        } else {
            if prod >= 0{
                pairs += n
            }
        }
    }
    return int64(pairs)
}