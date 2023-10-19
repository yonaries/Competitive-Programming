class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        
        for num in nums:
            count[num] += 1
            
        sorted_dict = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        sorted_list = [(key, value) for key, value in sorted_dict.items()]
        only_keys = [t[0] for t in sorted_list]
        
        return only_keys[:k]
        