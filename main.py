import random
rastgelesayi=random.randint(1,100)
print('Bilgisayar 0 ile 100 arasında bir sayı seçti. Sende 3 sayı seçeceksin ve bunların toplamının blgisayarın seçtiği sayıya eşit olmasını sağlayacaksın.5 hakkın var"nıı')
tahmin=0
while True:
    sayi1 = int(input('1. sayıyı giriniz:'))
    sayi2 = int(input('2. sayıyı giriniz:'))
    sayi3 = int(input('3. sayıyı giriniz:'))
    toplam=sayi1+sayi2+sayi3
    if rastgelesayi==toplam:
        tahmin+=1
        print('doğru bildin')
        print(tahmin,'tahminde bildin')
        break
    elif toplam>rastgelesayi:
        tahmin+=1
        print('daha küçük sayılar girmelisin')
    else:
        tahmin+=1
        print('daha büyük sayılar girmelisin')
    if tahmin==5:
        print('kaybettin')
        print('bilgisayarın tahmini',rastgelesayi)
        break

