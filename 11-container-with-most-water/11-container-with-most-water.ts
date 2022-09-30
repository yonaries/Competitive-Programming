function maxArea(height: number[]): number {
  let min = 0;
  let max = 0;
  let left = 0,
    right = height.length - 1;
    
    while (left < right) {
        max = Math.max(max, (right - left) * Math.min(height[left], height[right]));
        height[left] < height[right] ? left++ : right--;
    }
    return max;

};