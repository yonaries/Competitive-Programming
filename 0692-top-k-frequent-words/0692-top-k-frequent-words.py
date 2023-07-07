class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq_words = defaultdict(int)
        
        for i in words:
            freq_words[i] = freq_words.get(i, 0) + 1
        
        maxHeap = []
        for key, val in freq_words.items():
            heappush(maxHeap, [-val, key])
        
        result = []
        for _ in range(k):
            val, key = heappop(maxHeap)
            result.append(key)
            
            
        return result