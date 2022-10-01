function productExceptSelf(nums: number[]): number[] {
        let n:number = nums.length;
        let res = new Array(n);
        let product:number = 1;
        let zeros:number = 0;
    
        nums.forEach(num => {
            product *= (num == 0 ? 1 : num);
            if (num == 0) zeros++;
        })
    
        for (let i = 0; i < n; i++)
            res[i] = nums[i] == 0 ? zeros > 1 ? 0 : product : zeros > 0 ? 0 : product/nums[i];
        
    return res;
};