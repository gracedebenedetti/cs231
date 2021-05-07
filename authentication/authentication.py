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

def createSaltHash():
    saltMD5Dict = {}
    passwords = [line.strip().lower() for line in open('givenpasswords2.txt')]
    for login in passwords:
        login.split(":")
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

createSaltedWordDict():
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
    main()
