class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefixCount = 0
        
        
class MapSum:  

    def __init__(self):
        self.root = TrieNode()
        self.dic = {}

    def insert(self, key: str, val: int) -> None: 
        delta = val
        if key in self.dic:
            delta = val - self.dic[key]
            
        self.dic[key] = val
        cur = self.root
        
        for char in key:
            if char not in cur.children:
                cur.children[char] = TrieNode()
                
            cur = cur.children[char]
            cur.prefixCount += delta
        
    def sum(self, prefix: str) -> int:
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        return cur.prefixCount
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)