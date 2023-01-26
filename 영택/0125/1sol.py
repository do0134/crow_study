# leetcode 2359. Find Closest Node to Given Two Nodes
# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/description/
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)

        def dfs(root, arr, move):
            arr[root] = move
            edge = root
            while edges[edge] != -1:
                edge = edges[edge]
                if edge == -1:
                    arr[edge] = -1
                    break
                move += 1
                if arr[edge] != -1:
                    break
                arr[edge] = move

        answer = -1
        check1 = [-1] * n
        check2 = [-1] * n

        dfs(node1, check1, 0)
        dfs(node2, check2, 0)

        for i in range(n):
            if check1[i] != -1 and check2[i] != -1:
                if answer == -1:
                    answer = i
                elif max(check1[answer], check2[answer]) > max(check1[i], check2[i]):
                    answer = i

        return answer