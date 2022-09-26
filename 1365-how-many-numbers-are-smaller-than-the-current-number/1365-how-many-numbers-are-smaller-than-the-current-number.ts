function smallerNumbersThanCurrent(nums: number[]): number[] {
let arr: number[] = []
    //assigning 0 to every index of the result array
    for (let i = 0; i < nums.length; i++) {
        arr[i] = 0;
    }
    //compare current number with others
    for (let i = 0; i < nums.length; i++) {
        for (let j = 0; j < nums.length; j++) {
            if (nums[i] > nums[j]) arr[i]++
        }
    }
    return arr;
};