def blackjack(n1, n2, n3):
    result = n1 + n2 + n3

    if result <= 21:
        return result
    elif n1 == 11 or n2 == 11 or n3 == 11:
        result = result - 10
        if result <= 21:
            return result
        else:
            return 'BUST'
    else:
        return 'BUST'

n = list(map(int, input("Enter three numbers ").split()))

print(blackjack(n[0], n[1], n[2]))


