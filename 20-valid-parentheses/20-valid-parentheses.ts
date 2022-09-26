function isValid(s: string): boolean {
    const opened: string[] = []

    for (let i = 0; i < s.length; i++) {
        const top = opened[opened.length - 1]
        const brc = s[i]
        
        if (brc === '(' || brc === '[' || brc === '{') opened.push(brc)
        else if (brc === ')' && top === '(') opened.pop()
        else if (brc === ']' && top === '[') opened.pop()
        else if (brc === '}' && top === '{') opened.pop()
        else return false
    }

    return (opened.length === 0) ? true : false
};
