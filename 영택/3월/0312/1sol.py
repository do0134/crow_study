# leetcode 23. Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/description/
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        if len(lists) == 1:
            return lists[0]
        value = list()
        for i in lists:
            value += self.get_value(i)

        value.sort(reverse=True)
        return self.merge(value)

    def get_value(self, node):
        if not node:
            return []
        val = list()
        while node:
            val.append(node.val)
            node = node.next
        return val

    def merge(self, val):
        node = None
        for i in val:
            node = ListNode(i, node)
        return node
