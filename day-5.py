#print 1 to 10

for i in range(91,11):
    print(i)



#print 10to 1

for i in range(10,0,-1):
    print(i)


#print even numbers 1 to 20

for i in range(1,20):
    if i%2==0:
        print(i)


#print odd numbers(1 to 20)


for i in range(1,21):
    if i%2!=0:
        print(i)


#multiplication table

num=int(input("Enter anumber:"))

for i in range(1,11):
    print(num,"x",i,"=",num*i)


#sum of 1 to n

n=int(input("Entera number:"))

total=0

for i in range(1,n+1):
    total=total+i

print("sum=",total)


#factorial

n=int(input("Enter a number:"))

fact=1

for i in range(1,n+1):
      fact=fact*1

print("Factorial=",fact)


#count digits

num=int(input("Enter a number:"))

count=0

while num>0:
    num=num//10
    count+=1

print("Digits=",count)


#reverse a number

num=int(input("Enter a number:"))

reverse=0

while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10

print("Reverse=",reverse)


#prime number

num=int(input("Enter a number:"))

count=0

for i in range(1,num+1):
    if num%i==0:
        count+=1

if count==2:
    print("Prime Number")
else:
    print("Not a Prime Number")



    

    
