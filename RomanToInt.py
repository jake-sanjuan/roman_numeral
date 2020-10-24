"""Changes roman numeral into integer"""


class RomanToInt:

    def __init__(self):
        self.roman_numeral = input("Enter a roman numeral here: ")
        self.integer = 0
        self.roman_numeral_list = []
        self.split_numeral()

    def split_numeral(self):
        """Function splits string input into list of letters for
        function nums_for_letters to interpret and add"""
        for letter in self.roman_numeral:
            self.roman_numeral_list.append(letter.upper())

        self.nums_for_letters()

    def nums_for_letters(self):
        """Function takes list of letters input and adds value for each to
        self.integer.  Also handles exceptions and exits program if exception
        happens"""
        try:
            for letter in self.roman_numeral_list:
                if letter == "M":
                    self.integer += 1000
                elif letter == "D":
                    self.integer += 500
                elif letter == "C":
                    self.integer += 100
                elif letter == "L":
                    self.integer += 50
                elif letter == "X":
                    self.integer += 10
                elif letter == "V":
                    self.integer += 5
                elif letter == "I":
                    self.integer += 1
                else:
                    raise TypeError
        except TypeError:
            print("Only letters M, D, C, L, X, V, I are allowed!")
            exit(1)

    def __repr__(self):
        return "Your roman numeral converted is %d" % self.integer


if __name__ == '__main__':
    while True:
        one = RomanToInt()
        print(one)
        y_or_n = input("Do you want to input another number? y / n \n").lower()
        if y_or_n == 'n':
            break
