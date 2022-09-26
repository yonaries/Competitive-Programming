export function countingValleys(steps: number, path: string): number {
    const pathStr = path.split('')
    let level = 0; //current location of hikers compared to sea level
    let traverse = 0;

    pathStr.forEach((step, index) => {
        if (level == 0 && pathStr[index].toLowerCase() == 'd') {
            level--
            traverse++
        }
        else if (step.toLocaleLowerCase() === 'd') level--
        else level++
    })
    return traverse
}