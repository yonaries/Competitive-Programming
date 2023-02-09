class Solution:
    def maxArea(self, height: List[int]) -> int:
        minimum, maximum, left = 0,0,0
        right = len(height) - 1;
    
        while (left < right):
            maximum = max(maximum, (right - left) * min(height[left], height[right]));
            if (height[left] < height[right]):
                left +=1 
            else:
                right -=1

        return maximum;