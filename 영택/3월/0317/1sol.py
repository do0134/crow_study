# leetocde 208. Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/description/

class Trie:

    def __init__(self):
        self.try_dict = defaultdict(bool)

    def insert(self, word: str) -> None:
        self.try_dict[word] = True

    def search(self, word: str) -> bool:
        if self.try_dict[word]:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        key = self.try_dict.keys()
        for i in key:
            if i[0:len(prefix)] == prefix and self.try_dict[i]:
                return True
        else:
            return False