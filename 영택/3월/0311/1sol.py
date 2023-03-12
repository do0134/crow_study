# leetcode 109. Convert Sorted List to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return
        val = self.get_value(head)
        n = len(val)
        return self.dfs(0, n - 1, val)

    def get_value(self, head):
        val = list()
        while head:
            val.append(head.val)
            head = head.next
        return val

    def dfs(self, s, e, values):
        if s > e:
            return

        mid = (s + e) // 2
        node = TreeNode(values[mid])
        node.left = self.dfs(s, mid - 1, values)
        node.right = self.dfs(mid + 1, e, values)
        return node