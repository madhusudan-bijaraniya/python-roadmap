name = input("Enter your name: ")
rev_name = name[::-1]
if name == rev_name:
    print("Your name is a palindrome")
else:
    print("Your name is not a palindrome")