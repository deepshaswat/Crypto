import base64
string = raw_input("enter the input string to be encoded: ")
text = string.decode("hex")
encoded = base64.b64encode(text)
print "Encoded text: "
print encoded
