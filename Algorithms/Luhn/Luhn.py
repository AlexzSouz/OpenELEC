import sys

class Luhn:
    def DigitsOf(self, number):
        return [int(i) for i in str(number)]

    def CheckSum(self, card_number):
        digits = self.DigitsOf(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        total = sum(odd_digits[1:])
        for digit in even_digits:
            total += sum(self.DigitsOf(2 * digit))
        return total % 10

    def IsValidLuhn(self, card_number):
        return self.CheckSum(card_number) == 0

    def CalculateLuhn(self, partial_card_number): 
        check_digit = self.CheckSum(int(partial_card_number) * 10)
        return check_digit if check_digit == 0 else 10 - check_digit

luhn = Luhn()
print(sys.argv[1])
print(luhn.IsValidLuhn(sys.argv[1]))
print(luhn.CalculateLuhn(sys.argv[1]))

'''
# If the (sum mod 10) == 0, then the check digit is 0
# Else, the check digit = 10 - (sum mod 10)
# Append a zero check digit to the partial number and calculate checksum
'''