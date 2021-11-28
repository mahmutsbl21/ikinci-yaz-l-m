import time
import os
import random

resim = ["""
   +---+
   |   |
       |
       |
       |
       |
--------""","""
   +---+
   |   |
   O   |
       |
       |
       |
--------""","""
   +---+
   |   |
   O   |
   |   |
       |
       |
--------""","""
   +---+
   |   |
   O   |
  /|   |
       |
       |
--------""","""
   +---+
   |   |
   O   |
  /|  |
       |
       |
--------""","""
   +---+
   |   |
   O   |
  /|  |
  /    |
       |
--------""","""
   +---+
   |   |
   O   |
  /|  |
  /   |
       |
--------"""]

while True:
    print(("----->") + "Adam Asmaca Oyunu" + ("<-----"))
    
    kelime = random.choice(["a","b","c","d","e","f","g","h","k","l","m","n","o","s","t","v","y","z"])
    adim = 1
    tahmin = []
   
    
    while True:
        print(resim[adim])
        
        for i, char in enumerate(kelime):
            print(char if i in tahmin else "_________________"),
            
        cevap = input("Harf tahmin edin: ")
        
        if cevap == kelime:
            print("Kazandınız!")
            break
        else:
            while True:
                rastgele = random.randint(0, len(kelime,))
                
                if not rastgele in tahmin:
                    tahmin.append(rastgele)
                    break
            
            adim += 1
            os.system('clear')
        if adim >= len(resim):
            print("Kaybettiniz!")
            break
        
    if not "y" == input("Tekrar Oynamak İstermisiniz? (y/n): "):
        break