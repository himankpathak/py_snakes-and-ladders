from random import *

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

def printb(L):
	for a in range(10):
	for b in range(10):
	print(L[a][b],end=" ")
	print("")



if __name__ == '__main__':
	print("""
	Welcome to Snake&Ladders v0.9

	Instructions:
	1. Everybody plays with the initials of their names
	2. Your dice is rolled automatically when it's your turn

	""")

	n=True
	sum=[0,0,0,0]
	prevalue=[100,100,100,100]
	prev_a=[0,0,0,0]
	prev_b=[0,0,0,0]
	player=name=stager=["","","",""]

	L=initialize()
	printb(L)

	noofplayers=int(input("How many Players are playing: "))
	for i in range(noofplayers):
	player[i]=str(input("Enter name of "+str(i+1)+" Player: "))
	player[i]=player[i].capitalize()
	name[i]=player[i]
	stager[i]=player[i][0]
	stager[i]="["+stager[i]+"]"
	player[i]+="'s"

	maingame()
