# Sözlük(dictionary) Oluşturma

# not: sözlükler kapsayıcıdır, sırasızdır, değiştirilebilir

# sözlükler key(anahtar) velue(karşılık) bir arada bulunduğu bir veri yapısıdır.

sozluk = {"REG":"Regresyonj Modeli",20:"Lojistik Regresyon","CART": ["Classification and Reg",30]}

print(sozluk)
print(len(sozluk))


# Sözlük Eleman İşlemleri

sozluk = {"REG":"Regresyonj Modeli",20:"Lojistik Regresyon","CART": ["Classification and Reg",30]}
print(sozluk["REG"])
print(sozluk["CART"])

sozluk2 = {"REGt":{"REG":"Regresyonj Modeli",20:"Lojistik Regresyon","CART": ["Classification and Reg",30]}
           ,200:{"REG":"Regresyonj Modeli",20:"Lojistik Regresyon","CART": ["Classification and Reg",30]}
           ,"CARTt": {"REG":"Regresyonj Modeli",20:"Lojistik Regresyon","CART": ["Classification and Reg",30]}}

print(sozluk2)


# Sozluk - Eleman Eklemek & Degistirmek

sozluk = {"REG":"Regresyonj Modeli",20:"Lojistik Regresyon","CART": ["Classification and Reg",30]}
sozluk["GBM"] = "Gradient Boosting Mac"
print(sozluk)

sozluk["REG"] = "Coklu Dogrusal Regesyon"
print(sozluk)

sozluk[1] = "Yapay Sinir Aglari"

print(sozluk)

l = [1]
print(l)

# sozluk[l] = "yeni bir sey" - TypeError: unhashable type: 'list'- sözlüklerde key değerleri ancak sabit veri yapılarıyla oluşturulabilir, listeb veri yapısıyla oluşturulamaz.
print(sozluk)

t = ("tuple",)

sozluk[t] = "yeni bir sey"
print(sozluk)