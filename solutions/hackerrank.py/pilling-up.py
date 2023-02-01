# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())

for _ in range(T):
    num, cubes = int(input()), list(map(int,input().split()))
    answer = "Yes"
    
    while len(cubes) > 1:
        if cubes[0] >= cubes[-1]:
            larger_num = cubes[0]
            cubes.pop(0)     
        else:
            larger_num = cubes[-1]
            cubes.pop(-1)  
            
        if larger_num < cubes[0] or larger_num < cubes[-1]:
            answer = 'No'
            break
            
    print(answer)