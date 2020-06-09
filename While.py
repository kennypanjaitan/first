import random
ans = random.randint(1,10)



while True:
    jwb = int(input("Pilih dari 1 - 10: "))
    if jwb < ans:
        print("kekecilan")
    if jwb > ans:
        print("kegedean")
    if jwb == ans:
        print("Kamu Berhasil!1!")
        break