
class Flower:
    def __init__(self, nama, kelopak, harga):
        self.nama = str(nama)
        self.kelopak = int(kelopak)
        self.harga = float(harga)
        flowers.append(self)
    def bunga(self):
        return f"Bunga: {self.nama} ;Jumlah kelopak: {self.kelopak} ;Harga: {self.harga}"
    
    @classmethod
    def new_flower(cls):
        nama = input("Masukkan nama bunga: ")
        kelopak = input("Masukkan jumlah kelopal: ")
        harga = input("Masukkan harga: ")
        return cls(nama,kelopak, harga)

flowers = []

Flower("melati", 5, 90)
#flowers.append(Flower("lili", 4, 19.0))
#flowers.append(Flower("rose", 3, 20.0))


while True:
    lagi = input("Tambah bunga? (y/n): ")
    print("")
    if lagi == "y":
        Flower.new_flower()
    elif lagi == "n":
        break
    else:
        pass

for x in flowers:
    print(x.bunga())
