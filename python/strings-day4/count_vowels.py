name = input("Enter your name: ")
cout = 0
for char in name:
    if char in 'aeiouAEIOU':
        cout += 1
print("Number of vowels in your name:", cout)