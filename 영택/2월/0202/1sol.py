# leetcode 953. Verifying an Alien Dictionary
# https://leetcode.com/problems/verifying-an-alien-dictionary/description/
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        my_dict = {char: idx for idx, char in enumerate(order)}

        for word1, word2 in zip(words, words[1:]):
            if len(word1) > len(word2) and word1[:len(word2)] == word2:
                return False
            for s1, s2 in zip(word1, word2):
                if my_dict[s1] < my_dict[s2]:
                    break
                elif my_dict[s1] > my_dict[s2]:
                    return False

        return True