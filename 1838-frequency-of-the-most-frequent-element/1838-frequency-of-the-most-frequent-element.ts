function maxFrequency(nums: number[], k: number): number {
        nums.sort((a,b)=> a - b);
        let n = nums.length, sum = 0, ct = 1, end = n - 1, maxfreq = 1;
        let front = end - 1;
    
        while(front >= 0)
        {
            sum += nums[end] - nums[front];
            if(sum <= k)
            {
                ct++;
                maxfreq = Math.max(ct,maxfreq);
                front--;
            }
            else
            {
                let size = 1;
                while(sum > k)
                {
                    while(end > 0 && nums[end] == nums[end - 1]) end--; //for duplicate elements
                    if(end > 0)
                        end--;
                    let diff = nums[end + 1] - nums[end];
                    size = end - front + 1;
                    sum = sum - size*diff;
                }
                ct = size;
                front--;
               
             }
        
        }
        return maxfreq;
};