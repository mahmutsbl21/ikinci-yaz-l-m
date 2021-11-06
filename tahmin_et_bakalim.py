import random
import time
import os
print("____________________")
time.sleep(1.10)
print('sayı tahmin et oyunu\n->HOŞGELDİNİZ')
print("-----------")
time.sleep(2.30)
print("şimdi ben bir sayı yazdım")
time.sleep(2.30)
print("-------------------------")
print("sende o sayıyı bulacaksın")
time.sleep(2.30)
başla = input("tamam mı?: ")
print("-----")
if(başla == 'tamam'):
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
    numbers=random.randint(1,30)
    time.sleep(3)
    os.system('clear')
    print(numbers,"sayı")
    time.sleep(1.45)
    os.system('clear')
    for i in range(3):

        time.sleep(0.50)
        playernumbers=int(input('1 ile 30 arası bir sayı yazın: '))


        while True:
                if playernumbers > numbers:
                
                    time.sleep(1.15)
                    print("Bekleyin")
                    time.sleep(1.15)
                    
                    playernumbers=int(input("İpucu;daha küçük bir sayı seçiniz: "))
                elif playernumbers < numbers:
                
                    time.sleep(1.15)
                    print("Bekleyin")
                    time.sleep(1.15)
                    
                    playernumbers=int(input("İpucu;daha büyük bir sayı seçiniz: "))
            
                if playernumbers == numbers:
                    time.sleep(1.15)
                    print("Bekleyin")
                    time.sleep(1.15)
                    print("Tebrikler oyunu kazandınız\n Haydi tekrar")
                time.sleep(2.30)
                os.system('clear')
                break
        break
                    