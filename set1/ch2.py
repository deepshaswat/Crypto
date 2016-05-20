str1 = raw_input("Enter the hex string: ")
str2 = raw_input("Enter the dec string: ")
str = hex(int(str1,16)^ int(str2,16))
print str
