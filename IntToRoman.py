"""Class converts integer to roman numeral"""


class IntToRoman:
    def __init__(self):
        self.integer = int(input("Enter integer here: "))
        self.roman_numeral = []
        self.check_thousands()

    def check_thousands(self):
        if self.integer / 1000 != 0:
            number_m = int(self.integer / 1000)
            self.integer -= number_m * 1000
            for letter in range(number_m):
                self.roman_numeral.append("M")

        self.check_five_hundred()

    def check_five_hundred(self):
        if self.integer / 500 != 0:
            number_d = int(self.integer / 500)
            self.integer -= number_d * 500
            for letter in range(number_d):
                self.roman_numeral.append("D")

        self.check_hundreds()

    def check_hundreds(self):
        if self.integer / 100 != 0:
            number_c = int(self.integer / 100)
            self.integer -= number_c * 100
            for letter in range(number_c):
                self.roman_numeral.append("C")

        self.check_fifties()

    def check_fifties(self):
        if self.integer / 50 != 0:
            number_l = int(self.integer / 50)
            self.integer -= number_l * 50
            for letter in range(number_l):
                self.roman_numeral.append("L")

        self.check_tens()

    def check_tens(self):
        if self.integer / 10 != 0:
            number_x = int(self.integer / 10)
            self.integer -= number_x * 10
            for letter in range(number_x):
                self.roman_numeral.append("X")

        self.check_fives()

    def check_fives(self):
        if self.integer / 5 != 0:
            number_v = int(self.integer / 5)
            self.integer -= number_v * 5
            for letter in range(number_v):
                self.roman_numeral.append("V")

        self.check_ones()

    def check_ones(self):
        if self.integer / 1 != 0:
            number_i = int(self.integer / 1)
            for letter in range(number_i):
                self.roman_numeral.append("I")

    def __repr__(self):
        roman_str = "".join(self.roman_numeral)
        return "Your roman numeral is " + roman_str


if __name__ == '__main__':
    IntToRoman()
