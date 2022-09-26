export function theatreSquare(m: number, n: number, flagSize: number) {
    return Math.ceil(m / flagSize) * Math.ceil(n / flagSize)
}