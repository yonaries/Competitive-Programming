function rearrangeArray(nums: number[]): number[] {
    let arr = [], res = []
    nums.forEach(item => arr[item] = 1)
    
    let l = 0, r = arr.length - 1
    while(l <= r){
        while(!arr[l]) l++
        while(!arr[r]) r--
        if(l <= r)res.push(l++)
        if(l <= r)res.push(r--)
    }
    return res
};