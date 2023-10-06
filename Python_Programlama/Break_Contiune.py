# break & continue

maaslar = [8000,5000,2000,1000,3000,7000,1000]

dir(maaslar) #maaslar üzerine uygulanabilecek fonksiyonlar

maaslar.sort()
maaslar

for i in maaslar:
    if i == 3000:
        print("kesildi")
        break  #kirmak döngüden çıkmak
    print(i)
    
    
    
for int in maaslar:
    if i == 3000:
        print("kesildi")
        continue #atlamak
    print(i)