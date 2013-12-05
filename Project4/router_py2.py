# Author: Quinn Kelly
#ID: 4128785
#x500: kelly860
# Fall 2013 CSci4211: Introduction to Computer Networks
# This program serves as the router.
# Written in Python v2.


import sys
from socket import *

def main():
	host = "localhost" # Remote hostname. It can be changed to anything you desire.
	port = 5001 # Port number.

	try:
		cSock = socket(AF_INET, SOCK_STREAM)
	except error as msg:
		cSock = None # Handle exception
	
	try:
		cSock.connect((host, port))
	except error as msg:
		cSock = None # Handle exception

	if cSock is None:
		print("Error: cannot open socket")
		sys.exit(1) # If the socket cannot be opened, quit the program.

	#Take in the string sent by the test program
	sent_string = cSock.recv(4096).decode().strip() 
	data = sent_string
	print("Received:", data)
	st = "ACK\n"
	cSock.send(st.encode())	

	double_Array=stringstrip(sent_string)
	MAC_dict=switch_table(double_Array)

###############################
#  Function to strip String   #    
###############################
def stringstrip(sent_string):

	double_Array = [[0 for x in xrange(1)] for x in xrange(3)]
	split= sent_string.split(" ")
	j=0
	print"Quick Length Check... "
	len1=len(split)
	print(len1)
	len2 = len(double_Array)
	print(len2)

	#for loop to build list
	for list in split:
		double_Array[j] = split[j]
		j=j+1
	print"String Stripped, let's have a look: "
	print(double_Array)
	print(len(double_Array))
	return double_Array


#################################
# Build the exmpty switch table #  
#################################
#this isn't a very good way to do this, cuz a key may not be able to 
#have multiple values
def switch_table(double_Array):
	# MAC_hash={}
	# MAC_hash[double_Array[0]]=double_Array[1]
	# #MAC_hash[double_Array[0]]+=double_Array[2]
	# if (MAC_hash[double_Array[0]] == double_Array[1]):
	# 	#print (MAC_hash[double_Array[0]])
	# 	print"match nerd!"
	MAC_dict = dict()

	for line in double_Array:
		if line[0] in MAC_dict:
			MAC_dict[double_Array[0].append(double_Array[1])]
		else:
			MAC_dict[double_Array[0]] = [double_Array[1]]
	print(MAC_dict['0'])
	return MAC_dict	

#################################
#    Self-learning & Checks     #
#################################
#here we will implement the switches self-learning abilities
#This function also sends the messages bac to the test program

def check_table(MAC_dict,double_Array):
	



main()

