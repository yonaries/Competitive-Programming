no_cards = int(input())


def serja_and_dima(cards):
    serja = 0
    dima = 0
    for i in range(len(cards)):
        if i % 2 == 0:
            serja += max(cards[0], cards[-1])
            cards.remove(max(cards[0], cards[-1]))
        else:
            dima += max(cards[0], cards[-1])
            cards.remove(max(cards[0], cards[-1]))
    print(serja, dima)


if __name__ == '__main__':
    cards = list(map(int, input().split()))
    serja_and_dima(cards)
