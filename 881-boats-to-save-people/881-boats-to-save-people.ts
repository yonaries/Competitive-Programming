function numRescueBoats(people: number[], limit: number): number {
    people.sort((a, b) => a - b)
    let high = people.length - 1
    let least = 0
    let boats = 0

    while (least <= high) {
        if (people[least] + people[high] <= limit) {
            least++
            high--
        } else high--
        boats++
    }
    return boats
        
};