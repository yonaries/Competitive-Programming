function validateStackSequences(pushed: number[], popped: number[]): boolean {
 const stack = []
    let i = 0

   pushed.forEach( item => {
        stack.push(item)
        while (stack.length && stack[stack.length - 1] === popped[i]) {
            stack.pop()
            i++
        }
    })
    
    return pushed.length === i
};