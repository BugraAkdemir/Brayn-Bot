from discord_webhook import DiscordWebhook, DiscordEmbed
import time
import datetime 
import src.kurcm as kurcm



x = datetime.datetime.now()
webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1208441759810719754/y3MC_dp0OWcq9I6l3IICQn21Epq9IKKUyqhPuV00nigFEjGCMKqLaL-fLbymRybqyKXn")
embed = DiscordEmbed(title=f"{"MERHABAw"}", description=f"SAAT VE TARİH\n{x}", color="090785")
webhook.add_embed(embed)
response = webhook.execute()