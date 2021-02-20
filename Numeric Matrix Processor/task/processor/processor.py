def input_matrix() -> list:
    n, m = [int(x) for x in input().split()]
    matrix = []
    for i in range(n):
        vector = [int(x) for x in input().split()]
        if len(vector) != m:
            print(f"Wrong count of numbers in row: {len(vector)}\n must be: {m}")
            exit()
        matrix.append(vector)
    return matrix


# Stage 1
def sum_matrix(a, b):
    if type(a) is list and type(b) is list \
            and type(a[0]) is list and type(b[0]) is list \
            and len(a) == len(b) and len(a[0]) == len(b[0]):
        return [[x + y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(a, b)]
    else:
        print("ERROR")
        exit()


# Stage 2
def mult_by_const(a, c):
    if type(a) is list and type(a[0]) is list:
        return [[x * c for x in row_a] for row_a in a]
    else:
        print("ERROR")
        exit()


def print_matrix(a):
    if type(a) is list and type(a[0]) is list:
        for r in a:
            print(*r)


# stage 3
class MatrixProcessor:

    def show_menu(self):
        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("0. Exit")
        return input("Your choice: ")

    def show_transpose_menu(self):
        print("\n1. Main diagonal")
        print("2. Side diagonal")
        print("3. Vertical line")
        print("4. Horizontal line")
        return input("Your choice: ")

    def get_matrix(self, matrix_name=""):
        n, m = [int(x) for x in input(f"Enter size of{' ' + matrix_name} matrix: ").split()]
        return [[float(x) if x.count(".") else int(x) for x in input().split()] for _ in range(n)]

    def sum_matrix(self, a, b):
        if type(a) is list and type(b) is list \
                and type(a[0]) is list and type(b[0]) is list \
                and len(a) == len(b) and len(a[0]) == len(b[0]):
            return [[x + y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(a, b)]
        else:
            return None

    def multiply_by_const(self, a, c):
        if type(a) is list and type(a[0]) is list:
            return [[x * c for x in row_a] for row_a in a]
        else:
            return None

    def multiply_by_matrix(self, a, b):
        if type(a) is list and type(b) is list \
                and type(a[0]) is list and type(b[0]) is list \
                and len(a[0]) == len(b):
            return [[sum(cell_a * row_b[j] for cell_a, row_b in zip(row_a, b))
                     for j in range(len(b[0]))] for row_a in a]
        else:
            return None

    def trans_by_main(self, a):
        if type(a) is list and type(a[0]) is list:
            return [[row_a[j] for row_a in a] for j in range(len(a[0]))]
        else:
            return None

    def trans_by_side(self, a):
        if type(a) is list and type(a[0]) is list:
            reversed_a = list(reversed(a))
            return [[row_a[-j] for row_a in reversed_a] for j in range(1, len(a[0]) + 1)]
        else:
            return None

    def trans_by_vertical(self, a):
        if type(a) is list and type(a[0]) is list:
            return [list(reversed(row_a)) for row_a in a]
        else:
            return None

    def trans_by_horizontal(self, a):
        if type(a) is list and type(a[0]) is list:
            return list(reversed(a))
        else:
            return None

    def get_matrix_determinant(self, a):
        if len(a) == 1:
            return a[0][0]
        elif len(a) == 2:
            return a[0][0] * a[1][1] - a[0][1] * a[1][0]
        else:
            det, i = 0, 0
            for j in range(len(a)):
                submatrix = [[el for m, el in enumerate(row_a) if m != j] for k, row_a in enumerate(a) if k != i]
                det += (-1) ** (i + j) * a[i][j] * self.get_matrix_determinant(submatrix)

            return det

    def process_matrix_sum(self):
        a = self.get_matrix("first")
        b = self.get_matrix("second")
        res = self.sum_matrix(a, b)
        if res:
            print("The result is:")
            print_matrix(res)
            print()
        else:
            print("The operation cannot be performed.\n")

    def process_matrix_by_const(self):
        a = self.get_matrix()
        const = input("Enter constant: ")
        if const.count("."):
            const = float(const)
        else:
            const = int(const)

        res = self.multiply_by_const(a, const)
        if res:
            print("The result is:")
            print_matrix(res)
            print()
        else:
            print("The operation cannot be performed.\n")

    def process_matrix_by_matrix(self):
        a = self.get_matrix("first")
        b = self.get_matrix("second")

        res = self.multiply_by_matrix(a, b)
        if res:
            print("The result is:")
            print_matrix(res)
            print()
        else:
            print("The operation cannot be performed.\n")

    def process_transpose(self, act):
        a = self.get_matrix()

        if act == "1":
            res = self.trans_by_main(a)
        elif act == "2":
            res = self.trans_by_side(a)
        elif act == "3":
            res = self.trans_by_vertical(a)
        elif act == "4":
            res = self.trans_by_horizontal(a)
        else:
            res = None

        print("The result is:")
        print_matrix(res)
        print()

    def process_find_determinant(self):
        a = self.get_matrix()
        determinant = self.get_matrix_determinant(a)
        print(f"The result is:\n{determinant}\n")

    def run(self):
        while True:
            act = self.show_menu()
            if act == "1":
                self.process_matrix_sum()
            elif act == "2":
                self.process_matrix_by_const()
            elif act == "3":
                self.process_matrix_by_matrix()
            elif act == "4":
                act = self.show_transpose_menu()
                self.process_transpose(act)
            elif act == "5":
                self.process_find_determinant()
            elif act == "0":
                break


mp = MatrixProcessor()
mp.run()

# A = input_matrix()
# B = input_matrix()
# const = int(input())

# print_matrix(sum_matrix(A, B))
# print_matrix(mult_by_const(A, const))
