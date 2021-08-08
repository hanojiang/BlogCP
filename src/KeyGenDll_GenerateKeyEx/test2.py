from  ctypes import * 
     




def keyGen(seed_input):
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
		key_output.append(key[i][0])

	return key_output

a = [0x28, 0x27, 0x7c, 0x00]
key = keyGen(a)
print(key)
	
