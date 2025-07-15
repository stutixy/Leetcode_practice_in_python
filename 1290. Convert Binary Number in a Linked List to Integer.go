/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func getDecimalValue(head *ListNode) int {
    i := 0
    for head != nil {
        i <<= 1
        i += head.Val
        head = head.Next
    }
    return i
    
}