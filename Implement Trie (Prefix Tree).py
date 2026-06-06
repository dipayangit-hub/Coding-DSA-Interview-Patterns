class TrieNode:
     def __init__(self,isword=False):
          self.children=[None]*26
          self.isword=isword

class Trie:
    root=None
    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        node=self.root
        for ch in word:
            index=ord(ch)-ord('a')
            if not node.children[index]:
                node.children[index]=TrieNode()
            node=node.children[index]
        node.isword=True
        
            

    def search(self, word: str) -> bool:
        node=self.root
        for ch in word:
            index=ord(ch)-ord('a')
            if not node.children[index]:
                return False
            node= node.children[index]
        return node.isword

    def startsWith(self, prefix: str) -> bool:
        node=self.root
        for ch in prefix:
            index=ord(ch)-ord('a')
            if not node.children[index]:
                return False
            node= node.children[index]
        return True
    

trie=Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))