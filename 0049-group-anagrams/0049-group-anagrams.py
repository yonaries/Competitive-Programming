class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        
        for string in strs:
            count = [0 for _ in range(26)]
            
            for char in string:
                index = ord(char) - ord('a')
                count[index] = count[index] + 1
                
            for i in range(len(count)):
                count[i] = str(count[i])
                
            key = '-'.join(count)

            if key not in res:
                res[key] = [string]
            else:
                res[key] = res[key] + [string]
            
        answer = []
        for key in res:
            answer.append(res[key])
        
        return answer
            
                    