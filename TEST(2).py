1. # Check whether number is even or odd.(Use ternary operator

n1 = int(input("entered value you want to check is = "))


num = print("the number is even") if (n1 % 2 == 0) else print("the number is odd ")


2# Input: Age of the donor

age = int(input("Enter the age of the donor: "))

if age >= 18 and age <= 55:
        print("The donor is eligible to donate blood.")



3. # Write a program to convert the temperature from Celsius to Fahrenheit and Fahrenheit to Celsius.

celsius=float(input("enter the tempreture of celsius = "))
fahrenheit=(celsius*9/5)+32

print("---- the celsius to fahrenheit is --- :- ",fahrenheit)

fahrenheit=float(input("enter the tempreture of fahrenheit = "))
celsius=((fahrenheit-32)*5)/9

print("---- the fahrenheit to celsius is --- :- ",celsius)


4.# Write a Program to Check Whether a Character is Vowel or consonant

ch=str(input("enter any word to check vowel or consonant :- "))

if (ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' and ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U'):
    print("the entered word is vowel")
else:
    print("the entered word is consonant")


5. # Write a program to make a Simple Calculator to Add, Subtract, Multiply or Divide Using match...case

K = int(input("ENTER THE FIRST VALUE (1) :- "))
A = int(input("ENTER THE SECOND VALUE (2) :- "))


mylist = (K, A)

mylist = int(input("ENTER YOUR CHOISE :- "))

if (mylist == 1 or mylist == 2 or mylist == 3 or mylist == 4 or mylist == 5 or mylist == 6):
    print("THE CHOISE IS = ",mylist)

match mylist:
    case 1:
        print("the addition is = ", K + A)
    case 2:
        print("the substraction is = ", K - A)
    case 3:
        print("the multiplication is = ", K * A)
    case 4:
        print("the division is = ", K / A)
    case 5:
        print("the floor division is = ",K // A)
    case 6:
        print("the multiplication power is = ",K ** A)

6. # Write a program to find the maximum from given four numbers (using logical operator).

A1 = int(input("ENTER VALUE IN A1 :- ")) 
A2 = int(input("ENTER VALUE IN A2 :- ")) 
A3 = int(input("ENTER VALUE IN A3 :- ")) 
A4 = int(input("ENTER VALUE IN A4 :- ")) 


if(A1 > A2 and A1 > A4) :
    print("entered past value of A1 is maximum")  
elif(A2 > A3) :
    print("entered past value of A2 is maximum")  
elif(A3 > A4) :
    print("entered past value of A3 is maximum")  
elif(A4 > A2) :
    print("entered past value of A4 is maximum")  

else :
    print("SORRY! I CAN NOT UNDERSTAND YOUR ENTERED VALUE")

7.# Write a program to find the maximum from given four numbers (using logical operator)

num=int(input("enter the value of num is = "))

if(num<100):
    print("the entered number is less than 100")
    if(num%2==0):
     print("the entered number is even")
    else:
       print("the entered number is odd")
else:
   print("the enteres number is greter than 100")

8.# Take a number. If number is 1 then print Monday, 2 then print Tuesday and so on….(Use elif statement)

tn = int(input("enter the number any one :- "))

if tn == 1:
    print("MONDAY")
else:
    if tn == 2:
        print("TUESDAY")
    else:
        if tn == 3:
            print("WEDNESDAY")
        else:
            if tn == 4:
                print("THURSDAY")
            else:
                if tn == 5:
                    print("FRIDAY")
                else:
                    if tn == 6:
                        print("SATURDAY")
                    else:
                        if tn == 7:
                            print("SUNDAY")
                        else:
                            print("THE NUMBER IS OUT OF READ = ",tn) 

9.# Write a program to swap of two numbers 

N=int(input("enter the value of N = "))
K=int(input("enter the value of K = "))

# thre are two types of swap formula defined below


1.# first formula

'temp=N'
'N=K'
'K=temp'

2.# second formula

N,K = K,N

print("before swapping N is  = ",N)
print("before swapping K is  = ",K) 

10.# 10. Take 2 numbers and find smallest number (USING NOT OPERATOR)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

smallest = num1 if not num1 > num2 else num2

print("The smallest number is:",smallest)
