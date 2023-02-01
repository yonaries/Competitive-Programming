# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n_m = input().split()
    el_list = input().split()
    
    set_a = set(input().split())
    set_b = set(input().split())
    
    n = n_m[0]
    happiness = 0
    
    for i in range(0,int(n)):
        if set([el_list[i]]).issubset(set_a):
            happiness += 1
            
        elif set([el_list[i]]).issubset(set_b):
            happiness -= 1
    print(happiness)