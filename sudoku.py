import random

class Model:
    def __init__(self):
        self.quiz = ''
        self.current = ''
        self.solution = ''

    def load_quiz(self):
        pos = random.randint(0, 1000001)
        with open("sudoku.csv", 'r') as data:
            for r in range(0, 1000001):
                row = data.readline()
                if r == pos:
                    tokens = row.split(',')
                    self.quiz = tokens[0]
                    self.current = tokens[0]
                    self.solution = tokens[1]
                    print(tokens[0])
                    print(tokens[1])
                    break

    def play(self, row, col, value):
        try:
            irow = int(row)
            icol = int(col)
            pos = (irow-1)*9 + (icol-1)
            if self.quiz[pos] != '0':
                return "Cannot change this pos"
            self.current = self.current[:pos] + value + self.current[pos+1:]
            if self.solution[pos] == value:
                return ""
            else:
                return "Wrong value " + value
        except ValueError:
            return "Values must be numbers"

    def solved(self):
        return self.current == self.solution



class View:
    def __init__(self):
        self.error = ''

    def display_board(self, current):
        if self.error != '':
            print("ERROR: " + self.error)
        print('   1 2 3   4 5 6   7 8 9')
        print('   - - -   - - -   - - -')
        for i in range(0,81):
            if i % 9 == 0:
                if i > 0:
                    print()
                    if i % 27 == 0:
                        print()
                print(str(i//9+1) + '|', end=' ')
            elif i % 3 == 0 or i % 6 == 0:
                print(' ', end=' ')
            print(current[i], end=' ')
        print()

    def play(self):
        row = input('Row: ')
        col = input('Col: ')
        value = input('Value: ')
        return row, col, value






