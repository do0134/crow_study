# leetcode 472. Concatenated Words
# https://leetcode.com/problems/concatenated-words/
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def word_in_list(target_word, word_arr):
            if target_word in word_arr:
                return True

            for i in range(len(target_word), 0, -1):
                if target_word[:i] in word_arr and word_in_list(target_word[i:], word_arr):
                    return True
            return False

        answer = list()
        words_set = set(words)

        for word in words:
            words_set.remove(word)
            if word_in_list(word, words_set):
                answer.append(word)
            words_set.add(word)
        return answer