class Solution:
    def addLeadingZeros(self, bits):
        remaining = 32 - len(bits)
        return '0' * remaining + bits
        
    def reverseBits(self, n: int) -> int:
        bits = bin(n)[2:]
        bits = self.addLeadingZeros(bits)
        
        bits_reversed = ''
        
        for i in range(len(bits)-1, -1, -1):
            bits_reversed += bits[i]
        
        return int(bits_reversed, 2)