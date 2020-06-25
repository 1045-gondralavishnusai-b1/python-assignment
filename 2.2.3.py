def prime(a):
	if(a>1):
		for i in range(2,a):
			if(a%i)==0 :
				print("not a prime number")
				break
			else:
				print(' prime number')
	else:
		print(a,'isnot a prime number')
a=int(input('enter a number'))
prime(a)
