function maxOperations(nums: number[], k: number): number {
      nums.sort((a,b) => a - b);
        let i = 0, j = nums.length - 1;
        let count = 0;
        
        while(i < j){
            if(nums[i] + nums[j] == k){
                count++;
                i++;
                j--;
            } 
            else if(nums[i] + nums[j] < k) i++;
            else j--;
        }
        return count;
};