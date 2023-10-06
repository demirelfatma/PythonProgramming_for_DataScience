# Listeler - Liste Metodları

liste = ["ali", "veli", "isik"]

dir(liste)
print(liste)


#append -> eleman ekleme

liste.append("berkcan")
print(liste)



#remove -> eleman silme

liste.remove("berkcan")
print(liste)



#insert -> indekse göre eleman ekleme

liste = ["ali", "veli", "isik"]
print(liste)

liste.insert(0,"ayse")
print(liste)

liste = ["ali", "veli", "isik"]
liste[0] = "ayse"
print(liste)

liste[1] = "ali"
print(liste)

liste.insert(5, "berk")
print(liste)

liste.insert(len(liste), "beren")
print(liste)



#pop -> indekse göre eleman silme

liste.pop(0)
print(liste)


#count - sayma

liste = ["ali","veli","isik","ali","veli"]

liste.count("ali")
liste.count("veli")
print(liste.count("isik"))


#copy

liste_yedek = liste.copy()


#extend - iki listeyi birleştirmek için kullanılır

liste.extend(["a","b",10])
print(liste)

#index - elemanın hangi indekste olduğu bilgisini almak için kullanılır

print(liste.index("ali"))

#reverese - liste elemnlarını terse çevirmek için kullanılır

liste.reverse()
print(liste)


#sort - sıralama yapmak için kullanılır

listee = [10,40,5,90]
listee.sort()
print(listee)

#clear - listeyi temizleme - liste içindeki tüm elemanları siler

liste.clear()
print(liste)




























