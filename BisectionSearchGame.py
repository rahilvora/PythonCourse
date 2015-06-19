
userInput=int(raw_input("Please think of a number between 0 and 100!"))
low=0
high=100
if(userInput>-1 and userInput<100):
	ans=(low+high)/2
	while low<high:
		print("Is your secret number",ans)
		choice=raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
		if choice=="h":
			high=ans-1
			ans=(low+high)/2
		elif choice=="l":
			low=ans+1
			ans=(low+high)/2
		elif choice=="c":
			print("Game over. Your secret number was:",ans)
			break
		else:
			print("Sorry, I did not understand your input.")
else:
	print("Wrong Inputs")