lah = "ERROR!\nCOBA LAGI!"
while True:
    try:
        num1 = int(input("angka pertama : "))
        num2 = int(input("angka kedua : "))
        operator = int(input("1 = tambah\n2 = kurang\n3 = kali\n4 = bagi\n5 = pangkat\n0 = Selesai\nApa yang ingin anda lakukan?: "))

    except ValueError:
        print(lah)
    except:
        pass
    else:
        if operator == 1:
            print(num1 + num2)
        elif operator == 2:
            print(num1 - num2)
        elif operator == 3:
            print(num1 * num2)
        elif operator == 4:
            print(num1 / num2)
        elif operator == 5:
            print(num1 ** num2)
        elif operator == 0:
            print("Terima Kasih!")
            break
        else:
            print(lah)
    finally:
        lagi = input("Lagi?(y/n): ")
        if lagi == "y":
            print("OKAY!")
        elif lagi == "n":
            print("Terima Kasih!")
            break
        else:
            print(lah)



