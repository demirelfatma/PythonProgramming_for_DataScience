# NESNE YONELİMLİ PROGRAMLAMA

# Sinif nedir?

class VeriBilimci():
    print("Bu bir siniftir")
    
#Sinif ozellikleri(class attributes)

class VeriBilimciler():
    bolum = ''
    sql = 'evet'
    deneyim_yili = 0
    bildigi_diller = []
    
VeriBilimciler.bolum
VeriBilimciler.sql

#Siniflarin ozelliklerini degistirmek

VeriBilimciler.sql = 'hayir'
VeriBilimciler.sql

#Sinif orneklendirmesi(instantiation)

ali = VeriBilimciler()

ali.sql
ali.deneyim_yili
ali.bolum

ali.bildigi_diller.append("Python")
ali.bildigi_diller

veli = VeriBilimciler()
veli.sql
veli.bildigi_diller

#Ornek ozellikleri

class VeriBilimci():
    bildigi_diller = ["R","PYTHON"]
    bolum = ''
    sql = ''
    mezuniyet_yili = 0
    def __init__(self): #self ornekleri temsil eder
        self.bildigi_diller = []
        
veli = VeriBilimci()
veli.bildigi_diller

ali.bildigi_diller.append("Python")
ali.bildigi_diller

veli.bildigi_diller
veli.bildigi_diller.append("R")
veli.bildigi_diller


VeriBilimci.bildigi_diller
ali.bolum = "istatistik"
VeriBilimci.bolum
veli.bolum
veli.bolum = "end_muh"
veli.bolum
ali.bolum
VeriBilimci.bolum

#ornek metodlari

class VeriBilimci():
    calisanlar = []
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ''
        
    def dil_ekle(self, yeni_dil):
        self.bildigi_diller.append(yeni_dil)
        
        
ali = VeriBilimci()
ali.bildigi_diller
ali.bolum

veli = VeriBilimci()
veli.bildigi_diller
veli.bolum
        
dir(VeriBilimci)        

VeriBilimci.dil_ekle
VeriBilimci.dil_ekle("R")

ali.bildigi_diller("R")

veli.dil_ekle("Python")
veli.bildigi_diller
        
        
        













