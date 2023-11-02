class TrieNode:
    def __init__(self):
        self.root = {}
    
    def insert(self, bits):
        trie = self.root
        for bit in bits:
            if bit not in trie:
                trie[bit] = {}
            trie = trie[bit]
    
    def findXOR(self, bits, num):
        trie = self.root
        output = ''
        zero, one = '0', '1'
        for bit in bits:
            if bit == zero and one in trie:
                output += one
                trie = trie[one]
            elif bit == one and zero in trie:
                output += zero
                trie = trie[zero]
            else:
                output += bit
                trie = trie[bit]
                
        return int(output, 2) ^ num

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:

        trie = TrieNode()
        ans = 0
        for num in nums:
            trie.insert("{:032b}".format(num))
        for num in nums:
            ans = max(ans, trie.findXOR("{:032b}".format(num), num))

        return ans