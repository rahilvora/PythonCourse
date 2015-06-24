balance = 320000
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12
unPaid = balance
lowerBound = balance / 12
upperBound = (balance * (1 + monthlyInterestRate) ** 12) / 12.
monthlyPayment = 0
presion = 0.10


while balance >= presion:
	monthlyPayment = (lowerBound + upperBound) / 2
	for x in range(12):
		minMonthPayment = monthlyPayment
		balance = balance - minMonthPayment
		if(balance <= 0):
			break
		else:
			interest = (annualInterestRate / 12) * balance
			balance = balance + interest
	if balance < 0:
		upperBound = monthlyPayment
		balance = unPaid
	elif balance > presion:
		lowerBound = monthlyPayment
		balance = unPaid
print "Lowest Payment: ", round(monthlyPayment,2)

