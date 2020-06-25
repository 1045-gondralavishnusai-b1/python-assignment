a=int(input('enter a value\n'))
b=int(input('enter b value\n'))
c=int(input('enter c value\n'))
if((a==b)and(b==c)and(c==a)):
	print('all are equal')
elif((a==b)or(b==c)or(c==a)):
	print( ' only 2 are equal')
else:
	print('noy equal')

	