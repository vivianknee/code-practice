class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        # compare the character to the child key
        # make sure the endofnode is the last char
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False

        # at this point the word either exists or is part of a word
        if curr.endOfWord == True:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        # compare the character to the child key
        # make sure the endofnode is the last char
        for c in prefix:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return True
        
        