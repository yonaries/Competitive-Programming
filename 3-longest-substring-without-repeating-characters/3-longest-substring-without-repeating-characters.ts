function lengthOfLongestSubstring(s: string): number {
    let myset = [];
    let substr_length:number = 0;
    
    for (let i:number = 0; i < s.length; i++) {
        if(myset.includes(s[i])){
        myset.splice(0, myset.indexOf(s[i]) + 1)
        myset.push(s[i]);
    } else myset.push(s[i]);

    substr_length = myset.length  > substr_length ? myset.length : substr_length;
    }
    return substr_length
    
    
    
};