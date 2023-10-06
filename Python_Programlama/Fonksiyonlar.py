# FONKSİYONLARA GİRİS VE FONKSİYON 
# fonksiyon belirli amaçları yerine getiren belirteçlerdir
# argümanlar fonksiyonların genel amaçlarını biçimlendiren alt amaçlardır.

print("a", "b",sep="_")
print()
len("a")

# Matematiksel İşlemler

4*4
3+7
5-1
6/2


# Fonksiyon Nasıl Yazılır? def ifadesi fonksiyon tanımlamaya yarar

def kare_al(x):
    print(x**2)
    
kare_al(3)

# Bilgi notuyla cikti uretmek

kare_al(5)

def kare_al(x):
    print("Girilen Sayinin Karesi: " + str(x**2))
    
kare_al(3)

def kare_al(x):
    print("Girilen Sayi: " + str(x) + "\nKaresi:" + str(x**2))
    
kare_al(4)

# Iki argumanli fonksiyon tanimlamak

def kare_al(x):
    print(x**2)
    
def carpma_yap(x,y):
    print(x*y)
    
carpma_yap(2, 3)


# On Tanimli Argumanlar

def carp(x,y=3):
    print(x*y)

carp(4)

print("HELLO IA ERA")

# Argumanlarin Siralamasi

def carp(x,y=3):
    print(x*y)

carp(y=5,x=8)

# Ne zaman fonksiyon yazılır?

# isi, nem, sarj -> sokak lambası problemi

(40+25)/90

def direk_hesap(isi, nem, sarj):
    print((isi+nem)/sarj)
    
cikti = direk_hesap(25, 40, 70)
cikti
print(cikti)

#direk_hesap(25,49,70)*9 - type error

def direk_hesap(isi, nem, sarj):
    return (isi+nem)/sarj

cikti = direk_hesap(25, 40, 70)
cikti
print(cikti)
direk_hesap(25,49,70)*9

def direk_hesap(isi, nem, sarj):
    return (isi+nem)/sarj
direk_hesap(25,49,70)*9































