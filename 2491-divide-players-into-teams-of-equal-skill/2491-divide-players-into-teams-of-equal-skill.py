class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        # each players skill sum
        skillSum = skill[0] + skill[-1]
        
        # sum of the chemistry of all the teams
        chemistry = skill[0] * skill[-1]
        left, right = 1, len(skill) - 2

        while left < right:
            currSum = skill[left] + skill[right]
            
            # check if total skill of each teamis equal
            if skillSum != currSum:
                return -1
            
            chemistry += skill[left] * skill[right]
            left += 1
            right -= 1
            
        return chemistry