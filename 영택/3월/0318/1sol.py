# leetcode1472. Design Browser History
# https://leetcode.com/problems/design-browser-history/description/
class BrowserHistory:

    def __init__(self, homepage: str):
        self.idx = 0
        self.v = deque()
        self.v.append(homepage)
        self.idx += 1

    def visit(self, url: str) -> None:
        while len(self.v) - 1 > self.idx:
            self.v.pop()
        self.v.append(url)
        self.idx = len(self.v) - 1

    def back(self, steps: int) -> str:
        if self.idx < steps:
            self.idx = 0
            return self.v[0]

        self.idx -= steps
        return self.v[self.idx]

    def forward(self, steps: int) -> str:
        if steps + self.idx > len(self.v) - 1:
            self.idx = len(self.v) - 1
            return self.v[-1]
        self.idx += steps
        return self.v[self.idx]