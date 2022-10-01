function minPairSum(nums: number[]): number {
        nums.sort((a,b)=>a-b)
        let l = 0,r = nums.length-1;
        let res = 0;

        while (l<r) 
            res = Math.max(res, nums[l++] + nums[r--]);
        
        return res; 
};