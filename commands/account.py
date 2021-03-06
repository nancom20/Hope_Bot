import asyncio
import discord, json
from discord.ext import commands, tasks
from collections import OrderedDict

class games(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name= 'κ°μ')
    async def account(self, ctx):
        # user_tag = ctx.author.discriminator
        user_id = ctx.author.id
        user_name = ctx.author.name
        emoji = ['π©', 'π₯']

        with open('user.json', 'r', encoding='utf-8') as f: user_data = json.load(f)

        if f'{user_id}' in user_data:
            embed = discord.Embed(color= 0xec4747)
            embed.set_author(name="ν¬λ§λ΄", icon_url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png")
            embed.add_field(name="μ€...", value="μ΄λ―Έ κ°μ λΌμλ€μ............", inline=True)
            await ctx.channel.send(embed=embed)

        else:
            embed = discord.Embed(color= 0xfbb907)
            embed.set_author(name="ν¬λ§λ΄", icon_url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png")
            embed.add_field(name="κ°μ", value="λ­ μ μ₯νλκ±΄ λλ€μκ³Ό μμ΄λ λ°μ μμ΄μ Β―\_(γ)_/Β―", inline=True)
            embed.add_field(name="γγγ", value="λμνμ§ μμΌλ©΄ μ΄μ©ν λ μΌλΆμ νμ΄ μμ μλ μμ΄μ", inline=False)
            msg = await ctx.channel.send(embed=embed)
            await msg.add_reaction('π©')
            await msg.add_reaction('π₯')

            def check(reactin, user):
                return str(reactin) in emoji and user == ctx.author and reactin.message.id == msg.id
            try:
                reactin, _user = await self.bot.wait_for(event='reaction_add', timeout=15.0, check=check)
            except asyncio.TimeoutError:
                embed = discord.Embed(color= 0xfbb907)
                embed.set_author(name="ν¬λ§λ΄", icon_url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png")
                embed.add_field(name="μ΄μ.........", value="ν ..νμΌμ", inline=True)
                await msg.edit(embed=embed)
            else:
                if str(reactin) == 'π©':
                    Information = OrderedDict()
                    user_Information = OrderedDict()
                    user_Information["name"] = user_name
                    user_Information["money"] = 100
                    user_Information["levels"] = 1
                    user_Information["exp"] = 0
                    user_Information["atk"] = 1
                    user_Information["def"] = 1
                    user_Information["hp"] = 100
                    user_Information["hunger"] = 100
                    user_Information["item"] = {'weapon': 3, 'armor': 4, 'totem': 1, 'secondary_weapon': 0}
                    user_Information["fish"] = {'salmon': 0, 'Mackerel': 0, 'tuna': 0, 'cod': 0, 'Clownfish': 0, 'goldfish': 0}
                    user_Information["Inventory"] = {'0': {'id': 0, 'amount': 1}, '1': {'id': 0, 'amount': 1}, '2': {'id': 0, 'amount': 1}, '3': {'id': 0, 'amount': 1}, '4': {'id': 0, 'amount': 1}, '5': {'id': 0, 'amount': 1}, '6': {'id': 0, 'amount': 1}, '7': {'id': 0, 'amount': 1}, '8': {'id': 0, 'amount': 1}, '9': {'id': 0, 'amount': 1}}
                    Information[user_id] = user_Information
                    user_data.update(Information)

                    with open('user.json', 'w', encoding='utf-8') as outfile: json.dump(user_data , outfile, indent=4)
        
                    embed = discord.Embed(color= 0xfbb907)
                    embed.set_author(name="ν¬λ§λ΄", icon_url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png")
                    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png")
                    embed.add_field(name="μ°μμμμ°", value="κ°μ μλ£!", inline=True)
                    await msg.edit(embed=embed)    
                elif str(reactin) == 'π₯':
                    embed = discord.Embed(color= 0xfbb907)
                    embed.set_author(name="ν¬λ§λ΄", icon_url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png")
                    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png")
                    embed.add_field(name="νμ΄", value="γ ", inline=True)
                    await msg.edit(embed=embed)

    @commands.command(name= 'νν΄')
    async def secession(self, ctx):
        user_id = ctx.author.id
        user_name = ctx.author.name
        emoji = ['π©', 'π₯']

        with open('user.json', 'r', encoding='utf-8') as f: user_data = json.load(f)

        if f'{user_id}' in user_data:
            embed = discord.Embed(color= 0xfbb907)
            embed.set_author(name="ν¬λ§λ΄", icon_url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png",)
            embed.add_field(name="γ......", value="μ§μ§λ‘ νν΄νμ€κ±΄κ°μ", inline=True)
            msg = await ctx.channel.send(embed=embed)
            await msg.add_reaction('π©')
            await msg.add_reaction('π₯')

            def check(reactin, user):
                return str(reactin) in emoji and user == ctx.author and reactin.message.id == msg.id

            try:
                reactin, _user = await self.bot.wait_for(event='reaction_add', timeout=15.0, check=check)

            except asyncio.TimeoutError:
                embed = discord.Embed(color= 0xfbb907)
                embed.set_author(name="ν¬λ§λ΄", icon_url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png",)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png")
                embed.add_field(name="μ΄μ.........", value="ν γνμΌμ", inline=True)
                await msg.edit(embed=embed)

            else:
                if str(reactin) == 'π©':
                    embed = discord.Embed(color= 0xfbb907)
                    embed.set_author(name="ν¬λ§λ΄", icon_url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png",)
                    embed.add_field(name="νμ΄", value="μ±κ³΅μ μΌλ‘ νν΄νμμ μΈμ  κ° λ€μ μμ γ ", inline=True)
                    await msg.edit(embed=embed)

                    del user_data[f"{user_id}"]
                    with open('user.json', 'w', encoding='utf-8') as outfile: json.dump(user_data , outfile, indent=4)
                elif str(reactin) == 'π₯':
                    embed = discord.Embed(color= 0xfbb907)
                    embed.set_author(name="ν¬λ§λ΄", icon_url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png",)
                    embed.add_field(name="γ ", value=":sob:", inline=True)
                    await msg.edit(embed=embed)

        else:
            embed = discord.Embed(color= 0xec4747)
            embed.set_author(name="ν¬λ§λ΄", icon_url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png",)
            embed.add_field(name="?", value="νν΄ν  κ³μ μ΄ μλλ°μ?", inline=True)
            await ctx.channel.send(embed=embed)
