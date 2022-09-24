/**
 Do not return anything, modify nums in-place instead.
 */
function sortColors(colors: number[]): void {
    //sorting colors using bubble sort
    for (let i = 0; i < colors.length; i++) {
        for (let j = 0; j < colors.length; j++) {
            if (colors[j] > colors[j + 1]) {
                let temp = colors[j]
                colors[j] = colors[j + 1]
                colors[j + 1] = temp
            }
        }
    }
    console.log(colors);
};