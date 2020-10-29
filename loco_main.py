try:
    import requests,json,asyncio,pytz,time,discord
    from dhooks import Webhook, Embed
    from datetime import datetime
    from pytz import timezone
    from discord.ext.commands import Bot
    from discord.ext import commands
    import sys
    import subprocess
except Exception as e:
    print("Import Error:",str(e))

# input all datas
self_token = "NjEyNjE3ODkxMzM0MDYyMTQw.XnmSgA.p0BILxvBJc3eSMuofzKIs73EsBI"
bot_token = "NzAyMzkyOTU4MDE1NzY2NTU5.Xp_Yow.LS0m1CtkGDA9pzmrTF5zsVL3G08"

bot_prefix = "#"

answer_channel_id = "702354502136889354"

quipp_ch="691596828021620786"

jee_ch="607228908080857101"

Crowd_channels = ["694043708743483422","702354502136889354"]

#############################


    

client = discord.Client()


bot = Bot(command_prefix=bot_prefix)
bot.remove_command('help')


async def _restart_bot():
    try:
      await aiosession.close()
      #await bot.cogs["Music"].disconnect_all_voice_clients()
    except:
       pass
    await bot.logout()
    subprocess.call([sys.executable, "loco_main.py"])


def is_owner(ctx):
    return ctx.message.author.id == "488569887342723073","488569887342723073"   

    
@bot.event 
async def on_ready():
    print("Logged in as " + bot.user.name)
    l = bot.get_channel(answer_channel_id)
    q = bot.get_channel(quipp_ch)
    j = bot.get_channel(jee_ch)
    embed = Embed(title=f"**__TRIVIA CHALLENGE || PRO™__**", description=" ***Hq auto Runner bot Is Back...✅***",color=0xFFFFFF)
    embed.set_image(url="https://cdn.discordapp.com/attachments/649457795875209265/672845602824126494/Nitro_2.gif")
    embed.set_footer(text="© With ❤ By Challenge team",icon_url="https://cdn.discordapp.com/attachments/682521230569373714/700955273212329997/IMG-20200416-WA0004.jpg?size=1024")
    await bot.send_message(discord.Object(id="702354502136889354"), embed=embed)

    
    

@bot.command(hidden=True)
async def restart():
    """Restarts the bot"""
   # log.warning("{} has restarted the bot!".format(ctx.author))
    await _restart_bot()
    print("done")

    
@client.event
async def on_ready():
    print("Logged in as " + client.user.name)
    #client.loop.create_task(live_handling())

@client.event
async def on_message(message):
    channel = bot.get_channel(answer_channel_id)
    q = bot.get_channel(quipp_ch)
    j = bot.get_channel(jee_ch)

    
    if message.channel.id in Crowd_channels:
        content = message.content
        if "Hq" in content:
            if "Hq" in content or "Hq" in content:
                await bot.send_message(channel,"+hq")
       
        
        
                
loop = asyncio.get_event_loop()



loop = asyncio.get_event_loop()

loop.create_task(bot.start(bot_token))
loop.create_task(client.start(self_token,bot=False))

while True:
    try:
        try:
            loop.run_forever()
        finally:
            loop.stop()
    except Exception as e:
       print("Event loop error:", e)
       
