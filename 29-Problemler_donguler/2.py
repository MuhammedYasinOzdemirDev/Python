"""Problem 2
Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.

Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4
    """
sayi = input("sayi giriniz:")
us = len(sayi)
toplam = 0
for i in sayi:
    toplam += int(i)**us
if str(toplam) == sayi:
    print("{} sayısı armstrong sayı".format(toplam))
else:
    print("{} sayısı armstrong sayı değildir".format(sayi))
