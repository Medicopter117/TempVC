from ui.emojis import emoji_no, emoji_yes
import discord


ERROR_TITLE = f"{emoji_no} × Fehler"
ERROR_COLOR = discord.Color.red()
ERROR_DESCRIPTION = "Es ist ein Fehler aufgetreten. Bitte versuche es später erneut oder kontaktiere den Support."

SUCCESS_TITLE = f"{emoji_yes} × Erfolg"
SUCCESS_COLOR = discord.Color.green()
SUCCESS_DESCRIPTION = "Die Aktion wurde erfolgreich abgeschlossen."

INFO_COLOR = discord.Color.blue()

AUTHOR = "ManagerX"
FLOOTER = "Powered by ManagerX"