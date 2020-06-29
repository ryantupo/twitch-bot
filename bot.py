#bot.py
import config
import os # for importing env vars for the bot to use
from twitchio.ext import commands
import sys
import random
import datetime
import sched, time
from threading import Timer
from pagan import*
import os
from playsound import playsound
import sys
import redis
import config
import asyncio



#//////////////////////////////////////--server stuff--///////////////////////////////////////

r = redis.Redis (host='client.draculcorp.com', port=6379, password=config.redis_pass)

#///////////////////////////////////////--imports--////////////////////////////////////////////

j = open("code.txt", "r")
code = j.read()
j = open("client.txt", "r")
client = j.read()
TOKEN = code
CLIENT_ID = client
NICK="RoboSauresBOT"
PREFIX ="!"
CHANNEL=('nthd3gr33')


#//////////////////////////////////////////////////////////////////////////////////////////////

thic_counter = 0
thinnie_counter = 0
savings_count = 0

list_of_sounds=[]


start = False

bets = None

name_pot = []

count = 0

#todays goal
cur_tod =(f"Todays Project: add additional functions to the Twictch Chat Bot :D")

#this months project
cur_pro = (f"Ryan's current project is to increase his ability to code PYTHON <3")

#counts the amount of messages in chat
chat_counter = 0

#keeps track of deaths 
death_counter = 0

#current time (last time bot ran)
x = str(datetime.datetime.now())

#win clause for tic tac toe
win = False

#boar for tictactoe - to be manipulated
boardT  = ['_','_','_',
            '_','_','_',
            '_','_','_']

#basic board for tictacote for resetting
boardTOG  = ['_','_','_',
            '_','_','_',
            '_','_','_']

#list of sound effects viewers can use
song_list = []

#time for timer?
a = datetime.datetime.now()
b = a.minute

#for timer
addpoint = sched.scheduler(time.time, time.sleep)

#names of players for tictactoe used to reassign after 
first_player = "Player 1"
second_player = "Player 2"

#turn timer for tictactoe True == x player False == O player
turn = True
turn_count = 0

#counts the amount of messages being sent in chat
mes_counter = 0
mes2_counter = 0
mes3_counter = 0
fest_count = 0

#varibles used for timer
freq = 5
bet_freq = 25
used = {}

#pot for betting
pot = 0


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#dictonaries

#basic users for thicc points
users= {}

users_who_messaged = []
users_who_messaged2 = []
users_who_messaged3 = []

users_in_bet= {}

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

bot = commands.Bot(
	#set up the bot
	irc_token =TOKEN,
	client_id =CLIENT_ID,
	nick=NICK,
	prefix=PREFIX,
	initial_channels=[CHANNEL]


	)


@bot.event
async def event_ready():
	print(f"{NICK} is online!!!")
	ws = bot._ws #used to store messagees
	await ws.send_privmsg(CHANNEL, f"/me Welcome Everyone!!!")


@bot.event
async def event_message(ctx):
	#runs everytime a message is sent
	global chat_counter
	global death_counter 
	chat_counter += 1

	#chat print out suggesting to follow
	if chat_counter % 100 == 0:
		await ctx.channel.send(f"Welcome everyone to the Stream :D if you arn't already remember to follow!")


	#make sure it ignores itselfgg
	if ctx.author.name.lower() == NICK.lower():
		return

	#bot.py, in event message,below the bot-ignoring stuff
	#respond to everytime someone messages
	if ctx.content.lower() == 'hello':
		await ctx.channel.send(f"Hi, @{ctx.author.name}!")
	if ctx.content.lower() == 'hey':
		await ctx.channel.send(f"Hi, @{ctx.author.name}!")
	if ctx.content.lower() == 'hi':
		await ctx.channel.send(f"Hi, @{ctx.author.name}!")


	#if someone writes karaoke time! it prints a message 
	if 'karaoke time!' in ctx.content.lower():
		await ctx.channel.send(f"LETS! GO!!!!!, @{ctx.author.name}!")




	if type(ctx.content.lower()) == str:
		cquote=ctx.content.lower()
		if "!quote" not in cquote:
			with open('thequotes.txt', 'a') as f:
				f.write("%s\n" % cquote)
		else:
			pass
		
















#-----------------------server version -------------------------------#
	if type(ctx.content.lower()) == str:
		

		if r.exists(ctx.author.name):
			keys = r.keys("*") 
			for name in keys:
				pass
		else:
			r.hset(ctx.author.name.lower(),  "thicc", 1)# assigns the dictonary with name() mist important then sub dictonaries and finally values
			r.hset(ctx.author.name.lower(), "thinnie", 2)
			r.hset(ctx.author.name.lower(), "thinnies_saved", 5)


	

			
	#if you message your name is added to a list of user who have messaged in the last 50 messages
	if type(ctx.content.lower()) == str:
		if ctx.author.name in users_who_messaged:
			pass
		else:
			users_who_messaged.append(ctx.author.name)
			users_who_messaged2.append(ctx.author.name)
			users_who_messaged3.append(ctx.author.name)
			print(users_who_messaged)
	
	if type(ctx.content.lower()) == str:
		
		if ctx.author.name in users_who_messaged:
			pass
		else:
			await ctx.channel.send(f"Welcome to the stream!!! :D <3 {ctx.author.name}")


	
	#counts the amount of messages sent
	if type(ctx.content.lower()) == str:
		global mes_counter
		global mes2_counter
		global mes3_counter
		global fest_count
		mes_counter += 1
		mes2_counter += 1
		mes3_counter += 1
		fest_count += 1

#	if fest_count >= 100 and len(users_who_messaged) >= 3:
#		await ctx.channel.send(f" click this link to que music ----->  https://festify.us/party/-M8GjSBwJ1gHHoLU_EfU")
#		fest_count = 0
		

#-----------------------------server version ----------------------------
	#for every 50 messages and at least 3 different people talking fgive everyone whos messaged a thicc point
	if mes_counter >= 500 and len(users_who_messaged) >= 3:

		for name in keys:
			values = (int(float(r.hget(name, "thicc"))))
			values = values + 1
			r.hset(name, "thicc", values)

		await ctx.channel.send(f"These people have recieved a Thicc point:{users_who_messaged}")		

		mes_counter = 0
		users_who_messaged.clear()
		

#------------------------server version------------------------
	#for every 50 messages and at least 3 different people talking fgive everyone whos messaged thinne point interest
	if mes2_counter >= 75 and len(users_who_messaged2) >= 3:
		for name in keys:
			values = int(float(r.hget(name, "thinnie")))
			name_thicc = int(float(r.hget(name, "thicc")))
			values += (name_thicc/5)
			r.hset(name, "thinnie", values)
		mes2_counter = 0
		users_who_messaged2.clear()
		
#------------server version---------------------------

	#for every 50 messages and at least 3 different people talking fgive everyone whos messaged a thicc point
	if mes3_counter >= 501 and len(users_who_messaged3) >= 3:
		for name in keys:
			values = int(float(r.hget(name, "thinnies_saved")))
			if values == 0:
				pass
			else:
				values += (values*0.2)
				r.hset(name, "thinnies_saved", values)
		mes3_counter = 0
		users_who_messaged3.clear()
	await bot.handle_commands(ctx)





#basic function for use
async def timeout(ctx):
	global freq
	await ctx.channel.send('sorry buds but !play was used within the last %u seconds.' % (freq))

async def board_print_tw(ctx):
	await ctx.channel.send("|"+boardT[0]+"|"+boardT[1]+"|"+boardT[2]+"|"),
	await ctx.channel.send("|"+boardT[3]+"|"+boardT[4]+"|"+boardT[5]+"|"),
	await ctx.channel.send("|"+boardT[6]+"|"+boardT[7]+"|"+boardT[8]+"|")

async def tic_resetV():
	global win
	global win
	global turn
	global first_player
	global second_player
	global turn_count
	win = False
	global boardT
	boardT = boardTOG.copy()
	turn = True
	turn_count = 0
	first_player = "Player 1"
	second_player = "Player 2"

async def pick_winner(ctx):
	global name_pot
	global start
	if len(name_pot) == 0:
		return
	else:
		print("3")
		global users_in_bet
		global pot
		a = random.choice(list(name_pot))
		values = int(float(r.hget(a, "thicc")))
		values = values + pot
		await ctx.channel.send(f'@{a} has just won !!! {pot} thicc points!!')
		r.hset(a, "thicc", values)
		start = False
		


#bot commands
@bot.command(name="suggestion")
async def suggestion_txt(ctx, *suggest):
	global x
	suggest =' '.join(suggest)
	entry =(ctx.author.name + " : " + suggest + " submitted at: "+ x)
	with open('suggestions.txt', 'a') as f:
		f.write("%s\n" % entry)

@bot.command(name="discord")
async def discord_call(ctx):
	await ctx.channel.send(f"heres the discord link -----> https://discord.com/invite/3sR4Ru9")

@bot.command(name="reset_suggestions")
async def reset_suggests(ctx):
	global x
	if ctx.author.is_mod:
		new_ent = ("file reset at : " + x)
		with open('suggestions.txt', 'w') as f:
			f.write("%s\n" % new_ent)

@bot.command(name ="death")
async def death_count(ctx):
	global death_counter
	death_counter += 1
	await ctx.channel.send(f"DEATH COUNTHER =={death_counter}")
	if death_counter % 10 == 0:
		await ctx.channel.send(f"JESUS you must be really bad at this game XD!")

@bot.command(name="death_check")
async def death_checker(ctx):
	global death_counter
	await ctx.channel.send(f"DEATH COUNTHER =={death_counter}")

@bot.command(name="death-reset")
async def death_reset(ctx):
	global death_counter
	if ctx.author.is_mod:
		death_counter = 0
		await ctx.channel.send(f"DEATH COUNTHER has been reset to 0")

@bot.command(name="guess")
async def guesS_number(ctx, number):
    number = int(number)
    if number == random.randint(1, 10):
        await ctx.send("yay")
 
    else:
        await ctx.send(":(")

@bot.command(name="today")
async def what_today(ctx):
	await ctx.channel.send(cur_tod)

@bot.command(name="reset_today")
async def reset_tod(ctx, *new_tod):
	global cur_tod
	new_tod = ' '.join(new_tod)
	if ctx.author.is_mod:
		cur_tod = new_tod

@bot.command(name="project")
async def what_project(ctx):
	await ctx.channel.send(cur_pro)

@bot.command(name="reset_project")
async def reset_pro(ctx, *new_pro):
	global cur_pro
	new_pro =' '.join(new_pro)
	if ctx.author.is_mod:
		cur_pro = new_pro

@bot.command(name="help",aliases=["commands", "github"])
async def command_list(ctx):
	await ctx.channel.send(f"https://github.com/ryantupo/command-list/blob/master/README.md")

@bot.command(name="kill")
async def kill_command(ctx):
    sys.exit()

@bot.command(name="so")
async def shout_out(ctx, *who):
	who = ' '.join(who)
	if who == "me":
		await ctx.channel.send(f"you ever meet this guy ---> @{ctx.author.name}! there such a LEGEND!")
	else:
		await ctx.channel.send(f"you ever meet this guy ---> @{who}! they're such a LEGEND!")

@bot.command(name="play_tictactoe")
async def board(ctx):
	global boardT
	await tic_resetV()
	await board_print_tw(ctx)
	await ctx.channel.send(f"Game of TicTacToe started! type numbers from 0-8 to choose which space you want to use")
	await ctx.channel.send(f"Game of TicTacToe started! Anyone can play just take it in turns :D")

@bot.command(name="reset_tictactoe")
async def tic_reset(ctx):
	if ctx.author.is_mod:
		global win
		global win
		global turn
		global first_player
		global second_player
		global turn_count
		win = False
		global boardT
		boardT = boardTOG.copy()
		turn = True
		turn_count = 0
		first_player = "Player 1"
		second_player = "Player 2"

@bot.command(name="play_X",aliases=["play_x"])
async def play_x(ctx, x_entry):
	global boardT
	global win
	global first_player
	global turn
	global second_player
	global turn_count
	if turn == True:
		if first_player == "Player 1":
			if second_player == first_player:
				pass
			else:
				first_player = ctx.author.name
		if ctx.author.name == first_player:
			try:
				
				x_entry = int(x_entry)
				if((x_entry >= 0) and (x_entry<= 8) and (boardT[x_entry] !="X") and (boardT[x_entry] !="O")):
					boardT[x_entry]=("X")
					turn_count += 1
					win =win_clause(boardT)
					if win == True:
						await ctx.channel.send(f" ---> @{ctx.author.name}! Just won that TicTacToe game!")
						await board_print_tw(ctx)
						await tic_resetV()
						first_player = "Player 1"
						second_player = "Player 2"
						win = False
						
					elif win == False:
						await board_print_tw(ctx)
						turn = False
						if turn_count == 9:
							await ctx.channel.send(f"No one won that ended in a draw :(")
							await tic_resetV()

				elif(boardT[x_entry] == "X" or boardT[x_entry] == "O"):
					await ctx.channel.send(f"Space already taken try again!")
				
			except Exception as e:
				print(str(e))
		else:
			await ctx.channel.send(f"Please wait until {first_player}'s turn is over")
	else:
		await ctx.channel.send(f"Please wait until {second_player}'s turn is over")
		
@bot.command(name="play_O",aliases=["play_o"])
async def play_O(ctx, O_entry):
	global boardT
	global win
	global second_player
	global turn
	global first_player
	global turn_count
	if turn == False:
		if second_player == "Player 2":
			if ctx.author.name == first_player:
				pass
			else:
				second_player = ctx.author.name
		if ctx.author.name == second_player:
			try:
				
				O_entry = int(O_entry)
				if((O_entry >= 0) and (O_entry<= 8) and (boardT[O_entry] !="X") and (boardT[O_entry] !="O")):
					boardT[O_entry]=("O")
					turn_count += 1
					win =win_clause(boardT)
					if win == True:
						await ctx.channel.send(f" ---> @{ctx.author.name}! Just won that TicTacToe game!")
						await board_print_tw(ctx)
						await tic_resetV()
						first_player = "Player 1"
						second_player = "Player 2"
						win = False
						
					elif win == False:
						await board_print_tw(ctx)
						turn = True
						if turn_count == 9:
							await ctx.channel.send(f"No one won that ended in a draw :(")
							await tic_resetV()
							


				elif(boardT[O_entry] == "X" or boardT[O_entry] == "O"):
					await ctx.channel.send(f"Space already taken try again!")
				
			except Exception as e:
				print(str(e))
		else:
			await ctx.channel.send(f"Please wait until {second_player}'s turn is over")
	else:
		await ctx.channel.send(f"Please wait until {first_player}'s turn is over")

@bot.command(name="play")
async def check_file(ctx, file):
	global used
	global freq
	values = int(float(r.hget(ctx.author.name, "thicc")))
	if values > 0:
		if ("!play" not in used or time.time() - used["!play"] > freq):
			used["!play"] = time.time()
			script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
			rel_path = "sounds/"+(file)+".mp3"
			abs_file_path = os.path.join(script_dir, rel_path)
			if os.path.isfile(abs_file_path):
				playsound(abs_file_path)

				#server verions -------------------------------------
				
				values = values - 1 
				r.hset(ctx.author.name, "thicc", values)
				#----------------------------------------------------

				
			
			
			else:
				script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
				rel_path = "sounds/"+(file)+".wav"
				abs_file_path = os.path.join(script_dir, rel_path)
				playsound(abs_file_path)

				#server verions -------------------------------------
				
				values = values - 1 
				r.hset(ctx.author.name, "thicc", values)
				#----------------------------------------------------

		else:
			await timeout(ctx)
	else:
		await ctx.channel.send(f"sorry {ctx.author.name} your out of thicc points :(")

@bot.command(name="list_play")
async def songs_list(ctx):
	global song_list 
	script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
	rel_path = "sounds"
	abs_file_path = os.path.join(script_dir, rel_path)
	for filename in os.listdir(abs_file_path):
		if filename.endswith(".wav") or filename.endswith(".mp3"):
			filename = filename.split('.')
			song_list.append("!play "+filename[0])

			continue 
		else:
			continue

	await ctx.channel.send(f"This is the list of sound effects you can use :D : {song_list[:25]}")
	await ctx.channel.send(f"{song_list[26:49]}")

@bot.command(name="supp")
async def give_point(ctx, user, amountp):
	if ctx.author.is_mod:
		values = int(float(r.hget(ctx.author.name, "thicc")))
		values = values + int(float(amountp))
		r.hset(ctx.author.name, "thicc", values)

@bot.command(name="start_bet")
async def start_bet(ctx):
	global start
	if start == False:
		start = True
		await ctx.channel.send(f"{ctx.author.name} has started a betting pot join and try to get more Thicc points!!!! use command !bet followed by how much")
		await asyncio.sleep(20)
		global bets
		global pot
		global name_pot
		await pick_winner(ctx)
		pot = 0
		name_pot.clear()
	else:
		await ctx.channel.send(f"A betting game has already been started")


@bot.command(name="bet")
async def place_bet(ctx, amount):
	values = int(float(r.hget(ctx.author.name, "thicc")))
	if (values - int(amount)) < 0:
		return
	else:
			global pot
			global users_in_bet
			global name_pot
			amount = int(amount)
			if ctx.author.name in users_in_bet:
				users_in_bet[ctx.author.name] += amount
				pot += int(amount)
				values = values - amount
				for _ in range(amount):
					name_pot.append(ctx.author.name)
			else:
				users_in_bet[ctx.author.name] = amount
				pot += int(amount)
				values = values - amount
				for _ in range(amount):
					name_pot.append(ctx.author.name)
	r.hset(ctx.author.name, "thicc", values)


@bot.command(name="fest",aliases=["playlink", "sr", "festive"])
async def festify_link(ctx):
	await ctx.channel.send(f" click this link to que music ----->  https://festify.us/party/-M8GjSBwJ1gHHoLU_EfU")


#---------------------------server version --------------------------		
@bot.command(name="thiccen",aliases=["deposit"])
async def give_thin_pointt(ctx, who, amountTP):
	if int(amountTP) < 0:
		return
	else:
		values = int(float(r.hget(ctx.author.name, "thinnie"))) 
		if (values - int(amountTP)) <0:
			await ctx.channel.send(f"you dont have enough thinnies to give away right now wait a little bit.")
			return
		else:
			who = who.split("@")
			name = (str(who[1])).lower()
			if ctx.author.name == name:
				return
			else:
				amountTP = int(amountTP)
				if values < amountTP or r.exists(name)== False:
					await ctx.channel.send(f"you dont have that many thinnie points to invest in {name} or they dont exist")
					pass
				else:
					values = values - amountTP
					name_values = int(float(r.hget(name, "thinnies_saved")))
					name_values = name_values + amountTP
					r.hset(ctx.author.name, "thinnie", values)
					r.hset(name, "thinnies_saved", name_values)

@bot.command(name="withdraw")
async def withdraw_thintothiccc(ctx, amountI):
	amountI = int(float(amountI))
	if amountI<0:
		return
	if amountI % 50 == 0:
		values = int(float(r.hget(ctx.author.name, "thinnies_saved")))
		if (values - amountI) < 0:
			await ctx.channel.send(f"you dont have enough thinnies to withdraw right now wait a little bit.")
			return
		else:
			values_thicc = int(float(r.hget(ctx.author.name, "thicc")))
			values = values - amountI
			values_thicc = values_thicc + (amountI/50)
			r.hset(ctx.author.name, "thinnies_saved", values)
			r.hset(ctx.author.name, "thicc", values_thicc)
			await ctx.channel.send(f"{ctx.author.name} has just converted! {(amountI)} thinnie points into thicc points!!")		
	else:
		await ctx.channel.send(f"you have entered an invalid number(must be divisable by 50)")

@bot.command(name="wipe")
async def wipe_someone(ctx, userC):
	if ctx.author.is_mod:
		who = userC.split("@")
		name = (str(who[1])).lower()
		values = int(float(r.hget(name, "thicc")))
		values2 = int(float(r.hget(name, "thinnie")))
		values3 = int(float(r.hget(name, "thinnies_saved")))

		values = 10
		values2 = 10
		values3 = 10
		r.hset(name, "thicc", values)
		r.hset(name, "thinnie", values2)
		r.hset(name, "thinnies_saved", values3)
	else:
		return


@bot.command(name="donate")
async def donate_alll(ctx):
	values = int(float(r.hget(ctx.author.name, "thinnie")))
	global name_of_peoples_donated_to	
	if values <= 0:
		return
	else:
		while values > 0:
			users_who_messaged.remove(ctx.author.name)
			cu = (values/len(users_who_messaged))
			for i in users_who_messaged:
				valuesD = int(float(r.hget(i, "thinnies_saved")))
				valuesD+=cu
				values=0
				r.hset(ctx.author.name, "thinnie", values)
				r.hset(i, "thinnies_saved", valuesD)
	await ctx.channel.send(f"{ctx.author.name} has just donated thinnies to {users_who_messaged} {cu} going to each person :D !!! ")
	users_who_messaged.append(ctx.author.name)




@bot.command(name="me",aliases=["howthicc"])
async def thicc_me(ctx):
	values1 = int(float(r.hget(ctx.author.name, "thicc")))
	values2 = int(float(r.hget(ctx.author.name, "thinnie")))
	values3 = int(float(r.hget(ctx.author.name, "thinnies_saved")))
	await ctx.channel.send(f"{ctx.author.name} so! you have:{values1} thicc points :D |{values2} thinnie points |{values3} thinnes in savings")


@bot.command(name= "thiccCheck",aliases=["economy"])
async def how_thicc(ctx):
	global thic_counter
	global thinnie_counter
	global savings_count
	keys = r.keys("*") 
	for name in keys:
		thi =  (int(float(r.hget(name, "thicc"))))
		thin =  (int(float(r.hget(name, "thinnie"))))
		thinS =  (int(float(r.hget(name, "thinnies_saved"))))
		thic_counter += thi
		thinnie_counter += thin
		savings_count += thinS
	await ctx.channel.send(f"Total thicc: {thic_counter} | Total thinnie: {thinnie_counter} | Total savings: {savings_count}")
	thic_counter = 0
	thinnie_counter = 0
	savings_count = 0	


@bot.command(name="wipeall")
async def wipe_all(ctx):
	if ctx.author.is_mod:
		keys = r.keys("*")
		for name in keys:
			thi =  (int(float(r.hget(name, "thicc"))))
			thin =  (int(float(r.hget(name, "thinnie"))))
			thinS =  (int(float(r.hget(name, "thinnies_saved"))))
			thi= 10
			thin = 10
			thinS = 10
			r.hset(name, "thicc", thi)
			r.hset(name, "thinnie", thin)
			r.hset(name, "thinnies_saved", thinS)



@bot.command(name="all_quotes")
async def get_them(ctx):
	for i in range(105):
		await ctx.channel.send(f"!quote {i}")

@bot.command(name="hey")
async def say_hi(ctx):
	await ctx.channel.send(f"!quote")


#leaderboard top 5 people
# 1st 2nd 3rd 4th 5th 
# example = 1st: Ryantupo
#           2nd: Vivax123

#for x, y in thisdict.items():
#  print(x, y)




#@bot.command(name="most_thicc")
#async def get_dict(ctx):#
#	print(conn.hgetall("casirus"))







if __name__ == "__main__":
	bot.run()
