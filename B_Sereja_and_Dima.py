no_cards = int(input())


def playersSum(cards, length):
    player1 = 0
    player2 = 0

    left = 0
    right = length-1

    while left <= right:
        player1 += cards[left]
        player2 += cards[right]

        if left == right:
            player2 -= cards[right]

        left += 1
        right -= 1
    return ' '.join([str(player2), str(player1)])


cards = list(map(int, input().split()))
result = playersSum(cards, no_cards)
print(result)
