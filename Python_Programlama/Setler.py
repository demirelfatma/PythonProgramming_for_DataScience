# Veri Yapilari - Setler

# SETLER sırasızdır, değerleri eşsizdir, değiştirilebilir, farklı tipleri barındırabilir

s = set()

print(s)

l = [1,"a","ali",123]
s = set(l)
print(s)

t = ("a","ali")
s = set(t)
print(s)

ali = "lutfen_ata_bakma_uzaya_git"
print(type(ali))

s = set(ali)
print(s)

l = ["ali","lutfen","ata","bakma","uzaya","git","git","ali","git"]
print(l)

s = set(l)
print(s)

print(len(s))

print(l[0])

print(l[1])


# Eleman ekleme & cikarma

l = ["geleceği","yazanlar"]

s = set(l)

print(s)

dir(s)

s.add("i")
print(s)

s.add("gelecege_git")
print(s)


s.add("i")
print(s)

s.remove("i")
print(s)


# Setler - Klasik Kume Islemleri

# =============================================================================
# difference() ile iki kumenin farkini ya da "-" ifadesi 
# intersection() iki kume kesisimi ya da "&" ifadesi
# union() iki kumenin birlesimi
# symmetric_difference() ikisinde de olmayanlari
# =============================================================================


# difference

set1 = set([1,3,5])
set2 = set([1,2,3])

print(set1.difference(set2))
print(set2.difference(set1))

print(set1.symmetric_difference(set2))

print(set1 - set2)
print(set2 - set1)

# intersection & union

set1 = set([1,3,5])
set2 = set([1,2,3])

print(set1.intersection(set2))
print(set2.intersection(set1))

kesisim = set1 & set2
print(kesisim)

birlesim = set1.union(set2)
print(birlesim)

set1.intersection_update(set2)
print(set1)

# Set Sorgu Islemleri

set1 =set([7,8,9])
set2 = set([5,6,7,8,9,10])

#iki kumenin kesisiminin bos olup olmadiginin sorgulanmasi

print(set1.isdisjoint(set2))

#bir kumenin butun elemanlarinin baska bir kume icerisinde yer alip almadigi

print(set1.issubset(set2))
























