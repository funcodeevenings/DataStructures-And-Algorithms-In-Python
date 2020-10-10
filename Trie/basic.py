class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def getNode(self):
        return TrieNode()

    def _charToIndex(self,ch):
        return ord(ch)-ord('a')

    def insert(self,key):
        ptr=self.root
        l=len(key)
        for i in range(l):
            index=self._charToIndex(key[i])
            if not ptr.children[index]:
                ptr.children[index]=self.getNode()
            ptr=ptr.children[index]
        
        ptr.isEndOfWord=True
    
    def search(self,key):
        ptr=self.root
        l=len(key)
        for i in range(l):
            index=self._charToIndex(key[i])
            if not ptr.children[index]:
                return False
            ptr=ptr.children[index]
        if ptr and ptr.isEndOfWord:
            return True
        return False

    def preorder(self):
        pass

    def remove(self,key):
        pass

    def printAutoSuggestion(self,key):
        pass

    def countWords(self):
        pass
    
    

keys = ["the","a","there","anaswe","any","by","their"]
t=Trie()
for key in keys:
    t.insert(key)

print(t.search("there"))
print(t.search("ther"))
print(t.search("answer"))