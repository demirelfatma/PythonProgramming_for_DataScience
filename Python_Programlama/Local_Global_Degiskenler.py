# Local ve Global Degiskenler
#global degiskenler ana calisma alanimizdekiler
#lokal degiskenler bir fonksiyon, metot alaninda bulunanlar

x = 20 #global
y = 20

def carpma_yap(x,y): #local
    return x*y

carpma_yap(2, 3)

# local etki alanindan global etki alanini degistirmek

x = [] #boş liste []->liste isareti

def eleman_ekle(y):
    x.append(y)
    print(str(y)+" ifadesi eklendi")
    
x.append(1)
print(x)
eleman_ekle("13")
print(x)



















































