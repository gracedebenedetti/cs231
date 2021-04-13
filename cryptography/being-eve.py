def rsaFinder(num):
	#finds the prime numbers p and q that could mutliply to be n
	for i in range(2,num//2):
		if num%i==0:
			print(str(num/i)+" "+str(i))

def dFinder(trials):
	for i in range(limit):
		if 31*i%(4524)==1:
			print(i)

list = [2677, 4254, 1152, 4645, 4227, 1583, 2252, 426, 3492, 4227, 3889, 1789, 4254, 1704, 1301, 4227, 1420, 1789, 1821, 1466, 4227, 2252, 3303, 1420, 2234, 4227, 4227, 1789, 1420, 1420, 4402, 1466, 4070, 3278, 3278, 414, 414, 414, 2234, 1466, 1704, 1789, 2955, 4254, 1821, 4254, 4645, 2234, 1704, 2252, 3282, 3278, 426, 2991, 2252, 1604, 3278, 1152, 4645, 1704, 1789, 1821, 4484, 4254, 1466, 3278, 1512, 3602, 1221, 1872, 3278, 1221, 1512, 3278, 4254, 1435, 3282, 1152, 1821, 2991, 1945, 1420, 4645, 1152, 1704, 1301, 1821, 2955, 1604, 1945, 1221, 2234, 1789, 1420, 3282, 2991, 4227, 4410, 1821, 1301, 4254, 1466, 3454, 4227, 4410, 2252, 3303, 4645, 4227, 3815, 4645, 1821, 4254, 2955, 2566, 3492, 4227, 3563, 2991, 1821, 1704, 4254]
d = 2335
n = 4661

def decrypt(list, d, n):
    message = []
    for number in list:
        newNumber = (number**(d)) % n
        message.append(newNumber)
    wordMessage = ''
    for number in message:
        letter = chr(number)
        wordMessage = wordMessage + letter
    return wordMessage

output: 'Dear Bob, Check this out.  https://www.schneier.com/blog/archives/2017/12/e-mail_tracking_1.html Yikes! Your friend, Alice'
