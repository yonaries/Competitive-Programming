/**
 Do not return anything, modify nums in-place instead.
 */
function moveZeroes(nums: number[]): void {
    let zeros = 0;
    let j = 0;
    
    for(let i = 0; i < nums.length; i++){
            if(nums[i] == 0){
                zeros++;
            }
            else{
                nums[j] = nums[i];
                j++;
            } 
        }

        for(let i = 0; i < zeros; i++){
            nums[j++] = 0;
        }
};