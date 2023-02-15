class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        n = len(barcodes)
        
        freq = Counter(barcodes)
        freq = sorted([(count, num) for num, count in freq.items()], reverse=True)
        
        result = [0] * n
        i = 0
        
        for count, num in freq:
            for _ in range(count):
                result[i] = num
                i += 2
                if i >= n:
                    i = 1
        
        return result