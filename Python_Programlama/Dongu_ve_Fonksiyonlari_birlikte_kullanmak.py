# Dongu ve fonksiyonlari beraber kullanmak

def kare_al(x):
    print(x**2)
    
kare_al(2)

maaslar = [1000,2000,3000,4000,5000]

for i in maaslar:
    print(i)
    
#maaslara yuzde 20 zam yapilacak

1000*20/100 + 1000

maaslar[0]*20/100 + maaslar[0]
maaslar[1]*20/100 + maaslar[1]
maaslar[2]*20/100 + maaslar[2]

#dongu yazilacak

maaslar[0]*20/100 + maaslar[0]

#fonksiyonn yazmak

def yeni_maas(x):
    print(x)

yeni_maas(1000)
yeni_maas(2000)
yeni_maas(3000)    


for i in maaslar:
    yeni_maas(i)




















