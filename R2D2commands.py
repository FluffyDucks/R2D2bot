'''
R2D2 - A discord bot
Copyright (C) 2020  David Yeung
'''

#----- Import Libraries -----#
import discord
from discord.ext import commands
import asyncio
import random

#----- CONSTANTS -----#

#-- Grab constants from text file --#
file = open("constants.txt", "r")
CONSTANTS = file.read().split()
file.close()

TOKEN = CONSTANTS[0]
BOT_PREFIX = CONSTANTS[1]

bot = commands.Bot(command_prefix='%')

@bot.event
async def on_ready():
    name_choices = ["humans", "homo sapiens", "the boys", "the girls"]
    game = discord.Game("with {}".format(random.choice(name_choices)))
    await bot.change_presence(activity=game)
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

#========== Commands ==========#
@bot.command(name = "ping",
                brief = "Pong!",
                description = "Ping R2-D2")
async def ping(ctx):
    latency = bot.latency
    print("[DEBUG] Pinged!")
    embed=discord.Embed(title=":ping_pong: Pong! :ping_pong:", description='That took {}ms'.format(round(latency, 3)), color=0x2874A6)
    await ctx.send(embed=embed)



#----- Fun Commands -----#
@bot.command(name='8ball',
                brief="Answers from the void.",
                description="Answers a yes/no question.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(ctx):
    print("[DEBUG] 8ball summoned")
    possible_responses = ['That is a resounding no',
                          'It is not looking likely',
                          'Too hard to tell',
                          'It is quite possible',
                          'Definitely']
    await ctx.send("Beep boop " + random.choice(possible_responses) + ", " + ctx.message.author.mention)

@bot.command(name = "slap",
                brief = "get your stuff together!",
                description = "slap another user",
                pass_context = True)
async def slap(ctx, user:discord.Member = None):
    print("[DEBUG] slap detected")
    if not user:
        await ctx.send("Why you slapping air boi?")
    elif(ctx.message.author == user):
        text = "{} slapped themselves!\nTime to get your stuff together".format(ctx.message.author.mention)
        embed = discord.Embed(description=text, color=0x00ff00)
        embed.set_image(url='https://media.giphy.com/media/3XlEk2RxPS1m8/giphy.gif')
        await ctx.send(embed=embed)
    else:
        slap_possible_gifs = ['https://media.giphy.com/media/3XlEk2RxPS1m8/giphy.gif',
                              'https://media.giphy.com/media/IYcXTDme1ZPMI/giphy.gif',
                              'https://media.giphy.com/media/Hj9ixvpSfqcQo/giphy.gif',
                              'https://media.giphy.com/media/Gf3AUz3eBNbTW/giphy.gif',
                              'https://media.giphy.com/media/wcgMZsFyRVYDm/giphy.gif'
                              'https://media.giphy.com/media/XpgfPCejnWuAg/giphy.gif']

        text = "{} slapped {}!\nMust have been a real idiot!".format(ctx.message.author.mention, user.mention)
        embed = discord.Embed(description=text, color=0x00ff00)
        embed.set_image(url=random.choice(slap_possible_gifs))
        await ctx.send(embed=embed)

@bot.command(name = "slapass",
                brief = "Give'em a good 'ol whack to the glutes",
                description = "Gives a slap ass to another user (comedy sketch from Key & Peele)",
                pass_context = True)
async def slap_ass(ctx, user:discord.Member = None):
    print("[DEBUG] slapass detected")
    if not user:
        await ctx.send("Why you slapping air boi?")
    elif(ctx.message.author == user):
        text = "{} slapped their own ass!\nI don't know why they would, but I don't judge!".format(ctx.message.author.mention)
        embed = discord.Embed(description=text, color=0x00ff00)
        embed.set_image(url='https://media.giphy.com/media/tm4RM7lj2qM2k/giphy.gif')
        await ctx.send(embed=embed)
    else:
        text = "{} slapped {}'s ass!\nMust have been a great game!".format(ctx.message.author.mention, user.mention)
        embed = discord.Embed(description=text, color=0x00ff00)
        embed.set_image(url='https://media.giphy.com/media/tm4RM7lj2qM2k/giphy.gif')
        await ctx.send(embed=embed)

@bot.command(name = "hug",
                brief = "Someone needs a hug",
                description = "Give a hug to another user",
                pass_context = True)
async def hugs(ctx, user:discord.Member = None):
    print("[DEBUG] hug detected")
    if not user:
        await ctx.send("Why you hugging air boi?")
    elif(ctx.message.author == user):
        text = "{} hugged themselves!\n That's pretty sad, someone give {} a hug".format(ctx.message.author.mention, ctx.message.author.mention)
        embed = discord.Embed(description=text, color=0x00ff00)
        embed.set_image(url='https://media.giphy.com/media/23UUncwBQRkIg/giphy.gif')
        await ctx.send(embed=embed)
    else:
        text = "{} hugged {}!\nHow nice!".format(ctx.message.author.mention, user.mention)
        embed = discord.Embed(description=text, color=0x00ff00)
        embed.set_image(url='https://media.giphy.com/media/23UUncwBQRkIg/giphy.gif')
        await ctx.send(embed=embed)

@bot.command()
async def spit(ctx, user:discord.Member = None):
    print("[DEBUG] spit detected")

    spit_possible_gifs = ['https://media.giphy.com/media/l0HU5bbgdW6qzJsmQ/giphy.gif',
                          'https://media.giphy.com/media/MD27a3bvc6Rhu/giphy.gif',
                          'https://media.giphy.com/media/ZablVFuGJhb7qMmbqj/giphy.gif']

    if not user:
        await ctx.send("Oi! Don't spit on the ground, wtf man clean it up...")
    elif(ctx.message.author == user):
        text = "<:ratirlspit:561972370513068033> {} spat on themselves.\n\tAs to why, well that's anyone's guess...".format(ctx.message.author.mention)
        embed = discord.Embed(description=text, color=0x00ff00)
        embed.set_image(url="https://media.giphy.com/media/U0L0whTE3lzMc/giphy.gif")
        await ctx.send(embed=embed)
    else:
        text = "<:ratirlspit:561972370513068033> {} spat on {}!\n\tGross...".format(ctx.message.author.mention, user.mention)
        embed = discord.Embed(description=text, color=0x00ff00)
        embed.set_image(url=random.choice(spit_possible_gifs))
        await ctx.send(embed=embed)



# @bot.command(name = "kill",
#                 brief = "Have fun in the after life"
#                 description = "kill a user, user can be saved by reacting")

#----- Games -----#
@bot.command(name = "lotto",
                brief = "Gamble your senses away!",
                description = "enter the lotto by reacting to the lotto message.",
                pass_context = True)
async def lotto(ctx):
    print("[DEBUG] Lotto detected")
    msg = await ctx.send("React to this message")
    update_msg = await ctx.send("reactions on message: {}".format(msg.reaction))
    for i in range(10):
        await update_msg.edit(content="reactions on message: {}".format(msg.reaction))


@bot.command(name = "RPS",
                brief = "RPS with R2-D2 [warning: R2-D2 may or may not have rigged it]",
                description = "Play RPS with R2-D2",
                aliases = ["rps"],
                pass_context = True)
async def RPS(ctx):
    print("[DEBUG] RPS detected")
    temp = ctx.message.content
    temp2 = temp.split()
    userChoice = temp2[1]
    print("[DEBUG] User chooses " + userChoice)

    possible_choices = ["rock","paper","scissors"]

    botChoice = random.choice(possible_choices)
    print("[DEBUG] Bot chooses " + botChoice)

    if((userChoice in possible_choices) == False):
        await ctx.send(userChoice + " is not an option. The possible choices are rock, paper, or scissors.")
        await ctx.send("It can't be that hard to type one of the three options, right?")
    else:
        msg = await ctx.send("I choose")
        await asyncio.sleep(1)
        await msg.edit(content="I choose.")
        await asyncio.sleep(1)
        await msg.edit(content="I choose..")
        await asyncio.sleep(1)
        await msg.edit(content="I choose...")
        await asyncio.sleep(1)
        await msg.edit(content="I choose " + botChoice)
        if(userChoice == botChoice):
            await ctx.send("No one wins <:PepeThink:514677177917374465>")

        elif(userChoice == "rock" and botChoice == "scissors"):
            await ctx.send(ctx.message.author.mention + " wins... <:FeelsBadMan:514227559383171072:>")
        elif(userChoice == "rock" and botChoice == "paper"):
            await ctx.send("I win! <:POGGIES:688957460442251336>")

        elif(userChoice == "paper" and botChoice == "rock"):
            await ctx.send(ctx.message.author.mention + " wins... <:FeelsBadMan:514227559383171072:>")
        elif(userChoice == "paper" and botChoice == "scissors"):
            await ctx.send("I win! <:POGGIES:688957460442251336>")

        elif(userChoice == "scissors" and botChoice == "paper"):
            await ctx.send(ctx.message.author.mention + " wins... <:FeelsBadMan:514227559383171072:>")
        elif(userChoice == "scissors" and botChoice == "rock"):
            await ctx.send("I win! <:POGGIES:688957460442251336>")

bot.run(TOKEN)