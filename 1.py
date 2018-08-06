text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

alphabet_range = range(26)
intab = ''.join([chr(97+x%26) for x in alphabet_range]) 
outtab = ''.join([chr(97+(x+2)%26) for x in alphabet_range])

trantab = str.maketrans(intab, outtab)

print(text.translate(trantab)) 

print('map'.translate(trantab))