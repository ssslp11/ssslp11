def fact(n):
 fac = 1
 if(n>=1):
  for i in range(1,n+1):
    fac = fac*i
 elif(n==0):
    fac = 1
 else:
    print("Enter a valid number")
    
num = int(input("Enter a number: "))
print("The factorial of" ,num, "is" ,fact(num),) 


     
   
 
