/**
 Do not return anything, modify nums in-place instead.
 */
function rotate(nums: number[], k: number): void {
    while(k > 0){
        const last = nums.pop()
        nums.unshift(last)
        k--
    }
};