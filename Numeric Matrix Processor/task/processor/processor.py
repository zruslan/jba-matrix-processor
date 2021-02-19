def input_matrix() -> list:
    n, m = [int(x) for x in input().split()]
    matrix = []
    for i in range(n):
        vector = [int(x) for x in input().split()]
        if len(vector) != m:
            print(f"Wrong count of numbers in row: {len(vector)}\n must be: {m}")
        matrix.append(vector)
    return matrix


def sum_matrix(a, b):
    if type(a) is list and type(b) is list \
            and type(a[0]) is list and type(b[0]) is list \
            and len(a) == len(b) and len(a[0]) == len(b[0]):
        return [[x + y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(a, b)]
    else:
        print("ERROR")


def print_matrix(a):
    if type(a) is list and type(a[0]) is list:
        for r in a:
            print(*r)


A = input_matrix()
B = input_matrix()

print_matrix(sum_matrix(A, B))
