#First attempt, not used in final
import hashlib
import binascii

def createMD5Dict():
    MD5Dict = {}
    passwords = [line.strip().lower() for line in open('givenpasswords1.txt')]
    for login in passwords:
        login = login.split(":")
        username = login[0]
        MDhash = login[1]
        MD5Dict[MDhash] = username
    return MD5Dict

def createWordDict():
    hashCount = 0
    wordDict = {}
    words = [line.strip().lower() for line in open('words.txt')]
    for password in words:
        encodedPassword = password.encode('utf-8')
        md5 = hashlib.md5(encodedPassword)
        passwordHash = md5.digest()
        passwordHashAsHex = binascii.hexlify(passwordHash)
        passwordHashAsHexString = passwordHashAsHex.decode('utf-8')
        hashCount += 1
        wordDict[passwordHashAsHexString] = password
    print(hashCount)
    return wordDict

#####PROBLEM2#########

def createSaltHash():
    saltMD5Dict = {}
    passwords = [line.strip().lower() for line in open('givenpasswords2.txt')]
    for login in passwords:
        login = login.split(":")
        username = login[0]
        MDhash = login[1] #this includes salt$salthash+passwordhash
        MDhash = MDhash.split("$")
        salt = MDhash[0]
        encodedSalt = salt.encode('utf-8')
        md5Salt = hashlib.md5(encodedSalt)
        saltHash = md5Salt.digest()
        saltHashAsHex = binascii.hexlify(saltHash)
        saltHashAsHexString = saltHashAsHex.decode('utf-8')
        hashSalt = MDhash[1] #salt hash concatenated with password hash
        saltMD5Dict[hashSalt] = username
    return saltHashAsHexString, saltMD5Dict

def createSaltedWordDict():
    hashCount = 0
    wordDict = {}
    words = [line.strip().lower() for line in open('words.txt')]
    for password in words:
        encodedPassword = password.encode('utf-8')
        md5 = hashlib.md5(encodedPassword)
        passwordHash = md5.digest()
        passwordHashAsHex = binascii.hexlify(passwordHash)
        passwordHashAsHexString = passwordHashAsHex.decode('utf-8')
        hashCount += 1
        wordDict[password] = passwordHashAsHexString
    print(hashCount)
    return wordDict

def computePossiblePasswords(saltHash):
    wordDict = createSaltedWordDict()
    checkPasswordDict = {}
    for key in wordDict:
        checkPasswordDict[saltHash+wordDict[key]] = key
    return checkPasswordDict

def problem2():
    numSaltPasswords = 0
    saltMD5Dict = createSaltHash()[1]
    saltHashAsHexString = createSaltHash()[0]
    checkPasswordDict = computePossiblePasswords(saltHashAsHexString)
    for key in saltMD5Dict:
        if key in checkPasswordDict:
            foundPasswords[saltMD5Dict[key]] = checkPasswordDict[key]
            numSaltPasswords += 1
            #print (MD5Dict[key] + ":" + wordDict[key])
    print(numSaltPasswords)
    
##SKYLER
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

def saltDigestCombos(file):
	#reads file of all hackable passwords into a dictionary with keys as usernames and values as the password digest
	userDigests=[]
	f=open(file,"r")
	for line in f:
		fullInfo=line.split(":")
		saltDig=fullInfo.split('$')
		salt=saltDig[0]
		dig=saltDig[1]
		userDigest=[fullInfo[0],salt,dig]
		userDigests.append(userDigest)
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


def salted(salt,passwords,saltedDigest):
	for p in passwords:
		print(prepPassword(salt+p))
		if prepPassword(salt+p)==saltedDigest:
			return p
	return None


def saltDigest(passwords,saltDigs,f):
	computed=0
	for dig in saltDigs:
		valid=salted(dig[1],passwords,dig[2])
		if valid!=None:
			thingToAdd=dig[0][0]+':'+valid
			f.write(thingToAdd)
			print(thingToAdd)
			computed+=1
	print(computed)

##SKYLER DONE

def main():
    numPasswords = 0
    foundPasswords = {}
    MD5Dict = createMD5Dict()
    wordDict = createWordDict()
    for key in MD5Dict:
        if key in wordDict:
            foundPasswords[MD5Dict[key]] = wordDict[key]
            numPasswords += 1
            #print (MD5Dict[key] + ":" + wordDict[key])
    print(numPasswords)


if __name__ == "__main__":
    problem2()
