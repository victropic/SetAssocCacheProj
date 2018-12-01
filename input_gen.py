import random;

def getRandHexString(numChars) :
	hex = '0x';
	numToString = {10 : 'a', 11 : 'b', 12 : 'c', 13 : 'd', 14 : 'e', 15 : 'f'}
	
	for i in range(numChars) :
		num = random.randint(0, 15);
		if num < 10 :
			hex += str(num);
		else :
			hex += numToString[num];
		
	return hex;

file = open("file.txt", 'r+');
file.truncate(0);
random.seed()

for i in range(100) :
	file.write(getRandHexString(4) + ": W " + getRandHexString(4) + "\n")
