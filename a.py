
'''
s=raw_input("Enter the string ")
s=s.lower()
print s.count("bob")
'''

'''
sb = 'bob'
results = 0
sub_len = len(sb)
for i in range(len(s)):
    if s[i:i+sub_len] == sb:
        results += 1
print results
'''
'''
def gcditer(a,b):
	if b == 1:
		return 1
	elif a % b == 0 and b % b == 0:
		return b
	else:
		gcditer(a,b-1)

    

print gcditer(5,10)
'''
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
    print L

def createabs(param):
	return abs(param)

applyToEach([1, -4, 8, -9],createabs)