import instaloader
import pandas as pd



bot = instaloader.Instaloader()


nick = input("Kullanıcı adı: ")
profile = instaloader.Profile.from_username(bot.context, f"{nick}")

print("Username: ", profile.username)

print("User ID: ", profile.userid)

print("Number of Posts: ", profile.mediacount)

print("Followers Count: ", profile.followers)

print("Following Count: ", profile.followees)

print("Bio: ", profile.biography)

print("External URL: ", profile.external_url)

isim = (f"İsim: {profile.username}")
iis = (f"Kullanıcı İd: {profile.userid}")
postn = (f"Toplam Atılan Post: {profile.mediacount}")
takpçi = (f"Takipçi Sayısı: {profile.followers}")
takip = (f"Takip Edilen: {profile.followees}")
bio = (f"Biyogrofi: {profile.biography}")
