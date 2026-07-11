num = int(input("Enter a number to print its multiplication table: "))   # here we are asking to user which table you want to print.

def which_table(num_table):              # function define as which_table
    for i in range(1, 11):               # loop is used to print the table from 1 to 10
         print(f"{num_table} x {i} = {num_table * i}")   # that print statement.
which_table(num)   # here we are calling the function which_table and passing the user input as an argument.
