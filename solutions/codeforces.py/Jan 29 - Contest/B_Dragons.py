def fightDragon(strength, dragons):
    dragons.sort()
    for dragonStrength, bonus in dragons:
        if strength <= dragonStrength:
            return 'NO'
        strength += bonus
    return 'YES'


strength, n = list(map(int, input().split()))
dragons = []
for i in range(n):
    dragonStrength, bonus = map(int, input().split())
    dragons.append((dragonStrength, bonus))
print(fightDragon(strength, dragons))
