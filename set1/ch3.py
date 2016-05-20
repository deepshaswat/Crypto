str = raw_input("Enter the hex string: ")
key = (int(str,16)^ int(str,16))
print key
decoded = int(str,16) ^ key
print decoded
