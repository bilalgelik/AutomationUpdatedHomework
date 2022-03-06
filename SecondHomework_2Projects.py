
print("Birinci Class Ödevi")

class Ogrenci:
    def __init__(self, ogrenci_adi, ogrenci_soyadi, ogrenci_sinifi):
        self.ogrenci_adi = ogrenci_adi
        self.ogrenci_soyadi = ogrenci_soyadi
        self.ogrenci_sinifi = ogrenci_sinifi

    def ogrenci_bilgileri(self):
        print(""" 
              Öğrenci Adı : {}
              Öğrenci Soyadı  : {}
              Öğrenci Sınıfı : {}
              """.format(self.ogrenci_adi, self.ogrenci_soyadi, self.ogrenci_sinifi))

# net sayisi toplam puan
class Sorular:
    @staticmethod
    def net_sayisi(dogru, yanlis):
           # gidenDogru = int(Yanlis /4)
            toplam_net = dogru - (int(yanlis / 4))            
            print("""
                Doğru Soru Sayısı : {}
                Yanlış Soru Sayısı : {}
                Öğrenci Net Sayısı : {}
                """.format(dogru, yanlis, toplam_net))
            return toplam_net
            
    @staticmethod
    def not_hesapla(toplam_net):
        toplam_puan = toplam_net * 2
        if toplam_puan < 0 :
            print("Toplam Puan : 0")
        
        else:
            print(""" 
                ogrenciToplamPuani : {}
                """.format(toplam_puan))
        
ogrenci_adi = input("Öğrenci ismini giriniz:")
ogrenci_soyadi = input("Öğrenci soyismini giriniz:")
ogrenci_sinifi = input("Öğrenci sinifini giriniz:")

# Soru Sayısı Kontrolü
while True:
    dogru_sayisi = int(input("Öğrenci doğru sayısını giriniz:"))
    yanlis_sayisi = int(input("Öğrenci yanlış sayısını giriniz:"))

    if(dogru_sayisi + yanlis_sayisi != 50):
        print("Doğru yanlış toplam soru sayısı 50 olmalıdır!")
    else:
        break

ogrenci_ciktisi = Ogrenci(ogrenci_adi, ogrenci_soyadi, ogrenci_sinifi)
ogrenci_ciktisi.ogrenci_bilgileri()

soru_ciktisi = Sorular()
toplam_net = soru_ciktisi.net_sayisi(dogru_sayisi, yanlis_sayisi)
soru_ciktisi.not_hesapla(toplam_net)

print("*****************************************")


print("İkinci Class Ödevi")


class Insan():
    def __init__(self, ad = "Bilal", soyad = "Gelik", yas = 24, ulke = "Turkey", sehir = "Istanbul", yetenek_dizisi = []):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.ulke = ulke
        self.sehir = sehir
        self.yetenek_dizisi = yetenek_dizisi

    def yetenek_ekle(self):
        yetenek = input("Hangi Yeteneğini EKlemek İstersin? ")
        self.yetenek_dizisi.append(yetenek)

    def kisi_bilgileri(self):
        return self.ad, self.soyad, self.yas, self.ulke, self.sehir, self.yetenek_dizisi

kisi_hakkinda = Insan()

while True:
    cevap = input("Yetenek Listesine Yetenek Eklemek İster Misin?  E / H ")

    if(cevap == "E"):
        kisi_hakkinda.yetenek_ekle()
        print(kisi_hakkinda.kisi_bilgileri())

    else:
        kisi_hakkinda.kisi_bilgileri()
        break



