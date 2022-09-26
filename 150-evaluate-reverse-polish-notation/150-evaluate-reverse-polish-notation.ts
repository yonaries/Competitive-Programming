var evalRPN = function(tokens):number {
    let stack:number[] = [];
    
    for (let i = 0; i < tokens.length; i++) {
        const token = tokens[i]
        if (!isNaN(token)) 
            stack.push(parseInt(token));
        else {
            const num1 = stack.pop();
            const num2 = stack.pop();
            const result = calculate(num2, num1, token);
            stack.push(result);
        }
    }

    return stack.pop();
};

var calculate = function(num1, num2, operator) {
    switch(operator){
        case '+': return num1 + num2;
        case '-': return num1 - num2;
        case '/': return Math.trunc(num1 / num2);
        case '*': return num1 * num2;   
    }
};