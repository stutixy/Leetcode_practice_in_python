/**
 * // This is the MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * type MountainArray struct {
 * }
 *
 * func (this *MountainArray) get(index int) int {}
 * func (this *MountainArray) length() int {}
 */

func findInMountainArray(target int, mountainArr *MountainArray) int {
    length := mountainArr.length()
    l := 1
    r := length - 2
    peak := 0
    for l <= r {
        mid := int((l+r) / 2)
        left := mountainArr.get(mid-1)
        curr := mountainArr.get(mid)
        right := mountainArr.get(mid+1)
        if left < curr && curr < right {
            l = mid + 1
        } else if right < curr && curr < left {
            r = mid -  1
        } else {
            peak = mid
            break
        }
    }

    
    l = 0
    r = peak 

    for l <= r {
        mid := int((l+r) / 2)
        curr := mountainArr.get(mid)
        
        if curr < target {
            l = mid + 1
        } else if curr > target {
            r = mid -  1
        } else {
            return mid
        }
    }

    l = length - 1
    r = peak

    for l >= r {
        mid := int((l+r) / 2)
        curr := mountainArr.get(mid)
        
        if curr < target {
            l = mid - 1
        } else if curr > target {
            r = mid +  1
        } else {
            return mid
        }
    }
    return -1
}