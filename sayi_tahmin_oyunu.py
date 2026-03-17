import random
sayi = random.randint(1,100) # bilgisayar 1'den 100'e kadar rastgele bir sayı tutar.  (100 dahil)

tahmin = int(input("Lütfen bir sayı tahmin ediniz : "))
sayac = 0

while sayi != tahmin:
    if(sayi > tahmin):
        print("Daha yüksek bir sayı tahmin ediniz.")
        sayac += 1
        tahmin = int(input("Lütfen bir sayı tahmin ediniz : "))
    elif(sayi < tahmin):
        print("Daha düşük bir sayı tahmin ediniz.")
        sayac += 1
        tahmin = int(input("Lütfen bir sayı tahmin ediniz : "))


print(f'Tahmininiz doğru. Sayı = {sayi}  {sayac+1}. tahminde bildiniz.')
