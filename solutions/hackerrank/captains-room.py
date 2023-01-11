# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    N = int(input())
    roomsList = input().split()
    result = {}
    
    for i in range(0,len(roomsList)):
        val = result.get(roomsList[i])
        
        if val:
            result[roomsList[i]] = val + 1
        else:
            result[roomsList[i]] = 1
    
    key_list = list(result.keys())
    val_list = list(result.values())
    position = val_list.index(1)
    print(key_list[position])