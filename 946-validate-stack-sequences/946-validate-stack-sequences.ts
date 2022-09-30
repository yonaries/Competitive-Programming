function validateStackSequences(pushed: number[], popped: number[]): boolean {
 const stack = []
    let i = 0

    for (const item of pushed) {
        stack.push(item)
        while (stack.length && stack[stack.length - 1] === popped[i]) {
            stack.pop()
            i++
        }
    }
    
    return pushed.length === i
};