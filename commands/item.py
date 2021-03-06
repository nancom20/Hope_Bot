import discord, json

from discord.ext import commands, tasks

async def save_item(itemid:int, amount:int, ctx):
    user_id = ctx.author.id

    with open('user.json', 'r', encoding='utf-8') as f: user_data = json.load(f)
    with open('item\item.json', 'r', encoding='utf-8') as f: item_data = json.load(f)

    await ctx.channel.send(f"{itemid}   {amount}")

    for i in range(10):
        if user_data[f'{user_id}']['Inventory'][f'{i}']['id'] == int(itemid):
            save_line = i
            user_data[f'{user_id}']['Inventory'][f'{save_line}']['amount'] += int(amount)
            with open('user.json', 'w', encoding='utf-8') as f2:
                json.dump(user_data , f2, indent="\t")

            await ctx.channel.send(f"{i}라인 저장")
            return

    for i in range(10):
        if user_data[f'{user_id}']['Inventory'][f'{i}']['id'] == 0:
            user_data[f'{user_id}']['Inventory'][f'{i}']['id'] = int(itemid)
            user_data[f'{user_id}']['Inventory'][f'{i}']['amount'] = int(amount)

            with open('user.json', 'w', encoding='utf-8') as f2:
                json.dump(user_data , f2, indent="\t")

            await ctx.channel.send(f"{i}라인 저장")

            break

async def delete_item(line, amount, ctx):

    user_id = ctx.author.id

    with open('user.json', 'r', encoding='utf-8') as f: user_data = json.load(f)
    with open('item\item.json', 'r', encoding='utf-8') as f1: item_data = json.load(f1)

    if user_data[f'{user_id}']['Inventory'][f'{line}']['id'] == 0:
        await ctx.channel.send(f"{line}라인 에 삭제할 아이템 없")
        return

    user_data[f'{user_id}']['Inventory'][f"{line}"]["amount"] -= int(amount)

    if user_data[f"{user_id}"]["Inventory"][f"{line}"]["amount"] == 0:
        user_data[f"{user_id}"]["Inventory"][f"{line}"]["id"] = 0

    with open('user.json', 'w', encoding='utf-8') as f2: json.dump(user_data , f2, indent="\t")

    await ctx.channel.send(f"{line}라인 삭")