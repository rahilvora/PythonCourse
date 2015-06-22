s=raw_input("String Please ")
maxlength=0
tempString=""
perString=""
count=1
temp=0
for i in range(len(s)):
	for j in range(temp,len(s)):
		if s[j] not in tempString:
			count +=1
			tempString += s[j]
		else:
			break
	if(count>maxlength):
		maxlength=count
		perString=tempString
	count=0
	tempString=""
print "Longest substring is: ",perString
