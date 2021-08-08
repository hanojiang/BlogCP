
from  ctypes import * 


def generateKey(seed_input):
	lib = cdll.LoadLibrary("libkeygen.so")
	seed_data = c_char * 4
	seed = seed_data()
	for i in range(4):
		seed[i] = seed_input[i]
	
	key_data = c_char * 4
	key = key_data()
	  
	lib.GenerateKeyEx(seed, 4, key)
	key_output = []
	for i in range(4):
		print(hex(key[i][0]))
		key_output.append(hex(key[i][0])
    #print(key_output)	
	#return key_output
	


a = [0x28, 0x27, 0x7c, 0x00]
generateKey(a)
#print(b)