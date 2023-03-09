# leetcode 142. Linked List Cycle II
# https://leetcode.com/problems/linked-list-cycle-ii/description/
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next :
            slow, fast = slow.next, fast.next.next
            if slow == fast :
                break
        else :
            return
        while slow != head :
            slow, head = slow.next, head.next
        return head