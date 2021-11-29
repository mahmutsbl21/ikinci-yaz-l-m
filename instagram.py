from instabot import Bot
import time

bot = Bot()

username = input("kullanıcı adın? ")
password = input("şifren? ")
kişi = input("kime mesaj atcan? ")

# Giriş yapma
bot.login(username=username, password=password)


# Günaydın mesajı atma fonksiyonu
def gunaydin():
    message = "Günaydın  "
    friend = [kişi]

    bot.send_message(message, friend)