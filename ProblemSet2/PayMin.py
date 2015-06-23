balance = 5000
annualInterestRate = 0.18
monthlyPaymentRate = 0.02 
interest = 0
totalPaid=0
for x in range(12):
	print "Month: ",x+1
	minMonthPayment = monthlyPaymentRate * balance
	totalPaid += minMonthPayment
	balance = balance - minMonthPayment
	interest = (annualInterestRate / 12) * balance
	balance = balance + interest
	print "Minimum monthly payment: ", round(minMonthPayment,2)
	print "Remaining balance: ",round(balance,2)
print "Total paid: ", round(totalPaid,2)
print "Remaining balance: ",round(balance,2)
