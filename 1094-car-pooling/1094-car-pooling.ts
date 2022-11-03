function carPooling(trips: number[][], capacity: number): boolean {
let range = 0
    trips.forEach(t => range = Math.max(range,t[2]));
    let arr = new Array(range+1).fill(0);
    trips.forEach((t,i) => {
        arr[t[2]] -= t[0];
        arr[t[1]] += t[0];
    })
    let cur = 0;
    for(let i = 0; i <= range; i++) {
        cur += arr[i];
        if(cur > capacity) return false;
    }
    return true;
};