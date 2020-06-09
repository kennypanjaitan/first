hasil = []
class Tabung:
    def __init__(self, rad, tinggi, luas, volum):
        self.rad = rad
        self.tinggi = tinggi
        self.luas = luas
        self.volum = volum
        hasil.append(self)

    def equal(self):
        return f"Jari - jari = {self.rad}; Luas = {self.luas}"
    def samadengan(self):
        return f"Jari - jari = {self.rad}; Tinggi = {self.tinggi}; Luas = {self.luas}; Volume = {self.volum}"

    # def area(self):
    #     return phi * self.rad ** 2 
    # def volume(self):
    #     return phi * self.tinggi * self.rad ** 2
    
    @classmethod
    def new_tabung(cls):
        try:
            rad = int(input("Jari - jari alas tabung: "))
            operator = int(input("1 = Luas alas tabung\n2 = Volume tabung\nApa yang ingin anda hitung?: "))
        except ValueError:
            print("lah...")
        except:
            pass
        else:
            # equal = {}
            if operator == 1:
                luas = phi * rad ** 2
                print(luas)
                return cls(rad, None, luas, None)
                # equal["Luas"] = luas
                # equal["Volume"] = None
            elif operator == 2:
                tinggi = int(input("Tinggi tabung: "))
                luas = phi * rad ** 2
                volum = phi * tinggi * rad ** 2
                print(volum)
                return cls(rad, tinggi, luas, volum)
                # equal["Luas"] = None                
                # equal["Volume"] = volum
                # samadengan.append(equal)
        finally:
            pass

batas = "=========================="
phi = 3.14

print(batas)
print("KALKULATOR TABUNG")
print(batas)
while True:
    Tabung.new_tabung()
    lagi = input("Pakai kalkulator lagi? (y/n): ")
    if lagi == "y":
        continue
    elif lagi == "n":
        break
    else:
        pass


# def hasil(dictionary):
#     for key, val in dictionary.items():
#         #gabisa delete
#         if val == None:
#             del equal[key]
#         print (f"{key}  = {val}")

#caurrrrrrr....
#samadengan = []
print(batas)
print("USAGE HISTORY\n")
# for x in hasil:

#     print(x.equal())
for x in hasil:
    if "Tinggi = None" and "Volume = None" in hasil:
        hasil.remove()
    print(x.samadengan())
# for x in samadengan:
#     hasil(x)

