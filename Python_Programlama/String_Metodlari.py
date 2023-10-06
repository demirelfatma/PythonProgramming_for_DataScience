# STRİNG METOTLARI

# len()

gel_yaz="gelecegi_yazanlar"

a = 9
b = 10
a*b

len(gel_yaz)

# upper() & lower()

gel_yaz="gelecegi_yazanlar"
gel_yaz.upper()
gel_yaz.lower()

k = gel_yaz.islower()
b = gel_yaz.isupper()

# replace() - string ifadede değişiklik yapma

gel_yaz="gelecegi_yazanlar"
gel_yaz.replace("e","a")
gel_yaz.replace("a","i")

# strip()

gel_yaz="gelecegi*_yazanlar"
gel_yaz.strip("*")

# Metotlara Genel Bakış

gel_yaz="gelecegi_yazanlar"
dir(gel_yaz)
# dir() ifadeye uygulanabilecek metotlara erişmemizi sağlar