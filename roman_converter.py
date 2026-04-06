class RomanConverter:
    def int_to_roman(self, num):
        # Mapping standard values and special cases (like 4 and 9)
        val_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        roman_numeral = ''
        for value, symbol in val_map:
            # Check how many times the value fits into the number
            while num >= value:
                roman_numeral += symbol
                num -= value
        return roman_numeral

# Creating the object and taking user input
converter = RomanConverter()
number = int(input("Enter an integer: "))

print(f"The Roman value is: {converter.int_to_roman(number)}")
