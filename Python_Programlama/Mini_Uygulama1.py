# mini uygulama
sinir = 50000
magaza_adi = input("Magaza Adi Nedir?")
gelir = int(input("Gelirinizi giriniz: "))

if gelir > sinir:
    print("Tebrikler:"+ magaza_adi + " promosyon kazandınız!")
elif gelir < sinir:
    print("Uyari! cok dusuk gelir: " + str(gelir))
else:
    print("Takibe devam")

