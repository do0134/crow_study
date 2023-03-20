# leetcode 605. Can Place Flowers
# https://leetcode.com/problems/can-place-flowers/
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        if not n :
            return True
        for i in range(l) :
            if i == l-1 :
                if not flowerbed[i-1] and not flowerbed[i] :
                    n-= 1
                    flowerbed[i] = 1
            elif i == 0 :
                if not flowerbed[i] and not flowerbed[i+1] :
                    n -= 1
                    flowerbed[i] = 1
            elif not flowerbed[i-1] and not flowerbed[i+1] and not flowerbed[i]:
                n -= 1
                flowerbed[i] = 1
            if not n :
                return True
        else : 
            return False