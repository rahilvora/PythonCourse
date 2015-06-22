string=raw_input("Enter the string ")
count=0
for v in string:
	if v == 'a' or v == 'e' or v == 'i' or v == 'o' or v == 'u':
		count +=1
print ("Number of vowels", count)