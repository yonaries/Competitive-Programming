function longestOnes(nums: number[], k: number): number {
    let left = 0, right = 0;
    while (right < nums.length){
        if (!nums[right++]) k--
        if (k < 0)    
            if (!nums[left++]) k++
        
    }
    return right-left
};