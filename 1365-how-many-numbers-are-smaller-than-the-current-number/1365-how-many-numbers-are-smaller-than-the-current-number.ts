function smallerNumbersThanCurrent(nums: number[]): number[] {
    let arr = new Array(nums.length).fill(0)

    for (let i = 0; i < nums.length; i++) {
        for (let j = 0; j < nums.length; j++) {
            if (nums[i] > nums[j]) arr[i]++
        }
    }
    return arr;
};