NIM= int(input("masukan NIM tanpa 0 di depan : "))
loop=int(input("berapa banyak yang ingin di tampilkan : "))
JH = 0

print("jumlah angka NIM yang di tampilkan dalam bilangan genap ")
while (JH < loop):
        if (NIM % 2) ==0:
                print(NIM)
        JH += 1
        NIM += 1
print ("TERIMAKASIH")
