# Produced by Buğra Akdemir
# Anyone can use this automation by making some changes, or you can add it directly to your server and use it without making any changes.
# - Link Required to Add This Automation to Your Server 👇
# https://discord.com/api/oauth2/authorize?client_id=1207017285181513789&permissions=8&scope=bot
# Autoamsyon's Support Server 👇
# https://discord.gg/m9SwQvQ8xh

# GitHub And İnstagram

# Zylles     S1r.bugra

# Kütüphaneler Başlangıç

import os
import discord
from discord.ext import commands
import src.info as info
import src.kurcm as kurcm
import src.kur as kur
import src.zBot_Token as zBot_Token
import time
import traceback
import src.utils as utils
import src.game as game
from src.game import *
from discord.ext import tasks
from datetime import *
import src.duyurular as duyurular
import random
import requests
import sqlite3
import random
import asyncio
import os
import openai
from bs4 import BeautifulSoup

# Kütüphaneler Bitiş

intents = discord.Intents.all()


class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(command_prefix='!', intents=intents, *args, **kwargs)


bot = MyBot()
game = Game()
bot.remove_command('help')
version = "v4.9.5"
my_token = zBot_Token.Token1
openai.api_key = "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"
LOG_FILE2 = os.path.join('log', 'açiliş_logu.txt')
log_klasörü = 'log/'

# Açılış Baş

@bot.event
async def on_ready():
    print(f"{version}")
    print(f"{bot.user} BOT AKTİF!!")
    await bot.change_presence(activity=discord.Game(name="!yardim"))
    await bot.tree.sync()
    embed = discord.Embed(title="BOT AKTİF 🟩", url="", description=f"BOT SÜRÜMÜ: {version}", color=0x00ff11)
    channetwo = bot.get_channel(1210577527957889034)
    await channetwo.send(embed=embed)
    bot_name = bot.user.name
    # Tarih ve saat bilgisini al
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Log mesajını oluştur
    log_message = f"{bot_name} {now} tarihinde aktif edildi\n"
    with open(LOG_FILE2, 'a', encoding="utf-8") as file:
        file.write(log_message)


# Açılış Bit

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed2 = discord.Embed(title="HATALI KOMUT", url="", description=f"{info.hata_m}", color=0xff0000)
        await ctx.send(embed=embed2)


@bot.command(name="yapımcı")
async def yapımcı(ctx):
    embed = discord.Embed(title="Buğra Akdemir", url="https://hey.link/lAyMz", description=f"", color=0xffff00)
    await ctx.send(embed=embed)


@bot.command(name="producer")
async def producer(ctx):
    embed = discord.Embed(title="Buğra Akdemir", url="https://hey.link/lAyMz", description=f"", color=0xffff00)
    await ctx.send(embed=embed)


# BİLGİ kumutları başlangıç
@bot.tree.command(name="yardim", description="Komutllari Gösterir")
async def slash_command(interaction: discord.Interaction):
    embed = discord.Embed(title="KOMUTLAR", url="", description=f"{info.bilgi}", color=0x2800ba)
    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="admink", description="Admin Komutllari Gösterir")
async def slash_command2(interaction: discord.Interaction):
    embed = discord.Embed(title="ADMİN KOMUTLARI", url="", description=f"{info.admink}", color=0xcfde02)
    await interaction.response.send_message(embed=embed)


#         "/" komutları bitiş
@bot.command(name="admin")
async def admin(ctx):
    embed = discord.Embed(title="ADMİN KOMUTLARI", url="", description=f"{info.admink}", color=0x090785)
    await ctx.send(embed=embed)


@bot.command(name="yardim")
async def yardim(ctx):
    embed = discord.Embed(title="YARDIM - HELP", url="", description=f"{info.bilgi}", color=0x090785)
    await ctx.send(embed=embed)

@bot.command(name="resim_bilgi")
async def resim_bilgi(ctx):
    embed = discord.Embed(title="Resim Komutları", url="", description=f"{info.resim_b}", color=0x090785)
    await ctx.send(embed=embed)

@bot.command(name="vidio_bilgi")
async def vidio_bilgi(ctx):
    embed = discord.Embed(title="Vidio Komutları", url="", description=f"{info.vidio_b}", color=0x090785)
    await ctx.send(embed=embed)

#@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="Yardım",
        description="Yardım komutları",
        color=discord.Color.blue()
    )
    embed.add_field(name="!normal", value=f"Herkesin Kullanabileceği\nKomutları Gösterir", inline=False)
    embed.add_field(name="!admin", value="ADMİNLERİN KULLANABİLECEĞİ KOMUTLARI GÖSTERİR", inline=False)
    embed.add_field(name="!oyunlar", value="Oyun Komutlarını Gösterir", inline=False)
    # Daha fazla komut ekleyebilirsiniz

    await ctx.send(embed=embed)


# OYUNLAR - GAME BAŞLANGIÇ
@bot.command(name="oyunlar")
async def oyunlar(ctx):
    embed = discord.Embed(title="OYUNLAR", url="", description=f"{info.oyunlar}", color=0x090785)
    await ctx.send(embed=embed)


@bot.command(name="games")
async def game(ctx):
    embed = discord.Embed(title="GAME", url="", description=f"{info.oyunlar}", color=0x090785)
    await ctx.send(embed=embed)


# OYUNLAR - GAME BİTİŞ
# VERSİON

@bot.command(name="version")
async def admin(ctx):
    embed = discord.Embed(title=f"{version}", url="", description=f"", color=0x090785)
    await ctx.send(embed=embed)


# NORMAL KOMUTLAR BAŞLANGIÇ-
@bot.command(name="normal")
async def normal(ctx):
    embed = discord.Embed(title="NORMAL KOMUTLAR", url="", description=f"{info.normalb}", color=0x090785)
    await ctx.send(embed=embed)


@bot.command(name="basic")
async def basic(ctx):
    embed = discord.Embed(title="BASİC", url="", description=f"{info.normalb}", color=0x090785)
    await ctx.send(embed=embed)


@bot.command(name="tkmk")
async def basic(ctx):
    embed = discord.Embed(title="TAŞ KAĞIT MAKAS", url="", description=f"{info.tkmk}", color=0x090785)
    await ctx.send(embed=embed)


# -NORMAL KOMUTLAR BİTİŞ-

# DAVET BAŞLANGIÇ
@bot.command(name="davet")
async def davet(ctx):
    embed = discord.Embed(title="DAVET LİNKİ",
                          url="https://discord.com/api/oauth2/authorize?client_id=1207017285181513789&permissions=8&scope=bot",
                          description=f"", color=0x090785)
    await ctx.send(embed=embed)


@bot.command(name="invitation")
async def invitation(ctx):
    embed = discord.Embed(title="DAVET LİNKİ",
                          url="https://discord.com/api/oauth2/authorize?client_id=1207017285181513789&permissions=8&scope=bot",
                          description=f"", color=0x090785)
    await ctx.send(embed=embed)


# -davet bitiş
# KUR-
@bot.command(name="kur")
async def kur(ctx, *args):
    if "tümü" in args:
        embed = discord.Embed(title="KURLAR",
                              url="",
                              description=f"{kurcm.kur_dl + kurcm.kur_eu + kurcm.kur_str}", color=0x0acc14)
        await ctx.send(embed=embed)
    elif "dolar" in args:
        embed = discord.Embed(title="DOLAR",
                              url="",
                              description=f"{kurcm.kur_dl}", color=0x0acc14)
        await ctx.send(embed=embed)
    elif "euro" in args:
        embed = discord.Embed(title="Euro",
                              url="",
                              description=f"{kurcm.kur_eu}", color=0x0acc14)
        await ctx.send(embed=embed)
    elif "i-sterlin" in args:
        embed = discord.Embed(title="İNGİLİZ STERLİNİ",
                              url="",
                              description=f"{kurcm.kur_str}", color=0x0acc14)
        await ctx.send(embed=embed)
    else:
        await ctx.send(
            "!kur yazdiktan sonra \n istediğiniz kuru girin\n!kur tümü\n!kur euro\n!kur dolar\n!kur i-sterlin")


# -oyun-
@bot.command(name="oyun")
async def oyun(ctx, *args):
    if "zar" in args:
        await ctx.send("ZAR")
        await ctx.send(game.roll_dice())
    else:
        await ctx.send("YANLIŞ KOMUT!!")


# -mesaj sil-
@bot.command(name="sil")
@commands.has_role("Admin")
async def sil(ctx, amount=50):
    await ctx.channel.purge(limit=amount)


@bot.command(name="clear")
@commands.has_role("Admin")
async def clear(ctx, amount=50):
    await ctx.channel.purge(limit=amount)


# KULLANCI ATMA
@bot.command(name="at")
@commands.has_role("Admin")
async def at(ctx, member: discord.Member, *args, reason="YOK"):
    await member.kick(reason=reason)


@bot.command(name="kick")
@commands.has_role("Admin")
async def kick(ctx, member: discord.Member, *args, reason="YOK"):
    await member.kick(reason=reason)


# -ban
@bot.command(name="ban")
@commands.has_role("Admin")
async def ban(ctx, member: discord.Member, *args, reason="YOK"):
    await member.ban(reason=reason)


# -unban-
@bot.command(name="unban")
@commands.has_role("Admin")
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for bans in banned_users:
        user = bans.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.mention} KULLANICISININ  BANI KALKTI')
            return


# -ping-
@bot.command()
async def ping(ctx):
    await ctx.send(f'Pingim : `{bot.latency * 1000}`ms')

LOG_FILE4 = ("log" ,"user_logs.txt")

# Otomatik ROL VERME VE HOŞGELDİN MESAJI ve log
@bot.event
async def on_member_join(member):
    kayıt_role = member.guild.get_role(1208406371142344734)
    await member.add_roles(kayıt_role)
    await member.guild.get_channel(1208420167025954908).send(
        f"{member.mention} HOŞ GELDİN. {kayıt_role.mention} Rolünüz verildi")

# -GÜLE GÜLE MESAJI
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1208420167025954908)
    emb = discord.Embed(title=f"GÜLE GÜLE {member.name}")
    await channel.send(embed=emb)


# KAYIT BİLGİ
@bot.command()
async def destek(ctx):
    await ctx.send("AKD BOT RESMİ DİSCORD SUNUCUSU\n\nhttps://discord.gg/m9SwQvQ8xh")


# ROL VERME

@bot.command(pass_context=True)
@commands.has_role("Admin")
async def rolver(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    await ctx.send(f"{ctx.author.name} tarifindan {user.name} şu rol verildi:: {role.name}")

# adam asmaca

# Adam asmaca için kelime listesi
kelimeler = ["python", "programlama", "discord", "yapayzeka", "makineogrenmesi", "telefon", "bilgisayar", "google",
             "internet", "oyun"]


# Adam asmaca oyununu başlatan fonksiyon
async def adam_asmaca(ctx):
    kelime = random.choice(kelimeler).lower()  # Rastgele bir kelime seç
    tahmin_edilenler = []  # Tahmin edilen harflerin listesi
    can = 6  # Kullanıcının tahmin hakkı sayısı

    # Oyunun başlangıç mesajı
    await ctx.send("Adam asmaca oyununa hoş geldiniz! Kelimeyi tahmin etmek için harfleri yazın.")

    # Kelimeyi oluşturmak için "_" ile doldurulmuş hali
    kelime_gorunumu = "_ " * len(kelime)

    # Oyun döngüsü
    while can > 0:
        # Kelimenin görünümünü ve kalan canı göster
        await ctx.send(f"Kelime: {kelime_gorunumu}\nKalan can: {can}")

        # Kullanıcının bir harf girmesini bekleyin
        try:
            tahmin = await bot.wait_for("message", timeout=30.0,
                                        check=lambda m: m.author == ctx.author and m.content.isalpha())
            harf = tahmin.content.lower()
        except TimeoutError:
            await ctx.send("Zaman doldu! Oyun sona erdi.")
            return

        # Tahmin edilen harfi kontrol et
        if harf in tahmin_edilenler:
            await ctx.send("Bu harfi zaten tahmin ettiniz!")
            continue
        elif harf in kelime:
            tahmin_edilenler.append(harf)
            kelime_gorunumu = " ".join([h if h in tahmin_edilenler else "_" for h in kelime])
            if "_ " not in kelime_gorunumu:
                await ctx.send(f"Tebrikler! Kelimeyi doğru tahmin ettiniz. Kelime: {kelime}")
                return
        else:
            can -= 1
            await ctx.send(f"Bu harf kelime içinde değil. Kalan can: {can}")

    await ctx.send(f"Üzgünüm, can hakkınız bitti. Doğru kelime: {kelime}")


@bot.command(name="adamasmaca")
async def komut_adam_asmaca(ctx):
    await adam_asmaca(ctx)


# adam asmaca bitiş
# taş kağıt makas

@bot.command(name="tkm")
async def tkm(ctx, secim: str):
    await ctx.send("Lütfen  bir seçim yapın: taş, kağıt veya makas.")
    secimler = ["taş", "kağıt", "makas"]
    bot_secimi = random.choice(secimler)

    if secim not in secimler:
        await ctx.send("Lütfen geçerli bir seçim yapın: taş, kağıt veya makas.")
        return

    if secim == bot_secimi:
        await ctx.send(f"Ben de {bot_secimi}. Berabere!")
    elif (secim == "taş" and bot_secimi == "makas") or \
            (secim == "kağıt" and bot_secimi == "taş") or \
            (secim == "makas" and bot_secimi == "kağıt"):
        await ctx.send(f"Ben {bot_secimi}. Kazandın!")
    else:
        await ctx.send(f"Ben {bot_secimi}. Kaybettin!")


# taş kağıt makas bitiş

#        kullanıcı kayıt 

# Veritabanı bağlantısı oluşturma
klasor_yolu = "db"

veritabani_yolu = os.path.join(klasor_yolu, "kullanici_bilgileri.db")

conn = sqlite3.connect(veritabani_yolu)

cursor = conn.cursor()

# Kullanıcı tablosunu oluşturma
cursor.execute('''CREATE TABLE IF NOT EXISTS kullanicilar (
                kullanici_id INTEGER PRIMARY KEY,
                ad TEXT,
                soyad TEXT,
                yas INTEGER
                )''')
conn.commit()


# 'kayit' komutu
@bot.command()
async def kayit(ctx, ad: str, soyad: str, yas: int):
    kullanici_id = ctx.author.id
    cursor.execute("INSERT INTO kullanicilar (kullanici_id, ad, soyad, yas) VALUES (?, ?, ?, ?)",
                   (kullanici_id, ad, soyad, yas))
    conn.commit()
    await ctx.send("Başarıyla kaydedildi!")


# 'k_bilgi' komutu
@bot.command()
@commands.has_role("Admin")
async def k_bilgi(ctx, hedef_kullanici: discord.Member):
    kullanici_id = hedef_kullanici.id
    cursor.execute("SELECT ad, soyad, yas FROM kullanicilar WHERE kullanici_id = ?", (kullanici_id,))
    veri = cursor.fetchone()
    if veri is not None:
        ad, soyad, yas = veri
        await ctx.send(f"{hedef_kullanici.name}'in Bilgileri:\nAdı: {ad}\nSoyadı: {soyad}\nYaşı: {yas}")
    else:
        await ctx.send("Kullanıcı bilgisi bulunamadı.")


#      kullanıcı kayıt bitiş

# log komutu başlangıç

LOG_FILE0 = os.path.join('log', 'komut_logu.txt')


@bot.event
async def on_message(message):
    # Kullanıcının adını ve kullanılan komutu al
    log_message = f"{message.author.name} kullanicisi: {message.content} komutunu kullandi\n"

    # Log dosyasına yaz
    with open(LOG_FILE0, 'a', encoding="utf-8") as file:
        file.write(log_message)
    # Komutları işle
    await bot.process_commands(message)

#fdgdfg

# Log dosyasının adı
LOG_FILE5 = os.path.join('log', 'message_logs.txt')

# Kullanıcı mesajlarını loglama
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    

    now = datetime.now()
    current_time = now.strftime("%d/%m/%Y %H:%M:%S")
    with open(LOG_FILE5, "a", encoding="utf-8") as log_file:
        log_file.write(f"{message.author.name}: {message.content} ,{current_time}\n")
    await bot.process_commands(message)

#seviye sistemi

conn = sqlite3.connect('db/seviye.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS levels (
             user_id INTEGER PRIMARY KEY,
             level INTEGER
             )''')
conn.commit()

# level sistemi

@bot.command()
async def seviye(ctx, user: discord.Member):
    c.execute("SELECT level FROM levels WHERE user_id = ?", (user.id,))
    row = c.fetchone()
    if row:
        await ctx.send(f"{user.name} adlı kullanıcının seviyesi: {row[0]}")
    else:
        await ctx.send("Belirtilen kullanıcının seviyesi: 0'")

message_count = {}

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    author_id = message.author.id
    if author_id not in message_count:
        message_count[author_id] = 10
    else:
        message_count[author_id] = message_count[author_id] + 1

    if message_count[author_id] % 20 == 0:
        c.execute("SELECT level FROM levels WHERE user_id = ?", (author_id,))
        row = c.fetchone()
        if row is None:
            c.execute("INSERT INTO levels (user_id, level) VALUES (?, ?)", (author_id, 1))
        else:
            c.execute("UPDATE levels SET level = level + 1 WHERE user_id = ?", (author_id,))
        conn.commit()

    await bot.process_commands(message)

# seviye verme

@bot.command()
@commands.has_role("Admin")  # Sadece "ADMİN" adında bir rolü olanlar bu komutu kullanabilirs
async def seviye_ver(ctx, user: discord.Member, level: int):
    c.execute("SELECT * FROM levels WHERE user_id = ?", (user.id,))
    row = c.fetchone()
    if row:
        c.execute("UPDATE levels SET level = ? WHERE user_id = ?", (level, user.id))
    else:
        c.execute("INSERT INTO levels (user_id, level) VALUES (?, ?)", (user.id, level))
    
    conn.commit()
    
    await ctx.send(f"{user.name} adlı kullanıcıya seviye {level} verildi.")

# resim kaydetme


img_folder = "img"

@bot.command()
async def resim(ctx):
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    await ctx.send("Lütfen bir resim gönderin.")
    message = await bot.wait_for('message', check=check)
    if len(message.attachments) > 0:
        attachment = message.attachments[0]
        await attachment.save(f"{img_folder}/{attachment.filename}")
        await ctx.send("Resim başarıyla kaydedildi.")
    else:
        await ctx.send("Lütfen bir resim gönderin.")

@bot.command()
async def resim_bul(ctx, resim_ismi: str):
    if os.path.exists(f"{img_folder}/{resim_ismi}"):
        with open(f"{img_folder}/{resim_ismi}", 'rb') as file:
            picture = discord.File(file)
            await ctx.send(file=picture)
    else:
        await ctx.send("Belirtilen isimde bir resim bulunamadı.")


@bot.command()
async def resimler(ctx):
    resimler = os.listdir(img_folder)
    resim_listesi = "\n".join(resimler)
    await ctx.send(f"Kayıtlı resimler:\n{resim_listesi}")


if not os.path.exists(img_folder):
    os.makedirs(img_folder)

#vidio kayıt

video_folder = "vid"

@bot.command()
async def vidio(ctx):
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    await ctx.send("Lütfen bir video gönderin.")
    message = await bot.wait_for('message', check=check)
    if len(message.attachments) > 0:
        attachment = message.attachments[0]
        await attachment.save(f"{video_folder}/{attachment.filename}")
        await ctx.send("Video başarıyla kaydedildi.")
    else:
        await ctx.send("Lütfen bir video gönderin.")

@bot.command()
async def vidio_bul(ctx, video_ismi: str):
    if os.path.exists(f"{video_folder}/{video_ismi}"):
        await ctx.send(file=discord.File(f"{video_folder}/{video_ismi}"))
    else:
        await ctx.send("Belirtilen isimde bir video bulunamadı.")

@bot.command()
async def vidiolar(ctx):
    videolar = os.listdir(video_folder)
    video_listesi = "\n".join(videolar)
    await ctx.send(f"Kayıtlı videolar:\n{video_listesi}")

if not os.path.exists(video_folder):
    os.makedirs(video_folder)

try:
    bot.run(my_token)
except TypeError:
    print("Tokeni Kontrol Et")