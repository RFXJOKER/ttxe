import requests
import json
import time
from datetime import datetime
from lomond import WebSocket
from unidecode import unidecode
import colorama
import re
from dhooks import Webhook, Embed
import websocket
import random
#import base64
from websocket import create_connection	
#from bs4 import BeautifulSoup

ques = ""
cookies = {}
webhook_url = "https://discordapp.com/api/webhooks/745622647475404971/JQ3YzGGCYjnIsRA7AS1o-m0H6zG2ngu2ADITF8ymiUA_mDRS9nyJYmYlg30ggeEEwdy5"
options = ["","",""]
ouids = ["","",""]
cnt = ["","",""]
global uid1
uid1 = None
global uid2
uid2 = None
global uid3
uid3 = None
global opt1
opt1 = None
global opt2
opt2 = None
global opt3
opt3 = None
global question
question = None
global qnum
qnum = None
bt = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IkF5dXNoIE1vaGFwYXRyYSIsInVzZXJfdWlkIjoiNDEwMjQzOTAwNzU0ODA0NyIsImF2YXRhciI6IiIsImV4cCI6MTU5ODM2MzY1OSwiaWF0IjoxNTk4MzYxODU5LCJfX2FwcCI6InZlZGFudHUifQ.nO3QWYxKDQHP4xfVjVHoERxXEATjrkHwpHyPNppwb4Y"

try:
	hook = Webhook(webhook_url)
except:
	print("Invalid WebHook Url!")
"""	
try:
	loco = Webhook(lrun_url)
except:
	print("Invalid webhook Url!")

try:
	veda = Webhook(mandu)
except:
	print("Invalid Webhook Url!")
	
try:
	web = Webhook(dragon)
except:
	print("Invalid Webhook Url!")
	
try:
	rishi = Webhook(sunc)
except:
	print("Invalid Webhook Url!")
	
try:
	ank = Webhook(ankush)
except:
	print("Invalid Webhook Url!")
	
try:
	ad = Webhook(aditya)
except:
	print("Invalid Webhook Url!")								
try:
	nt = Webhook(nitin)
except:
	print("Invalid Webhook Url!")	
"""															
loco_bearer_token = "cJamdQK1wK4jslXuLSBmi3pfYlchA1"
response_data = requests.get("http://api.getloconow.com/v1/contests/",headers={'Authorization': f"Bearer {loco_bearer_token}"}).json()
print(response_data)
game=response_data['name']
priz=response_data['prize']
me=response_data['card_image_url']
cate=response_data['contest_category_name']
time=response_data['start_after']
milli=int(time)
seconds=(milli/1000)%60
seconds=int(seconds)
minutes=(milli/(1000*60))%60
minutes=int(minutes)
hours=(milli/(1000*60*60))%24
hours=int(hours)
"""
embed = Embed(title=f"Next Game Starts In {hours} Hours {minutes} Minutes!",color=0xFF6310)
embed.add_field(name="Game Starts In!", value="**{}hr {}min {}sec**".format(hours,minutes,seconds),inline=False)
embed.add_field(name="Game Name", value="**[{}](https://images.app.goo.gl/NQsDENJqKHVKesh68)**".format(game),inline=False)
embed.add_field(name="Prize Money", value="**{}**".format(priz),inline=False)
#embed.add_field(name="Game Type", value="**{}**".format(liv),inline=False)
embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/709231606430171196/734442488433082449/714808994136457257-1.png")
embed.set_footer(text="Vedantu Google | Atanu AD!#6554",icon_url="https://cdn.discordapp.com/attachments/709231606430171196/734442488433082449/714808994136457257-1.png")
web.send(embed=embed)
"""

SID_url = 'https://vedantu-realtime.getloconow.com/v2/?EIO=3&transport=polling'

headers = {

			'authority':	'vedantu-realtime.getloconow.com',
			'scheme':	'https',
			'accept':	'*/*',
			'authorization':	bt,
			'device-id':	'A2065A697438C1CCD93BF78FBD31067006CDD984',
			'x-app-language':	'1',
			'x-app-version':	'100015',
			'x-platform':	'5',
			'accept-encoding':	'gzip',
			'user-agent':	'okhttp/3.14.4',}
r = requests.get(SID_url, headers=headers)
rdata = r.text
print(rdata)

try:
	cookies = r.cookies
	print(cookies)	
except:
	print("Cookies Error!")
try:
	rdata = rdata[rdata.find('{'):]
	rjson = json.loads(rdata)
	print(rjson["sid"])
        #return rjson["sid"]
	SID = rjson["sid"]
except:
	print("There is some error in getting sid")
	#return -1

cookie = 'AWSALB='+cookies['AWSALB']
print(cookie)
#url = f'https://realtime.getloconow.com/v2/?EIO=3&sid={SID}&transport=polling'
url = f'https://vedantu-realtime.getloconow.com/v2/?EIO=3&sid ={SID}&transport=polling'

headers = {

			'authority':	'vedantu-realtime.getloconow.com',
			'scheme':	'https',
			'accept':	'*/*',
			'authorization':	bt,
			'cookie':	cookie,#f'AWSALB={Cokie}',
			'device-id':	'A2065A697438C1CCD93BF78FBD31067006CDD984',
			'x-app-language':	'1',
			'x-app-version':	'100015',
			'x-platform':	'5',
			'accept-encoding':	'gzip',
			'user-agent':	'okhttp/3.14.4',
	}

r = requests.get(url, headers=headers)
z = r.cookies

#cookies = z['AWSALB']
cookie = 'AWSALB='+cookies['AWSALB']
url = f'https://vedantu-realtime.getloconow.com/v2/?EIO=3&sid={SID}&transport=polling'
#this is a small barear = Bearer pfcbcZo8FrJDi17USGjXirf9UPUJa9
headers = {

			'authority':	'vedantu-realtime.getloconow.com',
			'scheme':	'https',
			'accept':	'*/*',
			'authorization':	bt,
			'cookie':	cookie,
			'device-id':	'A2065A697438C1CCD93BF78FBD31067006CDD984',
			'x-app-language':	'1',
			'x-app-version':	'100015',
			'x-platform':	'5',
			'accept-encoding':	'gzip',
			'user-agent':	'okhttp/3.14.4',
		}

r = requests.get(url, headers=headers)
print(r)
header = {
		   'Authorization':	bt,
			'Cookie':	cookie,
                        'Device-Id':	'A2065A697438C1CCD93BF78FBD31067006CDD984',
			'X-APP-LANGUAGE':	'1',
			'X-APP-VERSION':	'100015',
			'X-PLATFORM':	'5',
			'Upgrade':	'websocket',
			'Connection':	'Upgrade',
			#'Sec-WebSocket-Key':	'05ipoH3X8mATm4d9IsdaRg==',
			'Sec-WebSocket-Version':	'13',
			'Host':	'vedantu-realtime.getloconow.com',
			'Accept-Encoding':	'gzip',
			'User-Agent':	'okhttp/3.14.4'}
try:
	import thread
except ImportError:
	import _thread as thread
import time
def on_message(ws, message):
	#print(message)
	if message == '3probe':
		print("Successfully!! Connected")
		#hook.send('')
	elif message != '3':
		try:
			message = message[message.find('['):]
			mdata = json.loads(message)
			if "question" in mdata:
				global uid1
				global uid2
				global uid3
				global opt1
				global opt2
				global opt3
				global question
				global qnum
				ques = mdata[1]["text"]
				question_no = mdata[1]["question_rank"]
				coin= mdata[1]["reward_coins"]
				options = []
				for o in mdata[1]["options"]:
                                        options.append(o["text"])
				ouids = []
				for p in mdata[1]["options"]:
					ouids.append(p["uid"])
				real_question = str(ques).replace(" ","+")
				google_query = "https://google.com/search?q="+real_question
				qnum = f"{question_no}"
				question = f"{ques}"
				opt1 = f"{options[2]}"
				opt2 = f"{options[1]}"
				opt3 = f"{options[0]}"
				uid1 = f"{ouids[2]}"
				uid2 = f"{ouids[1]}"
				uid3 = f"{ouids[0]}"
				op1 = str(opt1).replace(" ","+")
				op2 = str(opt2).replace(" ","+")
				op3 = str(opt3).replace(" ","+")
				sr1 = "https://www.google.com/search?q="+real_question+"+"+op1
				sr2 = "https://www.google.com/search?q="+real_question+"+"+op2
				sr3 = "https://www.google.com/search?q="+real_question+"+"+op3
				#sl = "https://www.google.com/search?q="+real_question+"+"+op1+"+"+op2+"+"+op3
				#bar = "Search with all options"
				embed = Embed(title=f"**Question {str(question_no)} Out Of 10**", description=f"**[{ques}]({google_query})**\n**Reward Coins:- {coin}**",color=0xFF6310)
				#embed.add_field(name="**Answer Choice ❶**", value=f"**[{options[2]}]({sr1})**")
				#embed.add_field(name="**Answer Choice ❷**", value=f"**[{options[1]}]({sr2})**")
				#embed.add_field(name="**Answer Choice ❸**", value=f"**[{options[0]}]({sr3})**")
				embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/716372313141936280/738353169934843985/714808994136457257-1.png")
				embed.set_footer(text="Vedantu Google | Captain",icon_url=" ")
				hook.send(embed=embed)
				hook.send("lo")
				"""
				loco.send(embed=embed)
				veda.send(embed=embed)
				web.send(embed=embed)
				hook.send("l")
				loco.send("v")
				veda.send("v")
				web.send(embed=embed)
				rishi.send(embed=embed)
				ank.send(embed=embed)
				ad.send(embed=embed)
				nt.send(embed=embed)
				loco.send("v")
				hook.send("l")
				web.send("lo")
				"""
				r = requests.get("http://www.google.com/search?q=" + question +"+"+ opt1 +"+"+ opt2 +"+"+ opt3)
				res = str(r.text)
				countoption1 = res.count(opt1)
				countoption2 = res.count(opt2)
				countoption3 = res.count(opt3)
				maxcount = max(countoption1, countoption2, countoption3)
				sumcount = countoption1+countoption2+countoption3       
				if countoption1 == maxcount:
					embed = Embed(title="Google Results!", description=f"**A.** {options[2]}: **{countoption1}**✅\n**B.** {options[1]}: **{countoption2}**\n**C.** {options[0]}: **{countoption3}**",color=0xFF6310)
					hook.send(embed=embed)
					"""
					loco.send(embed=embed)
					veda.send(embed=embed)
					web.send(embed=embed)
					
					web.send(embed=embed)
					rishi.send(embed=embed)
					ank.send(embed=embed)
					ad.send(embed=embed)
					nt.send(embed=embed)
					"""
				elif countoption2 == maxcount:
					embed = Embed(title="Google Results!", description=f"**A.** {options[2]}: **{countoption1}**\n**B.** {options[1]}: **{countoption2}**✅\n**C.** {options[0]}: **{countoption3}**",color=0xFF6310)
					hook.send(embed=embed)
					"""
					loco.send(embed=embed)
					veda.send(embed=embed)
					web.send(embed=embed)
					
					web.send(embed=embed)
					rishi.send(embed=embed)
					ank.send(embed=embed)
					ad.send(embed=embed)
					nt.send(embed=embed)
					"""
				else:
					embed = Embed(title="Google Results!", description=f"**A.** {options[2]}: **{countoption1}**\n**B.** {options[1]}: **{countoption2}**\n**C.** {options[0]}: **{countoption3}**✅",color=0xFF6310)
					hook.send(embed=embed)
					"""
					loco.send(embed=embed)
					veda.send(embed=embed)
					web.send(embed=embed)
					
					web.send(embed=embed)
					rishi.send(embed=embed)
					ank.send(embed=embed)
					ad.send(embed=embed)
					nt.send(embed=embed)
					"""
			elif "status" in mdata:
				cuid = mdata[1]['question_stats']["correct_option_uid"]
				cnt = []
				for c in mdata[1]['question_stats']["answer_dist"]:
					cnt.append(c["count"])
				cnt1 = f"{cnt[2]}"
				cnt2 = f"{cnt[1]}"
				cnt3 = f"{cnt[0]}"
				c1 = int(cnt1)
				c2 = int(cnt2)
				c3 = int(cnt3)
				a23 = c2+c3
				a13 = c1+c3
				a12 = c1+c2
				if uid1 == cuid:
					embdd=Embed(title=f"**{str(qnum)})** **{question}**",description=f"Correct Answer: **A.{opt1}**",color=0x07E200)  
					embdd.add_field(name="Stats", value=f"**• Advancing Players:** **{c1}**\n**• Eliminated Players:** **{a23}**")
					hook.send(embed=embdd)
					"""
					loco.send(embed=embdd)
					veda.send(embed=embdd)
					web.send(embed=embdd)
					
					web.send(embed=embdd)
					rishi.send(embed=embdd)
					ank.send(embed=embdd)
					ad.send(embed=embdd)
					nt.send(embed=embdd)
					"""
				elif uid2 == cuid:
					embdd=Embed(title=f"**{str(qnum)})** **{question}**",description=f"Correct Answer: **B.{opt2}**",color=0x07E200) 
					embdd.add_field(name="Stats", value=f"**• Advancing Players:** **{c2}**\n**• Eliminated Players:** **{a13}**")
					hook.send(embed=embdd)
					"""
					loco.send(embed=embdd)
					veda.send(embed=embdd)
					web.send(embed=embdd)
					"""
				else:
					embdd=Embed(title=f"**{str(qnum)})** **{question}**",description=f"Correct Answer: **C.{opt3}**",color=0x07E200) 
					embdd.add_field(name="Stats", value=f"**• Advancing Players:** **{c3}**\n**• Eliminated Players:** **{a12}**")
					hook.send(embed=embdd)
					"""
					loco.send(embed=embdd)
					veda.send(embed=embdd)
					web.send(embed=embdd)
					
					web.send(embed=embdd)
					rishi.send(embed=embdd)
					ank.send(embed=embdd)
					ad.send(embed=embdd)
					nt.send(embed=embdd)
					"""
			elif "winners_v2" in mdata:
				tw = mdata[1]["total_winners"]
				print(tw)
				wamt = []
				for w in mdata[1]["winners"]:
					wamt.append(w["won"])
				print(wamt)
				wo = f"{wamt[0]}"
				print(wo)
				embdd=Embed(title="Game Summary!", description="",color=0xFF6310)
				embdd.add_field(name="Game Stats", value=f"**• Payout:** **₹{wo}**\n**• Prize Money:** **₹{priz}**\n**• Total Winners:** **{tw}**")
				embdd.set_thumbnail(url="https://cdn.discordapp.com/attachments/737764195743039488/738540310057058395/e70bcc65284623.5aef51b58b0c9.gif")
				embdd.set_footer(text="Vedantu Google | Captain",icon_url="https://cdn.discordapp.com/attachments/709231606430171196/734442488433082449/714808994136457257-1.png")
				hook.send(embed=embdd)
				"""
				loco.send(embed=embdd)
				veda.send(embed=embdd)
				web.send(embed=embdd)
				
				web.send(embed=embdd)
				rishi.send(embed=embdd)
				ank.send(embed=embdd)
				ad.send(embed=embdd)
				nt.send(embed=embdd)
				"""
		except:
			print(message)

def on_error(ws, error):
	print(error)
	#hook.send('')

def on_close(ws):
	print("closed")
	#hook.send('')

def on_open(ws):
		#print('## Opened ##')
		def run(*args):
				ws.send('2probe')
				ws.send('5')
				while True:
						try:
								#print('Sending to Server...')
								time.sleep(15)
								ws.send('2')
						
						except:
								print('Unable to send to server')
								break
				time.sleep(1)
				ws.close()
				print ("thread terminating..")
		thread.start_new_thread(run, ())



if __name__ == "__main__":
	websocket.enableTrace(True)
	#ws = websocket.WebSocketApp(f"wss://realtime.getloconow.com/v2/?EIO=3&sid={SID}&transport=websocket",
	ws = websocket.WebSocketApp(f"wss://vedantu-realtime.getloconow.com/v2/?EIO=3&sid={SID}&transport=websocket",
								on_message = on_message,
								on_error = on_error,
								on_close = on_close,
								cookie =cookie,
								header = header)
	ws.on_open = on_open
	ws.run_forever()
			   
