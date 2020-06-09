import random
import time
batas = "======================="
print(batas)
print("SUIT COMPETITION\nHUMAN VS COMPUTER")
print(batas)

#
def computer(comp, komp):
    if comp == 1:
        return komp == "Gunting"
    elif comp == 2:
        return komp == "Kertas"
    else:
        return komp == "Batu"

def hasil(user, komp):
    if user == "Gunting":
        if komp == "Gunting":
            print("Tie!")
        elif komp == "Kertas":
            print("You Win!")
        else:
            print("You Lose!")
    elif user == "Batu":
        if komp == "Gunting":
            print("You Win!")
        elif komp == "Kertas":
            print("You Lose")
        else:
            print("Tie!")
    elif user == "Kertas":
        if komp == "Gunting":
            print("You Lose!")
        elif komp == "Kertas":
            print("Tie!")
        else:
            print("You Win!")

while True:
    computer(comp = random.randint(1,4), komp =)
    user = input("Gunting/Batu/Kertas?: ")
    print(f"{user} vs {komp}")
    time.sleep(1.5)
    print(hasil)
    lagi = input("Play again? (y/n)")
    if lagi == "y":
        continue
    elif lagi == "n":
        print("See you!")
        break
    break
