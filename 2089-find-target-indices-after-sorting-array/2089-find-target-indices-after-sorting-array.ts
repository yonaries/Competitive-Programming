function targetIndices(nums: number[], target: number): number[] {
    const sorted = nums.sort((a, b) => a - b)
    const list: number[] = []
    sorted.forEach((num, index) => {
        if (num === target) list.push(index)
    })
    return list;
};