import hashlib
import binascii

def decryptMD5():
    passwords = [line.strip().lower() for line in open('passwords1.txt')]
    words = [line.strip().lower() for line in open('words.txt')]
    foundPasswords = {}
    for login in passwords:
        login.split(":")
        username = login[0]
        MDhash = login[1]
        for password in words:
            # Compute the MD5 hash of this example password
            #print('password ({0}): {1}'.format(type(password), password))

            encodedPassword = password.encode('utf-8') # type=bytes
            #print('encodedPassword ({0}): {1}'.format(type(encodedPassword), encodedPassword))

            md5 = hashlib.md5(encodedPassword)
            passwordHash = md5.digest() # type=bytes
            #print('passwordHash ({0}): {1}'.format(type(passwordHash), passwordHash))

            passwordHashAsHex = binascii.hexlify(passwordHash) # weirdly, still type=bytes
            #print('passwordHashAsHex ({0}): {1}'.format(type(passwordHashAsHex), passwordHashAsHex))

            passwordHashAsHexString = passwordHashAsHex.decode('utf-8') # type=string
            #print('passwordHashAsHexString ({0}): {1}'.format(type(passwordHashAsHexString), passwordHashAsHexString))
            if passwordHashAsHexString == MDhash:
                foundPasswords[username] = password
                print(foundPasswords)
    return foundPasswords

if __name__ == "__main__":
    decryptMD5()
