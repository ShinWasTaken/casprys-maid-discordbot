import disnake
import os 
from typing import Optional
from py_dotenv import read_dotenv
from saucenao_api import SauceNao
from disnake.ext import commands

class Sauce(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def sauce(self, inter: disnake.ApplicationCommandInteraction, file: Optional[disnake.Attachment] = None, url: Optional[str]="",):
        """SFX Sauce command do not use this for NSFW content there is another command for that""" 
        dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
        read_dotenv(dotenv_path)    

        API_KEY = os.getenv("API_KEY")
        sauce = SauceNao(api_key=API_KEY)
        answer = sauce.from_url(url=url)

        await inter.response.send_message(f"Anime/Character/Manga name is {answer[0].title}\n{answer[0].thumbnail}")

def setup(bot: commands.Bot):
    bot.add_cog(Sauce(bot))