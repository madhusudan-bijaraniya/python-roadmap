
# operators are used to perform operations on variables and values
# arithmetic operators  :- +,-,*,/,%,**,//
#logical operators :- and, or, not
#assignment operators :- =, +=, -=, *=, /=, %=, **=, //=
#comparison operators :- ==, !=, >, <, >=, <=
#bitwise operators :- &, |, ^, ~, <<, >>

#lets see some examples of operators in python

#addition
a = 10
b = 20
print("a + b = ", a + b)

#table of 5
for i in range(1, 11):
    print("5 *", i, "=", 5 * i)


#comparison operators
x = 5
y = 10
print("x == y :", x == y)
print("x != y :", x != y)
print("x > y :", x > y)
print("x < y :", x < y)
print("x >= y :", x >= y)
print("x <= y :", x <= y)
print(type(x), type(y))

#here x and y are integers, we can change into float and check the type
x = float(x)
y = float(y)    
print(type(x), type(y))

#x and y are now float 
 

#swapping of two numbers
x = 5
y = 10
print("Before swapping: x =", x, "y =", y)  
c = x
x = y
y = c
print("After swapping: x =", x, "y =", y)


#   Fahrenheit=(Celsius×59​)+32
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit) 
