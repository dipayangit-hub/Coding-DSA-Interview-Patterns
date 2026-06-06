class CharNode:
     def __init__(self,isword=False):
          self.children=[None]*26
          self.isword=isword

class WordDictionary:
    root=None
    def __init__(self):
        self.root=CharNode()

    def addWord(self, word: str) -> None:
        node=self.root
        for ch in word:
            index=ord(ch)-ord('a')
            if not node.children[index]:
                node.children[index]=CharNode()
            node=node.children[index]
        node.isword=True

    def search(self, word: str) -> bool:
        def searchhelper(node,word):
            for i in range(len(word)):
                ch=word[i]
                if ch=='.':
                    for c in node.children:
                        if c and searchhelper(c,word[i+1:]):
                            return True
                    return False
                index=ord(word[i])-ord('a')
                if not node.children[index]:
                    return False
                node= node.children[index]
            return node.isword
        node=self.root
        return searchhelper(node,word)

wd=WordDictionary()
wd.addWord("bcd")
wd.addWord("baa")
# wd.addWord("dad")
# wd.addWord("mad")
# print(wd.search("pad"))
# print(wd.search("bad"))
# print(wd.search("b.d"))
print(wd.search("b.."))
             