#Konversi Suhu (C/F/K)

#fungsi untuk mengkonversi nilai celcius menjadi fahrenheit dan kelvin
def convert_c (degree):
    fahr = (9/5 * degree) + 32
    kelv = degree + 273.15
    print("Suhu dalam Fahrenheit: ", fahr, " F")
    print("Suhu dalam Kelvin: ", kelv, " K")
    return;

#fungsi untuk mengkonversi nilai fahrenheit menjadi celcius dan kelvin
def convert_f (degree):
    cels = (degree - 32) * (5/9)
    kelv = ((degree - 32) * (5/9)) + 273.15
    print("Suhu dalam Celcius: ", cels, " C")
    print("Suhu dalam Kelvin: ", kelv, " K")
    return;

#fungsi untuk mengkonversi nilai kelvin menjadi celcius dan fahrenheit
def convert_k (degree):
    fahr = ((degree - 273.15) * (9/5)) + 32
    cels = degree - 273.15
    print("Suhu dalam Fahrenheit: ", fahr, " F")
    print("Suhu dalam Celcius: ", cels, " C")
    return;

#user input suhu yang akan dikonversi
temp = input("Suhu yang ingin dikonversi (C/F/K): ")
degree = float(input("Derajat temperatur suhu: "))

#menampilkan kembali besaran dan satuan suhu yang diinput oleh user untuk dikonversikan
print("Suhu yang dikonversi: ", degree , temp)


if temp.lower() == "c":
    convert_c(degree)
elif temp.lower() == "f":
    convert_f(degree)
elif temp.lower() == "k":
    convert_k(degree)
else:
    print("Error, input c/f/k only")