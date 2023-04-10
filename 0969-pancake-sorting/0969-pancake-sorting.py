class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        original = arr[:]
        arr.sort(reverse=True)
        
        result = []
        j = len(arr)
        
        for n in arr:
            i = original.index(n)
            
            original[:i + 1] = reversed(original[:i + 1])
            result.append(i + 1)
            result.append(j)
            
            original[:j] = reversed(original[:j])
            j -= 1
            
        return result