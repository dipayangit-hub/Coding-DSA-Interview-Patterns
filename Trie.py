class Trie(object):

    def __init__(self):
        self.root=Node()


    def insert(self, word):
        node=self.root #starting with root node
        #Traversing characters
        for ch in word:
            index=ord(ch)-ord('a')
            if not node.children[index]:
                node.children[index]=Node()
            #Moving Node to child
            node=node.children[index]

        #Make Last Node True
        node.isEnd=True
        node.word=word
        

    def search(self, word):
        node=self.root #starting with root node
        #Traversing characters
        for ch in word:
            index=ord(ch)-ord('a')
            #If not None, continue to children else return False
            if node.children[index]:
                node=node.children[index]
            else:
                return False
        #Check if its end, then its full word
        return node.isEnd
        

    def startsWith(self, prefix):
        node=self.root #starting with root node
        #Traversing characters
        for ch in prefix:
            index=ord(ch)-ord('a')
            #If not None, continue to children else return False
            if node.children[index]:
                node=node.children[index]
            else:
                return False
        return True
 
    def getSuggestions(self,prefix):
        node=self.root #starting with root node
        #Traversing characters
        for ch in prefix:
            index=ord(ch)-ord('a')
            #If not None, continue to children else return False
            if node.children[index]:
                node=node.children[index]
            else:
                return []
        
        res=[]
        def dfs(node,res):
            if not node:
                return res
            if node.isEnd:
                res.append(node.word)
            for child in node.children:
                dfs(child,res)
            return res
        
        return dfs(node,res)
                
class Node(object):
    def __init__(self):
        self.children=[None for _ in range(26)]
        self.isEnd=False
        #Storing the word at the last character
        self.word=""

# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("cat")
trie.insert("car")
trie.insert("cart")
print(trie.getSuggestions("ca"))
# trie.insert("apple")
# print(trie.search("apple"))
# print(trie.search("apila"))
# print(trie.search("app"))    
# print(trie.startsWith("app"))
# trie.insert("app")
# print(trie.search("app"))  
