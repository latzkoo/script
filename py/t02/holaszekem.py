def szekem(current):
    side = "bal" if ((int(-(-(current / 7) // 1))) % 2) == 0 else "jobb"

    position = 7 if current % 7 == 0 else current % 7
    position = 8 - position if side == "jobb" else position

    return str(int(-(-(current / 14) // 1))) + ". sor, " + side + " " + str(position) + ". szek"