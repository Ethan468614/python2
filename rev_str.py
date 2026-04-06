class Reverse:
    # Constructor with a default value for s
    def __init__(self, s=""):
        self.s = s

    # Method to return the reversed string
    def reverse_string(self):
        # [::-1] is the most efficient way to reverse a string in Python
        return self.s[::-1]

# Taking input from the user
user_input = input("Enter a word: ")

# Creating an instance of the class with the user's input
obj = Reverse(user_input)

# Printing the result
print(f"Reversed string: {obj.reverse_string()}")
