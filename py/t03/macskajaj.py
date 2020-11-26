def nyertes_korok(own, other):
    if len(own) != len(other) or (len(own) == 0 and len(other) == 0):
        return -1

    won = 0
    for i in range(0, len(own)):
        if own[i] > other[i]:
            won += 1

    return won