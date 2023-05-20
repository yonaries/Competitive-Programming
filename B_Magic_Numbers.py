def is_magic_number(n):
    while n > 0:
        if n % 1000 == 144:
            n //= 1000
        elif n % 100 == 14:
            n //= 100
        elif n % 10 == 1:
            n //= 10
        else:
            return False
    return True


n = int(input())
if is_magic_number(n):
    print("YES")
else:
    print("NO")
