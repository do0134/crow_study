# leetcode 2246. Longest Path With Different Adjacent Characters
# https://leetcode.com/problems/longest-path-with-different-adjacent-characters/description/
# 다시 풀어보기

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        tree = [[]*n for _ in range(n)]
        for i in range(1,n) :
            tree[parent[i]].append(i)
        
        self.answer = 1
        
        def dfs(node) :
            length = []
            for i in tree[node] :
                once = dfs(i)
                if s[i] != s[node] :
                    length.append(once)
            length.sort()
            if len(length) >= 2 :
                self.answer = max(self.answer, 1+length[-1]+length[-2])
            elif len(length) == 1 :
                self.answer = max(self.answer,1+length[-1])
            
            if not length : 
                return 1
            else : 
                return 1+length[-1]
        dfs(0)
        return self.answer