function maxSumTwoNoOverlap(nums: number[], firstLen: number, secondLen: number): number {
    let len = nums.length;
    for(let i = 1; i < len; i++) {
        nums[i] += nums[i - 1];
    }
    
    let LMax = nums[firstLen - 1], MMax = nums[secondLen - 1];
    let res = nums[secondLen + firstLen - 1];
    for(let i = secondLen + firstLen ; i < len ; i++) {
        LMax = Math.max(LMax, nums[i - secondLen ] - nums[i - secondLen - firstLen]);
        MMax = Math.max(MMax, nums[i - firstLen ] - nums[i - secondLen - firstLen]);
        res = Math.max(res,
            LMax + nums[i] - nums[i - secondLen],
            MMax + nums[i] - nums[i - firstLen]
        )
    }
    return res;
};