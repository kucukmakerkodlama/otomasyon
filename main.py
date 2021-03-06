# import pandas as pd kaldırıldı çünkü kullanılmıyor
import numpy as np
from matplotlib import pyplot as plt

#  from matplotlib import pyplot as plt1 kaldırıldı çünkü kullanılmıyor
import math as mt
from scipy.stats import norm as nrm
# from scipy.stats import binom kullanılmadığı için kaldırıldı
# import seaborn as sns kullanılmadığı için kaldırıldı

# boş bir array oluşturuyoruz
sinifList = []
# mevcud verisini deklare ediyoruz
mevcud = 0
# basariNotuHesaplaKontrol verisini deklare ediyoruz
basariNotuHesaplaKontrol = 0

# bir öğrenci şeması class'ı oluşturuyoruz
class ogrenci:
    basariNotu = 0.0
    basariDurumu = ""
    harfNotu = ""

    ogrenciNo = 0
    ogrenciAd = ""
    ogrenciSoyad = ""
    vize1 = 0
    vize2 = 0
    final = 0

# basariNotuHesapla fonksiyonunu oluşturdulk
def basariNotuHesapla():
    # basariNotuHesaplaKontrol verisini global olarak ulaşılabilir yapıyoruz.
    global basariNotuHesaplaKontrol
    basariNotuHesaplaKontrol = basariNotuHesaplaKontrol + 1
    # sınıf sayısı kadar döngüye sok
    for i in range(len(sinifList)):
        # sınıf listesindeki 1. 2. ve 3. notları satırlarda belinen float değerleri ile çarp ve bunları "Notu" verisine eşitle
        no1 = (float(sinifList[i].vize1) * 0.20)
        no2 = (float(sinifList[i].vize2) * 0.30)
        no3 = (float(sinifList[i].final) * 0.50)
        Notu = no1 + no2 + no3

        # "notu" verisini "kontrolStringi" altına string olarak ata
        kontrolStringi = str(Notu)


        for x in range(0, len(kontrolStringi)):
            if (kontrolStringi[x] == '.'):
                if (int(kontrolStringi[x + 1]) >= 5):
                    Notu = mt.ceil(Notu)
                else:
                    Notu = mt.floor(Notu)

        sinifList[i].basariNotu = Notu
        # notu geçip geçmediğini kontrol ediyoruz. bu kısımda switch case kullanmak daha mantıklı olabilir...
        if (sinifList[i].basariNotu >= 90 and sinifList[i].basariNotu <= 100):
            sinifList[i].harfNotu = "AA"
            sinifList[i].basariDurumu = "Geçti"
        elif (sinifList[i].basariNotu >= 85 and sinifList[i].basariNotu <= 89):
            sinifList[i].harfNotu = "BA"
            sinifList[i].basariDurumu = "Geçti"
        elif (sinifList[i].basariNotu >= 80 and sinifList[i].basariNotu <= 84):
            sinifList[i].harfNotu = "BB"
            sinifList[i].basariDurumu = "Geçti"
        elif (sinifList[i].basariNotu >= 75 and sinifList[i].basariNotu <= 79):
            sinifList[i].harfNotu = "CB"
            sinifList[i].basariDurumu = "Geçti"
        elif (sinifList[i].basariNotu >= 70 and sinifList[i].basariNotu <= 84):
            sinifList[i].harfNotu = "CC"
            sinifList[i].basariDurumu = "Geçti"
        elif (sinifList[i].basariNotu >= 65 and sinifList[i].basariNotu <= 69):
            sinifList[i].harfNotu = "DC"
            sinifList[i].basariDurumu = "Geçti"
        elif (sinifList[i].basariNotu >= 60 and sinifList[i].basariNotu <= 64):
            sinifList[i].harfNotu = "DD"
            sinifList[i].basariDurumu = "Geçti"
        elif (sinifList[i].basariNotu >= 50 and sinifList[i].basariNotu <= 59):
            sinifList[i].harfNotu = "FD"
            sinifList[i].basariDurumu = "Şartlı Geçti"
        elif (sinifList[i].basariNotu <= 49):
            sinifList[i].harfNotu = "FF"
            sinifList[i].basariDurumu = "Kaldı"
#  kayıtları listelemek için gerekli olan fonksiyon
def listele():
    # bellekte kullanmak için "i" ve "j" değişkenlerini atıyoruz.
    i = 0
    j = 0
    # sınıf listesindeki index verisi kadar döngüye sokuyoruz
    for index in range(len(sinifList)):
        # j'yi index'e eşitliyoruz
        j = index
        # sınıf listesinden çektiğimiz öğrenci bilgilerini ayıklıyoruz ediyoruz.
        while (j > 0) and (int(sinifList[j - 1].ogrenciNo) > int(sinifList[j].ogrenciNo)):
            sinifList[j - 1], sinifList[j] = sinifList[j], sinifList[j - 1]
            j -= 1
        # ayıkladığımız veriyi yazdırıyoruz.
    for i in range(len(sinifList)):
        print(
            '{0} {1} {2} {3} {4} {5}'.format(sinifList[i].ogrenciNo, sinifList[i].ogrenciAd, sinifList[i].ogrenciSoyad,
                                             sinifList[i].vize1, sinifList[i].vize2, sinifList[i].final))

# öğrenci bilgilerini güncellemede işimize yarayacak fonksiyon
def guncelle():
    # durum verisini deklare ediyoruz
    durum = 0
    try:
        # öğrenci no'sunu sonra kullanmak için "integer" olarak çekiyoruz.
        ogrNo = int(input('Güncellenecek Öğrencinin Öğrenci Numarasını Giriniz : '))
        try:
        # öğrenci no'nun olup olmadığına bakıyoruz
            for i in range(len(sinifList)):
                # eğer varsa:
                if (int(sinifList[i].ogrenciNo) == ogrNo):
                    durum = 1
                    # güncelleme işlemi fonksiyonuna gidiyoruz (130. satır)
                    guncellemeIslemiFonk(i)
                    break
            if (durum == 0):
                a = 1 / 0
        # eğer gelen veri yoksa hata veriyoruz :dadidadidadi:
        except ZeroDivisionError:
            print('Öğrenci Numarası Bulunamadı!')

    #  eğer gelen veri "integer" değilse hatayı yazdırıyoruz
    except ValueError:
        print('Numerik Değer Giriniz !')

def guncellemeIslemiFonk(indis):
# fonksiyonun çağrıldığı yerden öğrenci verilierini çekiyoruz ve bunların formatını ayarlıyoruz.
    print('Öğrenci Adı :{0} Öğrenci Soyadı :{1} Vize1 :{2} Vize2 :{3} Final :{4}'.format(sinifList[indis].ogrenciAd,
                                                                                         sinifList[indis].ogrenciSoyad,
                                                                                         sinifList[indis].vize1,
                                                                                         sinifList[indis].vize2,
                                                                                         sinifList[indis].final))
# yapılacak işlemi kullanıcıdan bekliyoruz
    islem = int(input('1)Vize1 Notu Güncelle 2)Vize2 Notu Güncelle 3)Final Notu Güncelle'))
# istenilen işlemlere göre veriyi çekip değişkeni düzenliyoruz. eğer uygun giriş yapılmaz ise uyarı atıyoruz.
    if (islem == 1):
        sinifList[indis].vize1 = int(input('Notu Giriniz : '))
        print('Güncelleme Başarılı Oldu')
    elif (islem == 2):
        sinifList[indis].vize2 = int(input('Notu Giriniz : '))
        print('Güncelleme Başarılı Oldu')
    elif (islem == 3):
        sinifList[indis].final = int(input('Notu Giriniz : '))
        print('Güncelleme Başarılı Oldu')
    else:
        print('Uygun Giriş Yapınız !')

# kullanıcı kaydı ekleme fonksiyonu
def kayitEkleme():
    durum = 0

    try:
        # eklenecek öğrencinin numarasını çekiyoruz eğer ineger değilse hata atıyoruz eğer zaten var ise kayıtlı hatası atıyorz
        numara = int(input('Eklenecek Öğrenci Numarasını Giriniz : '))
        try:
            durum = 1
            # öğrenci kayıtlı mı değil mi tüm sınıf listesinden çekiyoruz
            for i in range(len(sinifList)):
                if (int(sinifList[i].ogrenciNo) == numara):
                    durum = 0
            deneme = 1 / (durum)
            # öğrenci numarasını sisteme eklemek için öğrenci numarasıyla veriyi eklemeIslemiFonk fonksiyonuna gönderiyoruz.
            eklemeIslemiFonk(numara)
        except ZeroDivisionError:
            print('Bu Öğrenci Numarası Sisteme Kayıtlıdır')
    except ValueError:
        print('Numerik Değerler Giriniz !')

# öğrenci ekleme fonksiyonu 2.si
def eklemeIslemiFonk(gelenNumara):

    o2 = ogrenci
# öğrenciye ait verileri çekiyoruz
    o2.ogrenciNo = gelenNumara
    o2.ogrenciAd = input('Öğrencinin Adını Giriniz : ')
    o2.ogrenciSoyad = input('Öğrencinin Soyadını Giriniz : ')
    o2.vize1 = int(input('Öğrencinin Vize1 Notunu Giriniz : '))
    o2.vize2 = int(input('Öğrencinin Vize2 Notunu Giriniz : '))
    o2.final = int(input('Öğrencinin Final Notunu Giriniz : '))
# bu verileri bellekteki sınıf listesine ekliyoruz
    sinifList.append(o2)
    print('Ekleme İşlemi Başarılı Oldu')

# kayıt silme fonksiyonu
def kayitSilme():
    try:
        # silinecek öğrencinin numarasını alıyoruz
        numara = int(input('Silinecek Öğrencinin Numarasını Giriniz'))
        try:
            durum = 0
            index = 0
            # öğrenci kayıtlı mı bakıyoruz
            for i in range(len(sinifList)):
                if (int(sinifList[i].ogrenciNo) == numara):
                    durum = 1
                    index = i
                    del sinifList[index]
                    print('Kayıt silindi!\n')
                print('kayıt bulunamadı')
# kayıtsız ise :
        except ZeroDivisionError:
            print('Sisteme Kayıtlı Öğrenci Numarası Bulunamadı!')
            # sayı girmediyse :
    except ValueError:
        print('Numerik Değer Giriniz')

'''
gereksiz bir fonksiyon.
def kayitSilmeIslemiFonk(indis):
    del sinifList[indis]
    print('Kayıt Silme Başarılı Oldu')
'''
# başarı notunu sıraladığımız fonksiyon
def basariNotuSiralama():
    i = 0
    j = 0
    # sınıf listesindeki öğrenci sayısı kadar döngüyü alıyoruz.
    for index in range(len(sinifList)):
        j = index
        # başarı notunu sıralıyoreuz
        while (j > 0) and (sinifList[j - 1].basariNotu < sinifList[j].basariNotu):
            sinifList[j - 1], sinifList[j] = sinifList[j], sinifList[j - 1]
            j -= 1
            # başarı notlarını konsola yazdırıyoruz
    for i in range(len(sinifList)):
        print('{0} {1} {2} {3} {4} {5} {6} {7} {8}'.format(sinifList[i].ogrenciNo, sinifList[i].ogrenciAd,
                                                           sinifList[i].ogrenciSoyad, sinifList[i].vize1,
                                                           sinifList[i].vize2, sinifList[i].final,
                                                           sinifList[i].basariNotu, sinifList[i].harfNotu,
                                                           sinifList[i].basariDurumu))

# istatik alma fonksiyonu
def istatistik():

# sınıf listesi altındaki öğrencilerden başarı notlarını çekiyoruz ve bunu sınıf not listesini kaydediyoruz.
    sinifNotListesi = []
    for i in range(len(sinifList)):
        sinifNotListesi.append(sinifList[i].basariNotu)
# bu listeyi numpy kullanarak bir numpy arrayina atıyoruz
    list1 = np.array(sinifNotListesi)
# bu verileri düzenliyoruz
    enYuksekBasariNotu = list1.max()
    enDusukBasariNotu = list1.min()
    sinifOrtalamasi = list1.mean()
    standartSapma = list1.std()

    sayac = 0
# list1'de ki öğrenci sayısı kadar döngüye alıyoruz. bu kısımda öğrenci notlarının sınıf ortalamasından fazla olup olmadığını kontrol ediyoruz.
    for i in range(len(list1)):
        if (list1[i] > sinifOrtalamasi):
            sayac = sayac + 1
    ortalamayiGecenOgrenciSayisi = sayac
# yukarıda düzenlediğimiz verileri yazdırıyoruz.
    print('En Yüksek Başarı Notu : {0}'.format(enYuksekBasariNotu))
    print('En Düşük Başarı Notu : {0}'.format(enDusukBasariNotu))
    print('Sınıf Ortalaması : {0}'.format(sinifOrtalamasi))
    print('Ortalamayı Geçen Öğrenci Sayısı : {0}'.format(ortalamayiGecenOgrenciSayisi))
    print('Standart Sapma : {0}'.format(standartSapma))
# bu kısımda notlara göre öğrencilerin kalıp kalmama durumunu hesaplıyoruz.
    mean = sinifOrtalamasi
    standard_deviation = standartSapma

    x_values = np.arange(-3, 3, 0.1)
    y_values = nrm(mean, standard_deviation)

    plt.plot(x_values, y_values.pdf(x_values))
    plt.show()

    harfNotlari = []

    harfNotlari.append('AA')
    harfNotlari.append('BA')
    harfNotlari.append('BB')
    harfNotlari.append('CB')
    harfNotlari.append('CC')
    harfNotlari.append('DC')
    harfNotlari.append('DD')
    harfNotlari.append('FD')
    harfNotlari.append('FF')

    AA = 0
    BA = 0
    BB = 0
    CB = 0
    CC = 0
    DC = 0
    DD = 0
    FD = 0
    FF = 0
# öğrenci sayısı kadar döngü ve hesaplama
    for i in range(len(sinifList)):
        if (sinifList[i].harfNotu == 'AA'):
            AA = AA + 1
        elif (sinifList[i].harfNotu == 'BA'):
            BA = BA + 1
        elif (sinifList[i].harfNotu == 'BB'):
            BB = BB + 1
        elif (sinifList[i].harfNotu == 'CB'):
            CB = CB + 1
        elif (sinifList[i].harfNotu == 'CC'):
            CC = CC + 1
        elif (sinifList[i].harfNotu == 'DC'):
            DC = DC + 1
        elif (sinifList[i].harfNotu == 'DD'):
            DD = DD + 1
        elif (sinifList[i].harfNotu == 'FD'):
            FD = FD + 1
        elif (sinifList[i].harfNotu == 'FF'):
            FF = FF + 1

    harfNotlariSayac = []
    harfNotlariSayac.append(AA)
    harfNotlariSayac.append(BA)
    harfNotlariSayac.append(BB)
    harfNotlariSayac.append(CB)
    harfNotlariSayac.append(CC)
    harfNotlariSayac.append(DC)
    harfNotlariSayac.append(DD)
    harfNotlariSayac.append(FD)
    harfNotlariSayac.append(FF)

    plt.subplot(2, 1, 2)
    plt.bar(harfNotlari, harfNotlariSayac)
    plt.ylabel('Harf Notu Dağılımı')
    plt.show()

# menüyü hazırlıyoruz
def menu():
    print('-------------------------------------------------')
    print('1)Yeni Kayıt Ekle')
    print('2)Kayıt Güncelle')
    print('3)Kayıt Sil')
    print('4)Kayıtları Listele')
    print('5)Sınıf Başarı Notlarını Hesapla')
    print('6)Kayıtları Başarı Notuna Göre Sırala')
    print('7)İstatistiki Bilgiler')
    print('8)Çıkış')
# seçimi bekliyoruz
    try:
        secim = int(input('Yapmak İstediğiniz İşlemi Belirtiniz : '))

        if (secim == 1):
            kayitEkleme()
        elif (secim == 2):
            guncelle()
        elif (secim == 3):
            kayitSilme()
        elif (secim == 4):
            listele()
        elif (secim == 5):
            basariNotuHesapla()
            print("Başarı Notu Hesaplandı")
        elif (secim == 6):
            if (basariNotuHesaplaKontrol > 0):
                basariNotuSiralama()
            else:
                print('Önce Başarı Notlarını Hesaplayınız')
        elif (secim == 7):
            if (basariNotuHesaplaKontrol > 0):
                istatistik()
            else:
                print('Başarı Notu Hesaplandıktan Sonra Bu Fonksiyon Çalışabilir')
        elif (secim > 8):
            print('Geçerli bir seçenek girin.')
        elif (secim == 8):
            return 'Çıkış Yapıldı'
        menu()

    except ValueError:
        print('Numerik Bir Değer Giriniz')
        menu()

# menüyü çağırıyoruz.
menu()