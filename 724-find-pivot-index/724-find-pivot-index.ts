function pivotIndex(nums: number[]): number {
let sum = 0;
    for (let i = 0; i < nums.length; i++){
        sum += nums[i]
    }
    
    let fromleft = 0;
    for (let i = 0; i < nums.length; i++){
        if (fromleft === sum - fromleft - nums[i]) {
            return i;
        }
        fromleft += nums[i]
    }
    return -1;
};