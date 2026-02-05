var  = int(input("Enter a number: "))


odd_numbers = [num for num in range(1, var + 1) if num % 2 != 0]
print(odd_numbers)

