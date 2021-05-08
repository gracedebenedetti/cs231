#!/usr/bin/env python3
import hashlib
import binascii


def possiblePasswords(file):
	#takes a file of passwords and reads them into a list
	passwords=[]
	c=0
	f=open(file,"r")
	for line in f:
		passwords.append(line.lower().rstrip())
		c+=1
	print(c)
	return passwords



def userDigestCombos(file):
	#reads file of all hackable passwords into a dictionary with keys as usernames and values as the password digest
	userDigests=[]
	f=open(file,"r")
	for line in f:
		fullInfo=line.split(":")
		userDigest=[fullInfo[0],fullInfo[1]]
		userDigests.append(userDigest)
	print(len(userDigests))
	return userDigests


def prepPassword(password):
	#takes a password and finds its MD5 digest
	password=password.lower()
	encodedPassword = password.encode('utf-8')
	md5 = hashlib.md5(encodedPassword)
	passwordHash = md5.digest()
	passwordHashAsHex = binascii.hexlify(passwordHash)
	passwordHashAsHexString = passwordHashAsHex.decode('utf-8')
	return passwordHashAsHexString


def passwordDict(passwords):
	# finds all single word password digests and puts them in dictionary w/ key: digest, value: password
	passDict={}
	counter=0 #counts how many hashes we computed
	for password in passwords:
		digest=prepPassword(password)
		passDict[digest]=password
		counter+=1
	passDict['hashComputed']=counter
	return passDict

def findPassword(digest,passDict):
	#performs password lookup
	return passDict.get(digest)

def doubleDict(passwords):
	passDict={}
	counter=0
	loop1=0#counts how many hashes we computed
	for i in range(len(passwords)//2,len(passwords)):
		#print(loop1)
		for p in passwords:
			doublePass=passwords[i]+p
			#print(doublePass)
			digest=prepPassword(doublePass)
			passDict[digest]=doublePass
			counter+=1
		loop1+=1
	passDict['hashComputed']=counter
	return passDict

def normDigest(digests,passwords,f):
	doubles=[]
	computed=0
	for dig in digests:
		valid=findPassword(dig[1],passwords)
		if valid != None:
			thingToAdd=dig[0]+":"+valid+'\n'
			f.write(thingToAdd)
			computed+=1
		else:
			doubles.append(dig)
	return [doubles,computed]

def doubleFinder(doubles,passwords,f):
	computed=0
	doubleD=doubleDict(passwords)
	for d in doubles[1]:
		valid=findPassword(d,doubleD)
		if valid!=None:
			computed+=1
			thingToAdd=doubles[0]+":"+valid
			f.write(thingToAdd)
	return [computed, doubleD.get('hashComputed')]


def main():
	passwordsPrev=possiblePasswords('words.txt')
	passwords=passwordDict(passwordsPrev)
	digests=userDigestCombos('givenpasswords1.txt')
	fileToWrite=open('passwords1.txt','w')
	onePassData=normDigest(digests,passwords,fileToWrite)
	doubData=doubleFinder(onePassData[0],passwordsPrev,fileToWrite)
	print(onePassData[1])
	print(doubData[0])
	print(doubData[1])
	print(passwords.get('hashComputed'))




if __name__ == '__main__':
	main()
