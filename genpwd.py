import random
import string
from random import randrange

def id_generator(size=10000, chars=string.ascii_letters + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

f1 = open("bigString.txt", "w+")
f2 = open("indexes.txt", "w+")
strR = id_generator()

pwd = ""
for x in range(0, 16):
	a = randrange(10000)
	
	pwd = pwd + strR[a]
	
	f2.write(str(a))
	f2.write("\n")

print("Password: " + pwd)

f1.write(strR)



f1.close()
f2.close()