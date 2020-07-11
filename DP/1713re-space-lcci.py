class Solution:
    # O(n^2), O(n)
    def respace(self, dictionary: List[str], sentence: str) -> int:
        dic = {}.fromkeys(dictionary)
        N = len(sentence)
        dp = [0] * (N + 1)
        for i in range(1, N + 1):
            # sentence[j:i]
            dp[i] = dp[i - 1] + 1
            for j in range(i):
                if sentence[j:i] in dic:
                    dp[i] = min(dp[i], dp[j])

        return dp[-1]

    # O(mn), O(n)
    def respace1(self, dictionary: List[str], sentence: str) -> int:
        N = len(sentence)
        dp = [0] * (N + 1)
        for i in range(1, N + 1):
            dp[i] = dp[i - 1] + 1
            for j in range(len(dictionary)):
                length = len(dictionary[j])
                if length <= i and sentence[i - length:i] == dictionary[j]:
                    dp[i] = min(dp[i], dp[i - length])

        return dp[-1]

    # Trie to prune matching
    _end = '__end__'

    class Trie:
        def __init__(self):
            self.root = {}

        def make_trie(self, *words):
            root = self.root
            for word in words:
                current_dict = root
                # insert in reverse order of the word
                for i in range(len(word) - 1, -1, -1):
                    current_dict = current_dict.setdefault(word[i], {})
                current_dict[_end] = True

        # def in_trie(self, word):
        #     current_dict = self.root
        #     for i in range(len(word)-1, -1, -1):
        #         current_dict = current_dict.get(word[i], None)
        #         if not current_dict:
        #             return False
        #     return current_dict.get(_end, False)

        # def insert(self, word):
        #     current_dict = self.root
        #     for i in range(len(word)-1, -1, -1):
        #         current_dict = current_dict.setdefault(word[i], {})
        #     current_dict[_end] = True

        # def remove(self, word):
        #     current_dict = self.root
        #     for i in range(len(word)-1, -1, -1):
        #         current_dict = current_dict.get(word[i], None)
        #         if not current_dict:
        #             return
        #     current_dict[_end] = False

    class Solution:
        def respace(self, dictionary: List[str], sentence: str) -> int:
            len_sentence = len(sentence)
            t = Trie()
            # unpack
            t.make_trie(*dictionary)
            dp = list(range(len_sentence + 1))
            for i in range(1, len_sentence + 1):
                dp[i] = dp[i - 1] + 1
                flag = False
                current_dict = t.root
                for j in range(i - 1, -1, -1):
                    current_dict = current_dict.get(sentence[j], None)
                    if current_dict is None:
                        break
                    elif current_dict.get(_end, False):
                        dp[i] = min(dp[i], dp[j])
            return dp[len_sentence]
