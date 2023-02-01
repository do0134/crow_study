# leetcode 1071. Greatest Common Divisor of Strings
# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(check, target):
            if len(check) == len(target):
                if check == target:
                    return True
                return False
            if check != target[:len(check)]:
                return False
            return gcd(check, target[len(check):])

        if str1[0] != str2[0]:
            return ""

        if len(str1) < len(str2):
            str1, str2 = str2, str1

        check1 = ""
        answer = ""
        for i in str1:
            check1 += i
            if gcd(check1, str1) and gcd(check1, str2):
                answer = check1

        if answer:
            return answer
        else:
            return ""
