export function dominoPiling(m: number, n: number) {
    const dominoSize = 2 * 1
    const boardSize = m * n

    return Math.floor(boardSize / dominoSize)
}