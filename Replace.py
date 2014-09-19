# Tigran Hakobyan 
# week4 recitation class

#strReplace(’test’, ’t’, ’x’) => 'xesx'


# replace x with y in st.
def strReplace(st, x, y):
	if len(st) < 1:
		return st
	else:
		if st[0] == x:
			return y + strReplace(st[1:],x,y)
		else:
			return st[0] + strReplace(st[1:],x,y)
			
def strReplaceIter(st, x, y):
	result = ""
	for i in range(len(st)):
		if st[i] == x:
			result += y
		else:
			result += st[i]
	return result
			
def main():
	print(strReplaceIter('test', 't', 'x'))

main()