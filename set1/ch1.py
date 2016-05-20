import binascii

# function to return the binary for a hex number in all 8 bits
def _hex_to_bin_(h):
	return bin(int(h,16))[2:].zfill(len(h)*4)

# function to convert binary to decimal
def _bin_to_dec_(b):
	return int(b,2)

# function to convert 3 bytes to 4 groups
# need to optimize this method using 3-4 lines maximum
def _3bytes_to_4groups_(num):
	grp = []
	k=0
	temp = ""
	for i in num:
		if k<6:
			k += 1
			temp = temp + i
		else:
			grp.append(temp)
			temp = i
			k=1
	if temp!="":
		#zfill is used to add 0s in any string of a particular length at the beginning
		temp = temp.zfill(6)
		grp.append(temp)
	return grp

# function to convert the decimal to character
def _dec_to_char_(dec):
	char = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','+','/']
	return char[dec]

# function to convert 3byte hex to encoded char
def _3byte_hex_to_base64_(hex):
	bin = _hex_to_bin_(hex)
	bin_grp = _3bytes_to_4groups_(bin)
	encoded = []
	for i in bin_grp:
		dec = _bin_to_dec_(i)
		encoded.append(_dec_to_char_(dec))
	return encoded

# function to encode the hex to base64
def _hex_to_encode_(hex):
	encode = []
	for i in range(0,hex,24):
		encode.append(_3byte_hex_to_base64_(i))
	return encode


string = raw_input("enter the input string to be encoded: ")
encoded = _3byte_hex_to_base64_(string)
print ''.join(encoded)
