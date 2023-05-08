class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0 
        right = 0
        
        windowSize = 0
        hashMap = {}

        while(right < len(fruits)):
            hashMap[fruits[right]] = hashMap.get(fruits[right],0)+1
            
            while(len(hashMap) > 2):
                hashMap[fruits[left]] = hashMap.get(fruits[left])-1
                
                if(hashMap.get(fruits[left]) == 0):
                    del hashMap[fruits[left]]
                    
                left += 1

            windowSize = max(windowSize,right-left+1)
            right += 1
            
        return windowSize