number = int(input("Please Enter any Number: "))
if(number==0):
    try:
        print("invalid number")
        
    finally:
        print("final block stmt executed")
else:   
    reverse = 0
    temp = number

    while(temp > 0):
        Reminder = temp % 10
        reverse = (reverse * 10) + Reminder
        temp = temp //10
 
    print("Reverse of a Given number is = %d" %reverse)

    if(number == reverse):
        print("%d is a Palindrome Number" %number)
    else:
        print("%d is not a Palindrome Number" %number)