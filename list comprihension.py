var  = int(input("Enter a number: "))

#create a list with all the odd numbers from 1 to var
odd_numbers = [num for num in range(1, var + 1) if num % 2 != 0]
print(odd_numbers)

