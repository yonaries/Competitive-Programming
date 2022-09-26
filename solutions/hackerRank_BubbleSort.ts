export function hackerRankBubbleSort(a: number[]): void {
    let swapTimes = 0;
    for (let i = 0; i < a.length; i++) {
        for (let j = 0; j < a.length; j++) {
            if (a[j] > a[j + 1]) {
                let temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
                swapTimes++;
            }
        }
    }

    console.log(`Array is sorted in ${swapTimes} swaps.`);
    console.log(`First Element: ${a[0]}`);
    console.log(`Last Element: ${a[(a.length - 1)]}`);

}