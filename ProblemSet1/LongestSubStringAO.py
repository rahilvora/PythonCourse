s=raw_input("String Please ")
maxL=0
tempString=""
perString=""
count=1
flag=0
for i in range(len(s)):
    if tempString == "":
        tempString += s[i]
    if i+1 < len(s) and s[i+1]>=s[i]:
        tempString += s[i+1]
        count += 1
        flag=1
    else:
        count=1
        tempString=""

    if(count>maxL):
        preString=tempString
        maxL=count
if flag == 0:
    preString=s[0]

print ("Longest substring in alphabetical order is: ",preString)