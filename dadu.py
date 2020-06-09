import time
import random
batas = "======================="
print(batas)
print("Dice Roller Sim")
print(batas)

while True:
    jmlh = int(input("Berapa jumlah dadu: "))
    for x in range(1, jmlh+1):
        dadu = random.randint(1,7)
        print(f"Dadu {x} yang anda lempar: {dadu}")
        time.sleep(0.5)
    nanya = input("Apakah anda ingin mencoba lagi? (y/n): ")
    if nanya == "y":
        continue    
    elif nanya == "n":
        print("Terima kasih!")
        break
    else:
        print("ERROR!\nTRY AGAIN!") 