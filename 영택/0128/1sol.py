# leetcode 352. Data Stream as Disjoint Intervals
# https://leetcode.com/problems/data-stream-as-disjoint-intervals/
class SummaryRanges:
    def __init__(self):
        self.num = list()
        self.v = [0] * 10002
        self.min_v = int(1e9)
        self.max_v = -1

    def addNum(self, value: int) -> None:
        self.num.append(value)
        self.v[value] = 1
        if value > self.max_v:
            self.max_v = value
        if value < self.min_v:
            self.min_v = value

    def getIntervals(self) -> List[List[int]]:
        self.res = list()
        temp = list()
        if not self.num:
            return self.res
        for i in range(self.min_v, self.max_v + 1):
            if i == 0 and self.v[0] == 1:
                temp.append(i)
            elif self.v[i - 1] == 0 and self.v[i] == 1:
                temp.append(i)
            if self.v[i + 1] == 0 and self.v[i] == 1:
                temp.append(i)
            if len(temp) == 2:
                self.res.append(temp)
                temp = []
        return self.res

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()