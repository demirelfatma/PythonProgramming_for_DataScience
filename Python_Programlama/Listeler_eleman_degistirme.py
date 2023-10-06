# Listeler - Eleman Degistirme

liste = ["ali","veli","berkcan","ayse"]

print(liste)

liste[1] = "velinin_babasi"

print(liste)

liste[1] = "veli"

liste[0:3] = "alinin_babasi", "velinin_babasi", "berkcanin_babasi"

print(liste)

liste + ["kemal"]
print(liste)

# del herhangi bir listeyi ve liste içindeki istediğimiz elemanı silmemizi sağlar
del liste[2]
print(liste)