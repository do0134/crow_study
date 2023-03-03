# leetcode 28. Find the Index of the First Occurrence in a String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try :
            answer = haystack.index(needle)
        except :
            return -1
        return answer