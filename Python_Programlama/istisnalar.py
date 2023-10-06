# Istisnalar(excepsions)-Hatalar

a = 10
b = 0

# a/b - ZeroDivisionError: division by zero

try:
    print(a/b)
except ZeroDivisionError:
    print('Payda da sifir olamaz')
    

# tip hatasi

a = 10
b = "2"

# a/b - TypeError: unsupported operand type(s) for /: 'int' and 'str'

try:
    print(a/b)
except TypeError:
    print("Sayi ve String problemi")
    