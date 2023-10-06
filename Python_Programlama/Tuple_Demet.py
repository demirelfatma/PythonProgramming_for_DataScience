# Veri Yapıları - Tuple(demet)

# not: listeler kapsayıcıdır, sıralıdır, değiştirilebilir

# not : tuple kapsayıcıdır, sıralıdır, değiştirilemezzzzzz

# tuple oluşturma
t = ("ali","veli",1,2,3.2,[1,2,3,4])

t = "ali","veli",1,2,3.2, [1,2,3,4]

#tuple()

t = ("eleman",)
type(t)


# tuple eleman işlemleri
t1 = ("ali","veli",1,2,3,[1,2,3,4])
print(t1)

print(t1[1])
print(t1[0:3])

# t1[2]=90 - typeerror - tuple değiştirilemez