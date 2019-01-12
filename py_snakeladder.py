import copy,random
from colorama import Fore, Style

def diceprogram():
	dice=random.randint(1,6)
	print("You got "+str(dice),end="")
	if(dice==1):
		print("""
	 _______
	|       |
	|   *   |
	|_______|""")
	elif(dice==2):
		print("""
	 _______
	|       |
	|*     *|
	|_______|""")
	elif(dice==3):
		print("""
	 _______
	|       |
	|*  *  *|
	|_______|""")
	elif(dice==4):
		print("""
	 _______
	|*     *|
	|       |
	|*_____*|""")
	elif(dice==5):
		print("""
	 _______
	|*     *|
	|   *   |
	|*_____*|""")
	elif(dice==6):
		print("""
	 _______
	|*     *|
	|*     *|
	|*_____*|""")
	return dice

def snakeladder(sumtake):
	newsum=0
	if(sumtake==2):
		print("Yay! You found a ladder")
		print("Jump To 76")
		newsum=76
	elif(sumtake==12):
		print("Yay! You found a ladder")
		print("Jump To 50")
		newsum=50
	elif(sumtake==32):
		print("Yay! You found a ladder")
		print("Jump To 59")
		newsum=59
	elif(sumtake==45):
		print("Yay! You found a ladder")
		print("Jump To 82")
		newsum=82
	elif(sumtake==69):
		print("Yay! You found a ladder")
		print("Jump To 77")
		newsum=77
	elif(sumtake==40):
		print("Damn! A Snake bit you")
		print("Slide To 16")
		newsum=16
	elif(sumtake==60):
		print("Damn! A Snake bit you")
		print("Slide To 25")
		newsum=25
	elif(sumtake==74):
		print("Damn! A Snake bit you")
		print("Slide To 50")
		newsum=50
	elif(sumtake==88):
		print("Damn! A Snake bit you")
		print("Slide To 41")
		newsum=41
	elif(sumtake==92):
		print("Damn! A Snake bit you")
		print("Slide To 12")
		newsum=12
	if(newsum):
		halt=input()
	return newsum

def initialize():
	L=[]
	declare=100
	for i in range(10):
		l=[]
		for j in range(10):
			l.append(declare)
		L.append(l)

	for i in range(10):
		if(i%2==1):
			m=-1
			n=-11
			o=-1
			for j in range(m,n,o):
				L[i][j]=declare
				declare-=1
		elif(i%2==0):
			m=0
			n=10
			o=1
			for j in range(m,n,o):
				L[i][j]=declare
				declare-=1
	return L

def printb(L,Lnew,sum):
	print("")
	for a in range(10):
		for b in range(10):
			if(sum[0]==Lnew[a][b] or sum[1]==Lnew[a][b] or sum[2]==Lnew[a][b] or sum[3]==Lnew[a][b]):
				print(Fore.RED + str(L[a][b]),end="")
				print(Style.RESET_ALL,end=" ")
			else:
				print(L[a][b],end=" ")
		print("")
	print("")

def maingame(noofplayers,L,name,player,stager):
	n=True
	Lnew=copy.deepcopy(L)
	sum=[0,0,0,0]
	prevalue=[100,100,100,100]
	prev_a=[0,0,0,0]
	prev_b=[0,0,0,0]

	while(n==True):
		for i in range(noofplayers):
			printb(L,Lnew,sum)
			L[prev_a[i]][prev_b[i]]=prevalue[i]

			print(player[i]+" turn",end="")
			halt=input()
			dice=diceprogram()
			halt=input("Press enter to move your marker")
			sum[i]=sum[i]+dice

			sum[i]=snakeladder(sum[i])

			if(sum[i]==100):
				n=False
				print(name[i]+" Won !!")
				break
			elif(sum[i]>100):
				sum[i]=sum[i]-dice
				remain=100-sum1
				print(name1+" You cannot move ahead")
				print("You need "+remain+" to Win\n")
				halt=input()

			toplace=stager[i]
			for z in range(noofplayers):
				if(sum[i]==sum[z] and i!=z):
					toplace+=stager[z]

			for a in range(10):
				for b in range(10):
					if(sum[i]==Lnew[a][b]):
						prevalue[i]=Lnew[a][b]
						prev_a[i]=a
						prev_b[i]=b
						L[a][b]="["+toplace+"]"
						break

if __name__ == '__main__':
	print("""
	Welcome to Snake&Ladders v0.9

	Instructions:
	1. Everybody plays with the initials of their names
	2. Your dice is rolled automatically when it's your turn
	3. Your token will move ahead automatically
	4. Reach the tile 100 with your token to win the game

	""")

	name=stager=["","","",""]
	player=[]
	L=initialize()

	noofplayers=int(input("How many Players are playing: "))
	for i in range(noofplayers):
		player.append(str(input("Enter name of "+str(i+1)+" Player: ")))
		player[i]=player[i].capitalize()
		name[i]=player[i]
		stager[i]=player[i][0]
		player[i]+="'s"

	maingame(noofplayers,L,name,player,stager)
