if __name__ == '__main__':
    N = int(input())
    result = {}
    
    for i in range(0,N):
        input_str = input()
        val = result.get(input_str)
        
        if val:
            result[input_str] = val + 1
        else:
            result[input_str] = 1
            
    print(len(result))
    print(*result.values())