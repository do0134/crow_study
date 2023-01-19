# 149. Max Points on a Line
# https://leetcode.com/problems/max-points-on-a-line/description/
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        answer = 0 
        n = len(points)
        
        for i,p in enumerate(points) :
            temp = defaultdict(lambda : 1)
            temp["max_v"] = 1
            same = 0
            for j in range(i+1, n) :
                dx = p[0] - points[j][0]
                dy = p[1] - points[j][1]
                if dx == 0 and dy == 0 :
                    same += 1
                else : 
                    if dx == 0 :
                        slope = "max_v"
                    else : 
                        slope = dy / dx
                    
                    if not temp[slope] :
                        temp[slope] =1 

                    temp[slope] += 1
            answer = max(answer, max(temp.values())+same)
        return answer