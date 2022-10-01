function topKFrequent(nums: number[], k: number): number[] {
    const numFreq = new Map();

    nums.forEach(num =>  {
        numFreq.set(num, numFreq.get(num) + 1 || 1)
    })
    const sortedFreqs = [...numFreq.entries()].sort((a, b) => b[1] - a[1]);
    
    return sortedFreqs.slice(0, k).map((x) => x[0]);
};