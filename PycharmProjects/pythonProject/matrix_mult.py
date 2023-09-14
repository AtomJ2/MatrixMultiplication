import argparse

parser = argparse.ArgumentParser()
parser.add_argument('path_input', type=str, help='Path to matrix')
parser.add_argument('path_output', type=str, help='Path to output')
args = parser.parse_args()
input_file = open(args.path_input, 'r')
output_file = open(args.path_output, 'w')


def parse():
    """Parsing file"""
    string0 = input_file.readline()
    string0 = string0.replace('\n', '')
    lst = string0.split(' ')
    m = len(lst)
    n = 1
    string0 = input_file.readline()
    while not string0.startswith('\n'):
        string0 = string0.replace('\n', '')
        n += 1
        lst.extend(string0.split(' '))
        string0 = input_file.readline()
    return lst, n, m


def create_matrix(n, m):
    """Creating matrix"""
    return [[0 for _ in range(m)] for _ in range(n)]


def convert(n, m, lst):
    """Converting matrix from list to integer array"""
    matrix = create_matrix(n, m)
    for q in range(n):
        for w in range(m):
            matrix[q][w] = int(lst[q * m + w])
    print('converted matrix:\n', matrix)
    return matrix


def mult_matrix(n, m, k, matrix_1, matrix_2):
    """Matrices multiplication"""
    res = create_matrix(n, m)
    for i in range(n):
        for j in range(m):
            for k in range(k):
                res[i][j] += matrix_1[i][k] * matrix_2[k][j]
    print('res:\n', res)
    return res


lst1, n1, m1 = parse()
lst2, m2, n2 = parse()

matrix1 = convert(n1, m1, lst1)
matrix2 = convert(m1, n2, lst2)

res_matrix = mult_matrix(n1, n2, m1, matrix1, matrix2)
