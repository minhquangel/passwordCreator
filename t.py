import random
import string
from random import seed
from random import randint

def id_generator(size=32, chars = string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

seed(1)

f = open("bigFile.txt", "a")
str = ""
for i in range (0, 1000000):
	value = randint(32, 128)
	str = id_generator(value)
	f.write(str)
	f.write("\n")
f.close()