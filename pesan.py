foods = ["nasi", "kangkung", "telur asin", "ayam goreng"]
print("Berikut makanan yang anda pesan: ")

for n in range(len(foods)):
    print(n, foods[n])
while True:
    nanya = input("ada lagi yang ingin anda pesan? (y/n): ")
    if nanya == "y":
        foods.append(input("apa yang ingin anda pesan?: "))
    elif nanya == "n":
        print("Baik, saya ulang pesanan anda ya...")
        for n in range(len(foods)):
            print(n, foods[n])
        print("itu saja ya? Baik, mohon ditunggu...")
        break
    else:
        print("ERROR!\nTRY AGAIN!")