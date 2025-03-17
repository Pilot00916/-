class RomanNums:
    def __init__(self, roman):
        self.roman = roman
        self.arabic = self.from_roman()

    def from_roman(self):
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        integer = 0
        prev_value = 0

        for char in reversed(self.roman):
            value = roman_to_int[char]
            if value < prev_value:
                integer -= value
            else:
                integer += value
            prev_value = value

        return integer

    def is_palindrome(self):
        str_number = str(self.arabic)
        return str_number == str_number[::-1]
