import textwrap

def wrap(string, max_width):
    result = []
    i = 0
    
    for ch in string:
        result.append(ch)
        i+=1
        if i%max_width==0:
            result.append('\n')
            i=0
    return ''.join(result)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)