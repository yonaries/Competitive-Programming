function subarraySum(nums: number[], k: number): number {
    if (!nums || nums.length === 0) return -1;
    
    let result = 0;
    const map: Map<number, number> = new Map();
    map.set(0, 1);
    
    for (let i = 0; i < nums.length; i++) {
        nums[i] += i > 0 ? nums[i-1] : 0;
        const prefixSum = nums[i];
        const diff = prefixSum - k;
        
        if (map.has(diff)) {
            result += map.get(diff);
        }
        
        // Record to HashMap
        if (map.has(prefixSum)) {
            map.set(prefixSum, map.get(prefixSum) + 1);
        } else {
            map.set(prefixSum, 1);
        }
    }
    return result;
};