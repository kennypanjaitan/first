user1 = "harrisxoxo"
pasw1 = "12345"
access = int(3)
print(f"Anda memiliki kesempatan mencoba {access} kali!")
while access > 0:
    user = str(input("Enter username: "))
    pas = str(input("Enter password: "))
    if user == user1 and pas == pasw1:
        print("ACCESS GRANTED")
        break
    else:
        access -= 1
        print(f"ACCES DENIED!\nAnda memiliki kesempatan mencoba {access} kali lagi!")