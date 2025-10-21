def mask(card):
    result = ""
    length = len(card)
    for i in range (0, length-4):
        if card[i] != "-" and card[i] != " ":
            result += "*"

        else:
            result += card[i]

    result += card[-4:]
    return result
