export function hackerRank_countingSort(arr: number[]): number[] {
    const result = new Array(100).fill(0)

    arr.forEach(num => result[num]++)
    return result
}