function kClosest(points: number[][], k: number): number[][] {
    let dist = [];
    for (let i = 0; i < points.length; i++) {
        dist.push([Math.sqrt(points[i][0] ** 2 + points[i][1] ** 2), i]);
    }
    
    dist.sort((a, b) => a[0] - b[0]);
    
    let res = [];
    for (let i = 0; i < k; i++) {
        res.push(points[dist[i][1]]);
    }
    
    return res;
};