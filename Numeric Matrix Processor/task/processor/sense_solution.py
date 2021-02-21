from fractions import Fraction


class Matrix:
    def __init__(self, number_of_rows, number_of_columns):
        self.number_of_rows = int(number_of_rows)
        self.number_of_columns = int(number_of_columns)
        self.table = None
        self.determinant = None

    def __add__(self, other):
        if not (type(other) == type(self) and
                (self.number_of_rows == other.number_of_rows and self.number_of_columns == other.number_of_columns)):
            return None

        new_matrix = Matrix(self.number_of_rows, self.number_of_columns)
        new_matrix.table = [[self.table[i][j] + other.table[i][j] for j in range(self.number_of_columns)]
                            for i in range(self.number_of_rows)]
        return new_matrix

    def __mul__(self, other):
        matrix = None
        if isinstance(other, int) or isinstance(other, float) or isinstance(other, Fraction):
            matrix = Matrix(self.number_of_rows, self.number_of_columns)
            matrix.table = [[self.table[i][j] * other for j in range(self.number_of_columns)]
                            for i in range(self.number_of_rows)]
        if isinstance(other, Matrix):
            if not self.number_of_columns == other.number_of_rows:
                return None
            matrix = Matrix(self.number_of_rows, other.number_of_columns)
            matrix.table = []
            for n in range(self.number_of_rows):
                matrix.table.append([])
                for m in range(other.number_of_columns):
                    matrix.table[n].append(sum(self.table[n][i] * other.table[i][m]
                                               for i in range(self.number_of_columns)))

        return matrix

    def __str__(self):
        max_len_column = [max(len(str(self.table[i][j])) for i in range(self.number_of_rows))
                          for j in range(self.number_of_columns)]
        column_splitter = ' '
        s = ''
        for i in range(self.number_of_rows):
            for j in range(self.number_of_columns):
                s += str(self.table[i][j]).rjust(max_len_column[j]) + column_splitter
            s = s[:-len(column_splitter)] + '\n'
        return s

    def get_determinant(self):
        if self.determinant is None:
            self.determinant = Matrix.calculate_determinant(self.table)
        return self.determinant

    @staticmethod
    def calculate_determinant(table):
        if not table:
            return None
        if not len(table) == len(table[0]):
            return None
        if len(table) == 1:
            return table[0][0]
        i = 0
        return sum(table[i][j] * Matrix.get_cofactor(table, i, j) for j in range(len(table)))

    @staticmethod
    def get_cofactor(table, i, j):
        return -Matrix.get_minor(table, i, j) if (i + j) % 2 else Matrix.get_minor(table, i, j)

    @staticmethod
    def get_minor(table, i, j):
        if len(table) == 0:
            return None
        if len(table) == 1:
            return table[0][0]
        new_table = [[table[i_][j_] for j_ in range(len(table[i_])) if not j_ == j]
                     for i_ in range(len(table)) if not i_ == i]
        return Matrix.calculate_determinant(new_table)

    def inverse_matrix(self):
        det = self.get_determinant()
        if not det:
            return None
        C = Matrix(self.number_of_rows, self.number_of_columns)
        C.table = [[Matrix.get_cofactor(self.table, i, j) for j in range(self.number_of_columns)]
                   for i in range(self.number_of_rows)]
        C = C.transpose_main_diagonal()
        return C * (1 / det)

    def read(self):
        self.table = [[float(x) if x.count('.') else int(x) for x in input().split()[:self.number_of_columns]]
                      for _i in range(self.number_of_rows)]

    def transpose_horizontal_line(self):
        matrix = Matrix(self.number_of_rows, self.number_of_columns)
        matrix.table = [self.table[-i] for i in range(1, self.number_of_rows + 1)]
        return matrix

    def transpose_main_diagonal(self):
        matrix = Matrix(self.number_of_columns, self.number_of_rows)
        matrix.table = [[self.table[m][n] for m in range(self.number_of_rows)] for n in range(self.number_of_columns)]
        return matrix

    def transpose_vertical_line(self):
        matrix = Matrix(self.number_of_rows, self.number_of_columns)
        matrix.table = [[row[-i] for i in range(1, len(row) + 1)] for row in self.table]
        return matrix

    def transpose_side_diagonal(self):
        matrix = Matrix(self.number_of_columns, self.number_of_rows)
        matrix.table = [[self.table[-m][-n] for m in range(1, self.number_of_rows + 1)]
                        for n in range(1, self.number_of_columns + 1)]
        return matrix


class Menu:
    def __init__(self):

        main_menu = {
            '1': ['\n1. Add matrices', self.add_matrices],
            '2': ['2. Multiply matrix by a constant', self.multiply_matrix_by_constant],
            '3': ['3. Multiply matrices', self.multiply_matrices],
            '4': ['4. Transpose matrix', self.print_transpose_matrix_menu],
            '5': ['5. Calculate a determinant', self.calculate_determinant],
            '6': ['6. Inverse matrix', self.inverse_matrix],
            '0': ['0. Exit', None],
        }

        transpose_matrix_menu = {
            '1': ['\n1. Main diagonal', self.transpose_main_diagonal],
            '2': ['2. Side diagonal', self.transpose_side_diagonal],
            '3': ['3. Vertical line', self.transpose_vertical_line],
            '4': ['4. Horizontal line', self.transpose_horizontal_line],
            '0': ['0. Exit', None],
        }

        self.menu = (main_menu, transpose_matrix_menu)
        self.current_menu = self.menu[0]

    @staticmethod
    def add_matrices():
        first_matrix = Menu.create_matrix('first')
        second_matrix = Menu.create_matrix('second')
        Menu.print_result(result=first_matrix + second_matrix)

    @staticmethod
    def calculate_determinant():
        matrix = Menu.create_matrix()
        Menu.print_result(result=matrix.get_determinant())

    @staticmethod
    def create_matrix(number=''):
        dimensions = input(f'Enter size of {number}{" " if number else ""}matrix: > ').split()
        matrix = Matrix(dimensions[0], dimensions[1])
        print(f'Enter {number}{" " if number else ""}matrix:')
        matrix.read()
        return matrix

    @staticmethod
    def inverse_matrix():
        matrix = Menu.create_matrix()
        Menu.print_result(err_message="This matrix doesn't have an inverse.", result=matrix.inverse_matrix())

    @staticmethod
    def multiply_matrices():
        first_matrix = Menu.create_matrix('first')
        second_matrix = Menu.create_matrix('second')
        Menu.print_result(result=first_matrix * second_matrix)

    @staticmethod
    def multiply_matrix_by_constant():
        matrix = Menu.create_matrix()
        const = input('Enter constant: > ')
        const = float(const) if const.count('.') else int(const)
        Menu.print_result(result=matrix * const)

    def print_current_menu(self):
        menu = tuple(self.current_menu.values())
        for item in menu:
            print(item[0])
        return input('Your choice: > ')

    @staticmethod
    def print_result(err_message='The operation cannot be performed.', result=None):
        print(err_message if result is None else f'The result is:\n{result}')

    def print_transpose_matrix_menu(self):
        self.current_menu = self.menu[1]

    def run(self):
        answer = self.print_current_menu()
        while not answer == '0':
            item = self.current_menu.get(answer, None)
            if item is None:
                print('There is no such item\n')
                answer = self.print_current_menu()
                continue
            function = item[1]
            function()
            answer = self.print_current_menu()

    def transpose_matrix(function):
        def wrapper(self):
            matrix = Menu.create_matrix()
            Menu.print_result(result=function(self, matrix))
            self.current_menu = self.menu[0]

        return wrapper

    @transpose_matrix
    def transpose_horizontal_line(self, matrix):
        return matrix.transpose_horizontal_line()

    @transpose_matrix
    def transpose_main_diagonal(self, matrix):
        return matrix.transpose_main_diagonal()

    @transpose_matrix
    def transpose_vertical_line(self, matrix):
        return matrix.transpose_vertical_line()

    @transpose_matrix
    def transpose_side_diagonal(self, matrix):
        return matrix.transpose_side_diagonal()


Menu().run()
