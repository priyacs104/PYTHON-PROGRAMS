name = "Priya"
age = 22
college = "BON SECOURS ARTS AND SCIENCE COLLEGE"

print("Name:", name)
print("Age:", age)
print("College:", college)



name = input("Enter your name: ")
print("Hello,", name)



a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum =", a + b)



celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Fahrenheit =", fahrenheit)




p = float(input("Enter Principal Amount: "))
r = float(input("Enter Rate of Interest: "))
t = float(input("Enter Time (years): "))

si = (p * r * t) / 100

print("Simple Interest =", si)




a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swapping:")
print("a =", a)
print("b =", b)

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)
