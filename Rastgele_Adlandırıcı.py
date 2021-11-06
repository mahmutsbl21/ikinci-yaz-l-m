import random
import time
print('_______________')
print('SELAM KULLANICI|')
print('_______________|')
time.sleep(1.25)
print('Haydi başlayalım')
print('________________')
time.sleep(1.25)
print('               |')
print('               |')
print(' -_-_-_-_-_-_-_-')
print(' |')
print('\ /')
time.sleep(1.24)
print('Uyarı: BU RASTGELE YAPILANDIRILAN İSİM VE SOYADLARI KÖTÜ AMAÇLAR İÇİN KULLANMAYINIZ.')
time.sleep(2.30)
print('Herhangi bir siber saldırıda biz sorumlu değiliz!')
yapan_kişi = 'Mahmut'
soyadı = 'Sibal'
time.sleep(1.25)
print('AD=')
time.sleep(1.10)
name1 = 'Nazlı'
print('1.Nazlı')
time.sleep(1.10)
name2 = 'Ahmet'
print('2.Ahmet')
time.sleep(1.10)
name3 = 'Aslı'
print('3.Aslı')
time.sleep(1.10)
name4 = 'Arda'
print('4.Arda')
time.sleep(1.10)
name5 = 'Aylin'
print('5.Aylin')
time.sleep(1.10)
name6 = 'Muhammed'
print('6.Muhammed')
time.sleep(1.10)
name7 = 'İlknur'
print('7.İlknur')
time.sleep(1.10)
name8 = 'Mustafa'
print('8.Mustafa') 
time.sleep(1.10)
name9 = 'Dilara'
print('9.Dilara')
time.sleep(1.10)
name10 = 'Alican'
print('10.Alican')
time.sleep(1.10)
name11 = 'Aliye'
print('11.Aliye')
time.sleep(1.10)
name12 = 'Yusuf'
print('12.Yusuf')
time.sleep(1.10)
name13 = 'Esra'
print('13.Esra')
time.sleep(1.10)
name14 = 'Emirhan'
print('14.Emirhan')
time.sleep(1.10)
name15 = 'Emine'
print('15.Emine')
time.sleep(1.10)
name16 = 'Emin'
print('16.Emin')
time.sleep(1.10)
name17 = 'Ece'
print('17.Ece')
time.sleep(1.10)
print('--------------------')
time.sleep(1.10)
print('SOYAD=')
time.sleep(1.10)
surname1 = 'Yılmaz'
print('1.Yılmaz')
time.sleep(1.10)
surname2 = 'Aydın'
print('2.Aydın')
time.sleep(1.10)
surname3 = 'Kurt'
print('3.Kurt')
time.sleep(1.10)
surname4 = 'Yıldırım'
print('4.Yıldırım')
time.sleep(1.10)
surname5 = 'Esen'
print('5.Esen')
time.sleep(1.10)
surname6 = 'Korhan'
print('6.Korhan')
time.sleep(1.10)
surname7 = 'Aslan'
print('7.Aslan')
time.sleep(1.10)
surname8 = 'Arslan'
print('8.Arslan')
time.sleep(1.10)
surname9 = 'Gece'
print('9.Gece')
time.sleep(1.10)
surname10 = 'Gündüz'
print('10.Gündüz')
time.sleep(1.10)
surname11 = 'Dalmızrak'
print('11.Dalmızrak')
time.sleep(1.10)
surname12 = 'Can'
print('12.Can')
time.sleep(0.50)
Name_list = [name1, name2, name3, name4, name5, name6, name7, name8, name9, name10, name11, name12, name13, name14, name15, name16, name17] 

Surname_list = [surname1, surname2, surname3, surname4, surname5, surname6, surname7, surname8, surname9, surname10, surname11, surname12]

def ask():
    global start

    print(' ')
    start = input('Başlamak icin {Basla} yazınız: ')
    print(' ')

ask()

if(start == 'Basla'): 
    print('Yükleniyor...') 
    time.sleep(1.25) 
    print('╭━┳━╭━╭━╮')
    time.sleep(1.25)
    print('┃┈┈┈┣▅╋▅┫┃')
    time.sleep(1.25)
    print('┃┈┃┈╰━╰━━━━━━╮')
    time.sleep(1.25)
    print('╰┳╯┈┈┈┈┈┈┈┈┈◢▉◣')
    time.sleep(1.25)
    print('╲┃┈┈┈┈┈┈┈┈┈┈▉▉▉')
    time.sleep(1.25)
    print('╲┃┈┈┈┈┈┈┈┈┈┈◥▉◤')
    time.sleep(1.25)
    print('╲┃┈┈┈┈╭━┳━━━━╯')
    time.sleep(1.25)
    print('╲┣━━━━━━┫')
    time.sleep(1.25)
    print('╲┃┈┈┈┈┈┈┃')
    time.sleep(1.25)
    print('__________')
    print('By=OrGan MaFyAsı')
    rime.sleep(1.25)
    print('Yüklendi!') 
    print('-------------') 
    print('Rastgele isim yapıldı: ')
    print(random.choice(Name_list))
    print(random.choice(Surname_list))
    print('----------------')
    print('kurucusu',yapan_kişi,soyadı)
    print('-------------') 
elif(start != 'y'): 
    print('-------------') 
    ask() 
    print('-------------')