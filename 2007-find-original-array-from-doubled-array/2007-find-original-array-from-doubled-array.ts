function findOriginalArray(changed: number[]): number[] {
    if(changed.length % 2 !== 0) 
		return [];
		
	changed.sort((a, b) => a - b);
    
	const result = [], queue = []
    let i = 0;
    
	for (const num of changed) {
        if (queue.length > 0 && queue[0] === num)
            result[i++] = queue.shift() / 2;
        else 
			queue.push(num * 2);
    }
	
    return queue.length > 0 ? [] : result;
};