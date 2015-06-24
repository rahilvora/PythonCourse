balance = 4145
annualInterestRate = 0.18
unPaid = balance
interest = 0
monthlyPayment = 100

while True:
	for x in range(12):
		minMonthPayment = monthlyPayment
		balance = balance - minMonthPayment
		if (balance <= 0):
			break
		else:
			interest = (annualInterestRate / 12) * balance
			balance = balance + interest
	print "Per month",minMonthPayment
	print "Remaining balance: ",round(balance,2)
		
	if balance <= 0:
		print "Lowest Payment: ", minMonthPayment
		break
	else:
		monthlyPayment += 10
		balance = unPaid
