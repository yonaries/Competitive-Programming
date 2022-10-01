function kthLargestNumber(nums: string[], k: number): string {
    let n = nums.length;
    let key, j;
    
    for(let i = 1; i<n;i++) {
      key = BigInt(nums[i]);
      j = i - 1;
      
      while(j >= 0 && BigInt(nums[j]) > key) {
        nums[j + 1] = nums[j];
          j--;
      }
      nums[j + 1] = key;
        
  }
  return `${nums[n-k]}`;
    
};