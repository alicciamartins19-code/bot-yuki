import discord
from discord.ext import commands
import os

TOKEN = os.getenv("TOKEN")
WELCOME_CHANNEL_ID = int(os.getenv("WELCOME_CHANNEL_ID"))

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print("=" * 40)
    print(f"✅ Bot conectado como {bot.user}")
    print("=" * 40)


@bot.event
async def on_member_join(member):
    canal = bot.get_channel(WELCOME_CHANNEL_ID)

    if canal is None:
        return

    embed = discord.Embed(
        title="🎉 Bem-vindo(a)!",
        description=(
            f"Olá {member.mention}! 👋\n\n"
            "Seja muito bem-vindo(a) à nossa comunidade!\n\n"
            "🔴 Fique de olho nas lives.\n\n"
            "Esperamos que você tenha uma ótima experiência!"
        ),
        color=discord.Color.red()
    )

    embed.add_field(
        name="👥 Membros",
        value=f"Agora somos **{member.guild.member_count}** membros!",
        inline=False
    )

    embed.set_footer(text="Yukizona")

    arquivo = discord.File("banner.png", filename="banner.png")
    embed.set_image(url="attachment://banner.png")

    await canal.send(
        content=member.mention,
        embed=embed,
        file=arquivo
    )


bot.run(TOKEN)
