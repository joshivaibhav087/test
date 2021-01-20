a=int(input("enter a:"))
fact=1
if(a<0):
    print("invalid input")
elif(a==0):
    print("1")
else:
    for i in range (1,a+1):
        fact=fact*i
    print(fact)
      
