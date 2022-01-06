print("Birinci Fonksiyon Ödevi")


def bolunen_sayi_bulma(min_sayi, max_sayi, bolunecek_sayi):
    tam_bolunmus_sayilar = []
    for index in range(min_sayi, max_sayi):
        if index % bolunecek_sayi == 0:
            tam_bolunmus_sayilar.append(index)

    print(tam_bolunmus_sayilar)
    return len(tam_bolunmus_sayilar)


son_durum = bolunen_sayi_bulma(5, 25, 2)
print(son_durum)
print("********************************************")

print("İkinci Fonksiyon Ödevi")
sayi_girdisi = int(input("2 Basamaklı Sayı Giriniz:"))


def sayi_atama(sayi_girdisi):
    if ((sayi_girdisi >= 10) and (sayi_girdisi <= 99)):
        print("Geçerli Girdi")
        sayiOkunusu(sayi_girdisi)
    else:
        print("Geçersiz Girdi.Tekrar deneyin.")


def sayiOkunusu(sayi_girdisi):
    sayi_liste = [int(digit) for digit in str(sayi_girdisi)]

    onlar_basamak = {1: "on", 2: "yirmi", 3: "otuz", 4: "kirk", 5: "elli", 6: "altmiş", 7: "yetmiş", 8: "seksen",
                     9: "doksan"}
    birler_basamak = {1: "bir", 2: "iki", 3: "üç", 4: "dört", 5: "beş", 6: "alti", 7: "yedi", 8: "sekiz",
                      9: "dokuz"}

    onlar = onlar_basamak[sayi_liste[0]]
    birler = birler_basamak[sayi_liste[1]]

    print("{} {}".format(onlar, birler))


sayi_atama(sayi_girdisi)

print("********************************************")


print("Üçüncü Fonksiyon Ödevi")


def not_kontrol(score):
    while True:
        if score < 0 or score > 100:
            score = int(input("Hata! Lütfen 0-100 arası notunuzu tekrar giriniz:"))
        else:
            break
    return score


birinci_vize = not_kontrol(int(input("Lütfen birinci vize notunuzu giriniz:")))
ikinci_vize = not_kontrol(int(input("Lütfen ikinci vize notunuzu giriniz:")))
final = not_kontrol(int(input("Lütfen final notunuzu giriniz:")))

sinav_ortalamasi = ((birinci_vize * 0.3) + (ikinci_vize * 0.3) + (final * 0.4))

if (sinav_ortalamasi >= 90):
    print("Harf notunuz AA ve Genel puanınız:", sinav_ortalamasi)

elif (sinav_ortalamasi >= 85):
    print("Harf notunuz BA ve Genel puanınız:", sinav_ortalamasi)

elif (sinav_ortalamasi >= 80):
    print("Harf notunuz BB ve Genel puanınız:", sinav_ortalamasi)

elif (sinav_ortalamasi >= 75):
    print("Harf notunuz CB ve Genel puanınız:", sinav_ortalamasi)

elif (sinav_ortalamasi >= 70):
    print("Harf notunuz CC ve Genel puanınız:", sinav_ortalamasi)

elif (sinav_ortalamasi >= 65):
    print("Harf notunuz DC ve Genel puanınız:", sinav_ortalamasi)

elif (sinav_ortalamasi >= 60):
    print("Harf notunuz DD ve Genel puanınız:", sinav_ortalamasi)

elif (sinav_ortalamasi >= 55):
    print("Harf notunuz FD ve Genel puanınız:", sinav_ortalamasi)

elif (sinav_ortalamasi < 55):
    print("Harf notunuz FF ve Genel puanınız:", sinav_ortalamasi)

print("********************************************")
