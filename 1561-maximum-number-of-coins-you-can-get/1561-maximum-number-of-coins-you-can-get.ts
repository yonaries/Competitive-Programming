function maxCoins(piles: number[]): number {
    let me = 0;
        piles.sort((a,b)=>a-b);
        for (let j = piles.length - 2, i = 0; i < j; i++, j -= 2)
            me += piles[j];
        return me;
};