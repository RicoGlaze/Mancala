import random
import time
import os
import copy

#Fills the game board with default values.
def startBoard():
	for i in range(len(board)):
		if i == 6 or i==13:
			board[i]=0
		else:
			board[i] = 4
			
#Displays the boards values to the user, player one on left.		
def showBoard():
	print('P1~~~~~P2')
	for i in range(4):
		if i == 0:
			print(' ',end='')
		print('-',end=' ')
	print()
	print(' '+'|'+'<'+' '+str(board[13])+' '+'>'+'|')
	for j in range(6):
		print(str(j)+'|',end=str(board[j])+'|')
		for i in range(5):
			if i==2:
				print('~',end='')
			else:
				print('',end='')
		print('|'+str(board[12-j]),end='|'+str(12-j))
		print()
	print(' '+'|'+'<'+' '+str(board[6])+' '+'>'+'|')
	for i in range(4):
		if i==0:
			print(' ',end='')
		print('-',end=' ')
	print()
	
#Chooses player who goes first randomly,
#is also used to switch players after intitial values.		
def choosePlayer(firstPlay):
	firstPlay=random.randint(0,1)
	return firstPlay
	
#Using the index players choose this distributes the
#mancala marbles properly into a wrap around list.
def updateBoard(index,turn):
	buffer = 0
	for i in range(board[index]+1):
		if (turn ==0 and(i+index)%len(board)==13):
			buffer=buffer+1
			board[(i+index+buffer)%len(board)]=board[(i+index+buffer)%len(board)]+1
			board[index]=board[index]-1
			showBoard()
			time.sleep(.13)
			os.system('clear')
		elif (turn==1 and (i+index)%len(board)==6):
			buffer=buffer+1
			board[(i+index+buffer)%len(board)]=board[(i+index+buffer)%len(board)]+1
			board[index]=board[index]-1
			showBoard()
			time.sleep(.13)
			os.system('clear')
		else:
			board[(i+index+buffer)%len(board)]=board[(i+index+buffer)%len(board)]+1
			board[index]=board[index]-1
			lastIndexValue=copy.deepcopy((i+index+buffer)%len(board))
			showBoard()
			time.sleep(.13)
			os.system('clear')
	return lastIndexValue

#Validates the index chosen is not either players scoring
#holes.(6 or 13)
def checkValid(index,firstPlay,gameMode):
	index = '6'
	if firstPlay==0:
		while index == '6' or index == '13' or board[int(index)]==0 or int(index)>5 or int(index)<0:
			print('Player Ones Turn')
			print()
			print('0-5')
			print('Enter a value:',end='')
			index=input()
		return int(index)
######################A.I####################		
	elif firstPlay==1 and gameMode=='onePlayer':
		while index == '6' or index == '13' or board[int(index)]==0 or int(index)<7 or int(index)>13:
			index=artIntel()
			print(index)
			input()
		return int(index)
############################################		
	elif firstPlay==1 and gameMode=='twoPlayer':
		while index == '6' or index == '13' or board[int(index)]==0 or int(index)<7 or int(index)>13:
			print('Player Twos Turn')
			print()
			print('7-12')
			print('Enter a value:',end='')
			index=input()
		return int(index)

#Checks if either player has no marbles left on their side
#of the board and if so ends the game loop.		
def checkWinner(gameOver):
	if (board[0],board[1],board[2],board[3],board[4],board[5])==(0,0,0,0,0,0):
		gameOver=True
		return gameOver
		
	elif (board[7],board[8],board[9],board[10],board[11],board[12])==(0,0,0,0,0,0):
		gameOver=True
		return gameOver
		
	else:
		gameOver=False
		return gameOver

#If game loop is over each players side is added to their
#own score holes.
def finalScores():
	board[6]=board[6]+(board[0]+board[1]+board[2]+board[3]+board[4]+board[5])
	board[13]=board[13]+(board[7]+board[8]+board[9]+board[10]+board[11]+board[12])
	for i in range(len(board)):
		if i == 6 or i ==13:
			None
		else:
			board[i]=0

#Checks if players last move ended on an empty index,
#if so they get the values in that hole and the one opposite
#added to their score hole.	
def checkLast(lastIndex,firstPlay,distanceFromZero):
	if board[lastIndexValue] ==1 and firstPlay ==0 and lastIndexValue>-1 and lastIndexValue<6:
		for i in range(6):
			if board[i]==board[lastIndexValue] and i==distanceFromZero:
				board[6]=board[6]+board[i]
				board[i]=0
				board[6]=board[6]+board[12-i]
				board[12-i]=0
				firstPlay = 1
				return firstPlay
				
	elif board[lastIndexValue] ==1 and firstPlay ==1 and lastIndexValue>6 and lastIndexValue<13:
		for i in range(6):
			if board[12-i]==board[lastIndexValue] and i==distanceFromZero:
				board[13]=board[13]+board[12-i]
				board[12-i]=0
				board[13]=board[13]+board[i]
				board[i]=0
				firstPlay=0
				return firstPlay
				
	elif lastIndexValue == 6 and firstPlay == 0:
		firstPlay=0
		return firstPlay
		
	elif lastIndexValue == 13 and firstPlay ==1:
		firstPlay=1
		return firstPlay
		
	elif firstPlay == 1:
		firstPlay=0
		return firstPlay
		
	else:
		firstPlay=1
		return firstPlay
		
#Returns the distance (0-5) the last index changed is from
#the top of each players side of the board.		
def convertIndex(lastIndexValue,firstPlay):
	if firstPlay==0:
		for i in range(6):
			if i==lastIndexValue:
				return i
	elif firstPlay==1:
		for i in range(6):
			if 12-i==lastIndexValue:
				return i
				
def menu():
	mode=' '
	print('~~~~~MANCALA~~~~~')
	print()
	print('a.1 Player')
	print('b.2 Player')
	print()
	print('Choose game mode:',end='')
	mode=input()
	if mode=='a':
		return 'onePlayer'
	elif mode=='b':
		return 'twoPlayer'

def replay(playAgain):
	choice=' '
	print('Do you want to play again? (yes or no)')
	choice=input().lower()
	if choice.startswith('y'):
		playAgain=True
		return playAgain
	else:
		playAgain=False
		return playAgain
#A.I chooses move in this order;
#Any move that gives a second chance(lands in score hole).
#Any move in which last marble lands in an empty spot on its side.
#Choose index with largest value.
def artIntel():
	tempBoard=[0]*14
	randomMove=0
	largestValue=0
	for i in range(len(tempBoard)):
		tempBoard[i]=board[i]
	for j in range(6):
		if tempBoard[12-j]==j+1 or tempBoard[12-j]==j+14:
			return (12-j)
	for j in range(6):
		for i in range(6):
			if tempBoard[((12-j)+tempBoard[12-j]%len(tempBoard))==tempBoard[12-i]] and tempBoard[12-i]==0 and tempBoard[12-j]!=0:
				return (12-j)
	for i in range(6):
		if largestValue < tempBoard[12-i]:
			largestValue=tempBoard[12-i]
	for j in range(6):
		if tempBoard[12-i]==largestValue:
			return (12-i)
	while randomMove<7 or randomMove>13 or tempBoard[randomMove]==0:
		randomMove=random.randint(7,12)
	return randomMove
	
##################MAIN######################
board=[0]*14
firstPlay=0
index=0
gameOver=False
playAgain=True
lastIndexValue=0
distanceFromZero=0
gameMode=' '

#Setting initial board values
while playAgain==True:
	os.system('clear')
	gameMode=menu()
	startBoard()
	firstPlay=choosePlayer(firstPlay)
	#Game loop
	while gameOver==False:
		os.system('clear')
		showBoard()
		index=checkValid(index, firstPlay,gameMode)
		lastIndexValue=updateBoard(index,firstPlay)
		distanceFromZero=convertIndex(lastIndexValue,firstPlay)
		firstPlay=checkLast(lastIndexValue,firstPlay,distanceFromZero)
		gameOver=checkWinner(gameOver)
	#Final scoring
	finalScores()
	showBoard()
	if board[6]>board[13]:
		print('Player One Won! '+str(board[6])+' to '+str(board[13]))
	elif board[6]==board[13]:
		print('Game Tie!')
	else:
		print('Player Two Won! '+str(board[13])+' to '+str(board[6]))
	playAgain=replay(playAgain)
	gameOver=False
