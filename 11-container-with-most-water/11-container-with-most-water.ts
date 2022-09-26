function maxArea(height: number[]): number {
  let min = 0;
  let max = 0;
  let l = 0,
    r = height.length - 1;
    
    while (l < r) {
        max = Math.max(max, (r - l) * Math.min(height[l], height[r]));
        height[l] < height[r] ? l++ : r--;
    }
    return max;

};