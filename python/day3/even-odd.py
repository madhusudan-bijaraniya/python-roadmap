def even_odd(num):
    if num%2==0:
        print(f"{num} is even number")
    else:
        print(f"{num} is odd number")   

num = int(input("Enter a number: "))
even_odd(num)