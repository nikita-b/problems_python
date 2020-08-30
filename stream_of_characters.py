# Implement the StreamChecker class as follows:
#
# - StreamChecker(words): Constructor, init the data structure with the given words.
# - query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to newest, including this letter just queried) spell one of the words in the given list.
# https://leetcode.com/problems/stream-of-characters/

from typing import List

# https://github.com/nikita-b/data_structure_and_algorithms_python/blob/master/Trees/trie.py


class TrieNode:
    def __init__(self, end: bool = False):
        self.children = {}
        self.end = end

    def add_child(self, key, node):
        self.children[key] = node

    def get_child(self):
        return self.children

    def is_end(self):  # Real drama!
        return self.end


class Trie:
    def __init__(self):
        """
        Create root node
        """
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current_node = self.trie

        for i in word:
            if i not in current_node.get_child():
                new_node = TrieNode()
                current_node.add_child(i, new_node)
            current_node = current_node.get_child()[i]
        current_node.end = True

    def search(self, word: str, starts_with: bool = False) -> bool:
        """
        Returns True if the word is in the trie and False otherwise
        """
        current_node = self.trie

        for i in word:
            if i in current_node.get_child():
                current_node = current_node.children[i]
                continue
            return False

        if not starts_with and not current_node.is_end():
            return False

        return True

    def starts_with(self, prefix: str) -> bool:
        """
        Returns True if there is any word in the trie that starts with the given prefix.
        """
        return self.search(prefix, True)


class StreamChecker:
    def __init__(self, words: List[str]):
        self.letters = ''
        self.t = Trie()
        for i in words:
            self.t.insert(i)

    def query(self, letter: str) -> bool:
        print(self.letters)
        self.letters += letter

        if not self.t.starts_with(self.letters):
            self.letters = self.letters[1:]

        if self.t.search(self.letters):
            return True

        return False