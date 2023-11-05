class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i=1
        while i**2<=num:
            if i**2<num: i+=1
            if i**2==num: return True
        return False