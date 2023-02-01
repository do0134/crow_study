# leetcode 93. Restore IP Addresses
# https://leetcode.com/problems/restore-ip-addresses/description/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        answer = list()

        def back_tracking(answer, cnt, o, temp):
            if cnt == 4 and not o:
                print(temp, cnt)
                answer.append(temp)
                return
            elif cnt == 3 and len(o) > 3:
                print(temp, cnt)
                return
            else:
                if cnt == 3 and check(o):
                    back_tracking(answer, cnt + 1, "", temp + o)
                else:
                    n = len(temp)
                    for i in range(min(3, len(o))):
                        if check(o[:i + 1]):
                            back_tracking(answer, cnt + 1, o[i + 1:], temp + o[:i + 1] + ".")

        def check(num):
            if not num:
                return False
            n = int(num)
            if len(num) == 1:
                return True
            elif num[0] == "0":
                return False
            elif len(num) == 2 and n > 0:
                return True
            elif len(num) == 3 and n <= 255:
                return True
            else:
                return False

        back_tracking(answer, 0, s, "")
        return answer