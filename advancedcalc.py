#!/usr/bin/python

import time
import math 



while True:
	print ("""You have 4 options. They are:
1. Addition
2. Subtraction
3. Multiplication
4. Division
""")

	menu_choice = int(input("Please choose an option: "))
	print ("")
	time.sleep(1)
	if menu_choice == 1:
		print ("Addition")
		print ("")
		num1 = float(input("Enter the first number: "))
		num2 = float(input("Enter the second number: "))
		print ("The answer is: ", (num1 + num2))
		time.sleep(2)
		print ("")
		break
	
	if menu_choice == 2:
		print ("Subraction")
		print ("")	
		num1 = float(input("Enter the first number: "))
		num2 = float(input("Enter the second number: "))
		print ("The andwer is", (num1 - num2))
		time.sleep(2)
		print("")
		break

	if menu_choice == 3: 
		print ("Multiplication")
		print ("")
		num1 = float(input("Enter the first number: "))
		num2 = float(input("Enter the second number: "))
		print ("The answer is", (num1 * num2))
		time.sleep(2)
		print("")
		break
	
	if menu_choice == 4:
		print ("Division")
		print ("")	
		num1 = float(input("Enter the first number: "))
		num2 = float(input("Enter the second number: "))
		print ("The answer is", (num1/num2))
		time.sleep(2)
		print ("")
		break

		
	else:
		print ("Invalid input!")
3









