import discord, json, random
from discord.ext import commands, tasks
from collections import OrderedDict

class games(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name= '낚시')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def fishing(self, ctx):
        user_id = ctx.author.id
        with open('user.json', 'r', encoding='utf-8') as f:
            user_data = json.load(f)

        if f'{user_id}' in user_data:
            fish = ['연어', '고등어', '참치', '대구', '흰동가리', '금붕어']
            random_fishing = random.choices(fish, weights=[30, 30, 25, 30, 1, 25])[0]
            embed = discord.Embed(color= 0x00ff9c)
            embed.add_field(name="호우우", value=f'{random_fishing}', inline=True)
            await ctx.channel.send(embed=embed)

            if random_fishing == "연어":
                user_data[f"{user_id}"]["fish"]["salmon"] += 1
            elif random_fishing == "고등어":
                user_data[f"{user_id}"]["fish"]["Mackerel"] += 1
            elif random_fishing == "참치":
                user_data[f"{user_id}"]["fish"]["tuna"] += 1
            elif random_fishing == "대구":
                user_data[f"{user_id}"]["fish"]["cod"] += 1
            elif random_fishing == "희동가리":
                user_data[f"{user_id}"]["fish"]["Clownfish"] += 1
            elif random_fishing == "금붕어":
                user_data[f"{user_id}"]["fish"]["goldfish"] += 1

            with open('user.json', 'w', encoding='utf-8') as f2:
                json.dump(user_data , f2, indent="\t")

        else:
            embed = discord.Embed(color= 0xec4747)
            embed.add_field(name="이런", value="가입이 안돼있네요 희망봇 가입을 쳐보세요!", inline=True)
            await ctx.channel.send(embed=embed)

    @commands.command(name= '인벤토리')
    async def Inventory(self, ctx):

        with open('user.json', 'r', encoding='utf-8') as f:
            user_data = json.load(f)

        user_id = ctx.author.id

        if f'{user_id}' in user_data:

            with open('item\item.json', 'r', encoding='utf-8') as f:
                item_data = json.load(f)

            user_weapon = user_data[f"{user_id}"]["item"]["weapon"]
            user_armor = user_data[f"{user_id}"]["item"]["armor"]
            user_totem = user_data[f"{user_id}"]["item"]["totem"]
            user_Inventory0 = user_data[f"{user_id}"]["Inventory"]["0"]
            user_Inventory1 = user_data[f"{user_id}"]["Inventory"]["1"]
            user_Inventory2 = user_data[f"{user_id}"]["Inventory"]["2"]
            user_Inventory3 = user_data[f"{user_id}"]["Inventory"]["3"]
            user_Inventory4 = user_data[f"{user_id}"]["Inventory"]["4"]
            user_Inventory5 = user_data[f"{user_id}"]["Inventory"]["5"]
            user_Inventory6 = user_data[f"{user_id}"]["Inventory"]["6"]
            user_Inventory7 = user_data[f"{user_id}"]["Inventory"]["7"]
            user_Inventory8 = user_data[f"{user_id}"]["Inventory"]["8"]
            user_Inventory9 = user_data[f"{user_id}"]["Inventory"]["9"]

            embed = discord.Embed(color= 0x00ff9c)
            embed.set_author(name="희망봇", icon_url="https://cdn.discordapp.com/attachments/773727937069056000/857254590218371082/526_B39FCE5.png",)
            embed.set_thumbnail(url=ctx.author.avatar_url)

            embed.add_field(name="레벨", value=f'``{user_data[f"{user_id}"]["levels"]}``', inline=True)
            embed.add_field(name="경험치", value=f'``{user_data[f"{user_id}"]["exp"]}``', inline=True)
            embed.add_field(name="힘", value=f'``{user_data[f"{user_id}"]["power"]}``', inline=True)
            embed.add_field(name="방어", value=f'``{user_data[f"{user_id}"]["def"]}``', inline=True)
            embed.add_field(name="HP", value=f'``{user_data[f"{user_id}"]["hp"]}``', inline=True)

            embed.add_field(name="돈:moneybag:", value=f'``{user_data[f"{user_id}"]["money"]}``', inline=True)

            embed.add_field(name="무기", value=f'``{item_data[f"{user_weapon}"]["name"]}``', inline=True)
            embed.add_field(name="아머", value=f'``{item_data[f"{user_armor}"]["name"]}``', inline=True)
            embed.add_field(name="토템", value=f'``{item_data[f"{user_totem}"]["name"]}``', inline=True)

            embed.add_field(name="인벤토리:pouch:", value="-----------------------------------------------", inline=False)
            embed.add_field(name="0", value=f'``{item_data[f"{user_Inventory0}"]["name"]}``', inline=True)
            embed.add_field(name="1", value=f'``{item_data[f"{user_Inventory1}"]["name"]}``', inline=True)
            embed.add_field(name="2", value=f'``{item_data[f"{user_Inventory2}"]["name"]}``', inline=True)
            embed.add_field(name="3", value=f'``{item_data[f"{user_Inventory3}"]["name"]}``', inline=True)
            embed.add_field(name="4", value=f'``{item_data[f"{user_Inventory4}"]["name"]}``', inline=True)
            embed.add_field(name="5", value=f'``{item_data[f"{user_Inventory5}"]["name"]}``', inline=True)
            embed.add_field(name="6", value=f'``{item_data[f"{user_Inventory6}"]["name"]}``', inline=True)
            embed.add_field(name="7", value=f'``{item_data[f"{user_Inventory7}"]["name"]}``', inline=True)
            embed.add_field(name="8", value=f'``{item_data[f"{user_Inventory8}"]["name"]}``', inline=True)
            embed.add_field(name="9", value=f'``{item_data[f"{user_Inventory9}"]["name"]}``', inline=True)

            embed.add_field(name="낚시:fish:", value="-----------------------------------------------", inline=False)
            embed.add_field(name="연어", value=f'``{user_data[f"{user_id}"]["fish"]["salmon"]}``', inline=True)
            embed.add_field(name="고등어", value=f'``{user_data[f"{user_id}"]["fish"]["Mackerel"]}``', inline=True)
            embed.add_field(name="참치", value=f'``{user_data[f"{user_id}"]["fish"]["tuna"]}``', inline=True)
            embed.add_field(name="대구", value=f'``{user_data[f"{user_id}"]["fish"]["cod"]}``', inline=True)
            embed.add_field(name="희동가리", value=f'``{user_data[f"{user_id}"]["fish"]["Clownfish"]}``', inline=True)
            embed.add_field(name="금붕어", value=f'``{user_data[f"{user_id}"]["fish"]["goldfish"]}``', inline=True)
            await ctx.channel.send(embed=embed)
        else:
            embed = discord.Embed(color= 0xec4747)
            embed.add_field(name="이런", value="가입이 안돼있네요 희망봇 가입을 쳐보세요!", inline=True)
            await ctx.channel.send(embed=embed)