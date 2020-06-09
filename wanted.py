access = "akusayangharis"
password = input("Enter your password: ")
batas = "======================="

if password == access:
    import time
    time.sleep(2)
    print("ACCESS GRANTED")
    print(batas)
    time.sleep(0.3)
    print("Wanted criminals Badan Intelijen Tebet")
    time.sleep(0.3)
    print(batas)
    for y in range(1,4):
        time.sleep(1)
        dot = "."
        for x in range(0,4):
            print("Loading" + "." * x)
            time.sleep(0.5)
    print(batas)
    def criminals(dictionary):
        for key, val in dictionary.items():
            print(f"{key} : {val}")
    crim0 = {"Nama": "Budi", "umur": "23", "Tindakan Kriminal": "Perampokan bank"}
    crim1 = {"Nama": "Nepy", "umur": "21", "Tindakan Kriminal": "Pembocoran jaringan intel BIN"}
    crim2 = {"Nama": "Haris", "umur": "20", "Tindakan Kriminal": "Pencurian Semangka"}
    criminals(crim0)
    print(batas)
    criminals(crim1)
    print(batas)
    criminals(crim2)
    print(batas)
else:
    print("ACCESS DENIED")

