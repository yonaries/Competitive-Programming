function reverseParentheses(s: string): string {
    let stack:string[] = []
    const str = s.split('');
    
    for(let crr of str){
        if(crr === ')'){
            var letter = stack.pop();
            let temp = []
            
            while(letter !== '('){
                temp.push(letter);
                letter = stack.pop();
            }
            stack = stack.concat(temp);
            
        }else stack.push(crr)

    }
    return stack.join('');
};