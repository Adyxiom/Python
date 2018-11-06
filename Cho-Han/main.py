import random


def main(totalv, totald, rowv, rowd):
    even = {2, 4, 6, 8, 10, 12}
    cho = input("Cho or Han : ")
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    d = d1 + d2
    print("Dice =", d)
    if "Cho" in cho:
        if d in even:
            win(totalv, totald, rowv, rowd)
        else:
            loose(totalv, totald, rowv, rowd)
    if "Han" in cho:
        if d in even:
            loose(totalv, totald, rowv, rowd)
        else:
            win(totalv, totald, rowv, rowd)
    print("Wrong input (Cho or Han)")
    print("---------------------------------------------------")
    main(totalv, totald, rowd, rowv)


def win(totalv, totald, rowv, rowd):
    totalv += 1
    rowv += 1
    rowd = 0
    print("You win !")
    print("You have", totalv, "victories !")
    print("You have", rowv, "victories in a row !")
    print("---------------------------------------------------")
    main(totalv, totald, rowv, rowd)


def loose(totalv, totald, rowv, rowd):
    totald += 1
    rowd += 1
    rowv = 0
    print("You loose...")
    print("You have", totald, "defeats...")
    print("You have", rowd, "defeats in a row...")
    print("---------------------------------------------------")
    main(totalv, totald, rowv, rowd)


if __name__ == '__main__':
    print("Welcome to the best dice game ever !\nChoose Cho(even) or Han(odd) !")
    main(0, 0, 0, 0)
