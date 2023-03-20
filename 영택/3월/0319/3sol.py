# leetcode 211. Design Add and Search Words Data Structure
# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
class WordDictionary:
    def __init__(self):
        self.wd = defaultdict(set)

    def addWord(self, word: str) -> None:
        self.wd[len(word)].add(word)

    def search(self, word: str) -> bool:
        if "." in word:
            for w in self.wd[len(word)]:
                for i in range(len(word)):
                    if word[i] != "." and word[i] != w[i]:
                        break
                else:
                    return True
            else:
                return False
        else:
            return word in self.wd[len(word)]