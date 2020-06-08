class Trie:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.s = set()

	def insert(self, word: str) -> None:
		"""
		Inserts a word into the trie.
		"""
		self.s.add(word)

	def search(self, word: str) -> bool:
		"""
		Returns if the word is in the trie.
		"""
		return word in self.s

	def startsWith(self, prefix: str) -> bool:
		"""
		Returns if there is any word in the trie that starts with the given prefix.
		"""
		for i in self.s:
			if i.startswith(prefix):
				return True
