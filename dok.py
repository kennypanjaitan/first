def doc(dictionary):
    for key, val in dictionary.items():
        print(f"{key}   : {val}")

doctor = []

print("Doctor Database")
print("=======================")

while True:
    lagi = input("Add a doctor? (y/n):")
    print("")
    if lagi == "y":
        dokter = {}
        name = input("Enter name    :")
        age = input("Enter age     :")
        spec = input("Speciality    :")
        dokter["nama"] = name
        dokter["umur"] = age
        dokter["spes"] = spec
        doctor.append(dokter)
    if lagi == "n":
        break
    else:
        pass

for x in doctor:
    doc(x)
    print("")
