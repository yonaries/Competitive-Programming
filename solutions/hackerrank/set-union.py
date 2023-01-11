eng = int(input())
eng_sub = set(input().split())
french = int(input())
french_sub = set(input().split())
 
print(len(eng_sub.union(french_sub)))