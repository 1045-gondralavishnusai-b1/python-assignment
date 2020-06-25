def maxoftwo(a,b):
	if(a>b):
		return a
	return b
def maxofthree(a,b,c):
	return maxoftwo(a,maxoftwo(b,c))
a=int(input('enter a value\n'))
b=int(input('enter b value\n'))
c=int(input('enter c value\n'))
print('max of3 numbers is')
print(maxofthree(a,b,c))