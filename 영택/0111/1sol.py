# leetcode 1443. Minimum Time to Collect All Apples in a Tree
# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/description/
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = [[]*n for _ in range(n)]

        for i,j in edges :
            tree[i].append(j) 
            tree[j].append(i)
        
        def dfs(p,node) :
            answer = 0

            for i in tree[node] :
                if i != p :
                    answer += dfs(node,i)
            
            if (hasApple[node] or answer > 0) and node != 0 :
                answer += 2

            return answer
        
        return dfs(-1,0) 
