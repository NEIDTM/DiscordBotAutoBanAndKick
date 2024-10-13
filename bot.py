import disnake
from disnake.ext import commands

# Установите ваш токен
TOKEN = ''
intents = disnake.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# Команда для кика всех участников сервера
@bot.command()
@commands.has_permissions(administrator=True)
async def kickall(ctx):
    guild = ctx.guild
    members = guild.members
    for member in members:
        if member != ctx.author and not member.bot:  # Не кикать себя и ботов
            try:
                await member.kick(reason="Mass kick command executed")
                await ctx.send(f'{member.name} был кикнут')
            except disnake.Forbidden:
                await ctx.send(f'У меня нет прав кикнуть {member.name}')
            except disnake.HTTPException:
                await ctx.send(f'Не удалось кикнуть {member.name}')

# Команда для бана всех участников сервера
@bot.command()
@commands.has_permissions(administrator=True)
async def banall(ctx):
    guild = ctx.guild
    members = guild.members
    for member in members:
        if member != ctx.author and not member.bot:  # Не банить себя и ботов
            try:
                await member.ban(reason="Mass ban command executed")
                await ctx.send(f'{member.name} был забанен')
            except disnake.Forbidden:
                await ctx.send(f'У меня нет прав забанить {member.name}')
            except disnake.HTTPException:
                await ctx.send(f'Не удалось забанить {member.name}')

# Событие при запуске бота
@bot.event
async def on_ready():
    print(f'{bot.user} подключен и готов!')

bot.run(TOKEN)
