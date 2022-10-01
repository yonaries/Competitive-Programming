function minSetSize(arr: number[]): number {
  const map = {};
    
  arr.forEach(num => map[num] = (map[num] || 0) + 1) 

  const freqs = new Array(arr.length + 1).fill(0);
    
  for(const num in map) {
    const freq = map[num];
    freqs[freq]++;
  }

  let ans = 0;
  let currentFreq = arr.length;
  let removed = 0;
    
  while (removed < arr.length / 2) {
    while (freqs[currentFreq] === 0) currentFreq--;

    removed += currentFreq;
    freqs[currentFreq]--;
    ans++;
  }

  return ans;
};