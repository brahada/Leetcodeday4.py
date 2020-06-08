class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        for i in range(len(word)):
            if word[:i] in self.dic:
                continue
            self.dic[word[:i]] = 1
        self.dic[word] = 2

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return word in self.dic and self.dic[word] == 2

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return prefix in self.dic
