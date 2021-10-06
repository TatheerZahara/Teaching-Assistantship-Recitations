                                         #EXAMPLE 1

# Check if a number is a perfect power of another number. For example, is 125 a perfect power of 5 because 5^3=125. Another example would be 243 being a perfect power of 3

num=int(input("Enter your nunber: "))
base=int(input("Enter the base:"))

while num%base==0:   #125%5=0 ----> 25%5=0---->5%5==0 
  num=num/base

if num==1:
  print("It is a perfect power of", base)
else:
    print("It is not a perfect power of", base)
    
    
                                             #EXAMPLE 2


#This program is an extension of the above one. Here we ask the user to enter a number and check if the entered number is a perfect power of any number in the number set
num=int(input("Enter your number:"))  
base= 2

while base < num**(1/2) :   #This loop would run from 2 to the square root of num 

  num2=num   #Copying num to a new variable so that my loops don't change the value of original number 

  while num2%base==0:  #Inner Loop 125%5==0 25%5==0 etc 
    num2=num2/base      
    #Inner loop ends 
  #Back in outer loop 
  if num2==1:
    print("It is a perfect power of", base)
    base=num #Changing the value of base to num just to escape out of the loop 
  else: 
    base+=1 #Normal loop increment (Outer loop) 
    
    
                                 
                                                  #EXAMPLE  3

    
    

#Fibonnaci Series 

#0, 1, 1, 2, 3, 5, 8, 13, 

num1=0
num2=1 

cond=int(input("Enter how many numbers you want from the series"))
print(num1, end=",") #Just printing out first number
print(num2, end=",")  #Printing second number 

i=0 #loop conditional variable 
sum=0 #variable for addition 

while i < cond-2: #cond-2 because we have already entered first two values 
  sum=num1+num2 
  print(sum, end=",") 

  num1=num2 
  num2=sum 

  i+=1 #loop variables





                                                #Example 4

# Find a missing number from a range entered by the user. First ask the user to enter a ranger. After this ask the user to enter [range-1] numbers. Our program should be able to find the missing number from the range 
first=int(input("Enter first number of your range"))
last=int(input("Enter last number of your range"))


#Find the sum of numbers in the range. FOr example, in case of 1 to 4, our sum would be 1+2+3+4=10 

sum=0
while first<=last: 
  sum=sum+first
  first+=1

#End of sum 
i=0
sum2=0 #Sum of the values entered by the user
while(i<last-1):
  num=int(input("Enter a number in your range"))
  sum2=sum2+num #actually finding the sum here 
  i+=1

missing= int(sum-sum2)
print("Your missing number is",missing)
