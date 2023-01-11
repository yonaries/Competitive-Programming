if __name__ == '__main__':
    N = int(input())
    result = []
    for i in range(0,N):
        input_str = input()
        elements = input_str.split()
        
        if elements[0] == 'insert':
            result.insert(int(elements[1]),int(elements[2]))
        elif elements[0] == 'remove':
            result.remove(int(elements[1]))
        elif elements[0] == 'append':
            result.append(int(elements[1]))
        elif elements[0] == 'pop':
            result.pop()
        elif elements[0] == 'print':
            print(result)
        elif elements[0] == 'sort':
            result.sort()
        elif elements[0] == 'reverse':
            result.reverse()
