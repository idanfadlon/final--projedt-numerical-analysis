import sympy as sp
from datetime import *

x = sp.symbols('x')


def calc_av(A, b):
    inverseMat = inverse(A)
    av = mul_matrix_wVector(inverseMat, b)
    return av


def identity_matrix(size):
    I = list(range(size))
    for i in range(size):
        I[i] = list(range(size))
        for j in range(size):
            if i == j:
                I[i][j] = 1
            else:
                I[i][j] = 0
    return I


def mul_matrix(m1, m2):
    len_m1 = len(m1)
    cols_m1 = len(m1[0])
    rows_m2 = len(m2)
    if cols_m1 != rows_m2:  # Checks if it is valid to multiply between matrix
        print("Cannot multiply between matrix (incorrect size)")
        return
    new_mat = list(range(len_m1))
    val = 0
    for i in range(len_m1):
        new_mat[i] = list(range(rows_m2))
        for j in range(len(m2[0])):
            for k in range(cols_m1):
                val += m1[i][k] * m2[k][j]
            new_mat[i][j] = val
            val = 0
    return new_mat


def inverse(mat):
    size = len(mat)
    invert_mat = identity_matrix(size)
    for col in range(size):
        elem_mat = identity_matrix(size)
        max_row = max_val_index(mat, col)  # Returns the index of the row with the maximum value in the column
        invert_mat = mul_matrix(eMatForSwap(size, col, max_row), invert_mat)  # Elementary matrix for swap rows
        mat = mul_matrix(eMatForSwap(size, col, max_row), mat)  # swap between rows in case the pivot is 0
        pivot = mat[col][col]
        for row in range(size):
            if row != col and mat[row][col] != 0:
                elem_mat[row][col] = (-1) * (mat[row][col] / pivot)
        mat = mul_matrix(elem_mat, mat)
        invert_mat = mul_matrix(elem_mat, invert_mat)
    # check diagonal numbers
    for i in range(size):
        pivot = mat[i][i]
        if pivot != 1:
            for col in range(size):
                invert_mat[i][col] /= float(pivot)
            mat[i][i] = 1
    return invert_mat


def mul_matrix_wVector(m, v):
    len_m = len(m)
    cols_m = len(m[0])
    rows_v = len(v)
    if cols_m != rows_v:  # Checks if it is valid to multiply between matrix
        print("Cannot multiply between matrix (incorrect size)")
        return
    new_mat = list(range(len_m))
    val = 0
    for i in range(len_m):
        for k in range(len(m[0])):
            val += m[i][k] * v[k]
        new_mat[i] = val
        val = 0
    return new_mat


def max_val_index(mat, col):
    max = abs(mat[col][col])
    index = col
    for row in range(col, len(mat)):
        if abs(mat[row][col]) > max:
            max = abs(mat[row][col])
            index = row
    return index


def eMatForSwap(size, index1, index2):
    mat = identity_matrix(size)
    # swap rows
    tmp = mat[index1]
    mat[index1] = mat[index2]
    mat[index2] = tmp
    return mat


def polynomial_interpolation(pointlist, xf):
    n = len(pointlist)
    A = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            A[i][j] = pointlist[i][0] ** j
    b = [0 for i in range(n)]
    for i in range(n):
        b[i] = pointlist[i][1]
    a = calc_av(A, b)
    p = 0
    pstr = "p{0}(x) = ".format(n - 1)
    for i in range(n):
        p = p + a[i] * xf ** i
        if i is 0:
            pstr += "{:.5}x**{} ".format(a[i], i)
        if a[i] > 0:
            pstr += "+{:.5}x**{} ".format(a[i], i)
        else:
            pstr += "{:.5}x**{} ".format(a[i], i)
        print("p{}({}) = {:.5}".format(i, xf, p))
    pstr.replace(" ", "+")
    print(pstr)
    print("p{0}({1}) = {2}".format(n - 1, xf, p))
    return p


def neville_interpolation(pointlist, xf):
    n = len(pointlist)
    p = n * [0]
    for k in range(n):
        iteration = k
        for i in range(n - k):
            if k == 0:
                p[i] = pointlist[i][1]
            else:
                p[i] = ((xf - pointlist[i + k][0]) * p[i] + (pointlist[i][0] - xf) * p[i + 1]) / (
                        pointlist[i][0] - pointlist[i + k][0])
                print(f'p {i}, {iteration} = {p[i]:.5f}')
                iteration += 1
        if k + 1 != n:
            print('\n=====================Iteration ' + str(k + 1) + ' ==============================')
    print('\nF( ' + str(xf) + ') = ', end='')
    return p[0]


def main35():
    inter_t = [[1.2, 3.5095], [1.3, 3.6984], [1.4, 3.9043], [1.5, 4.1293], [1.6, 4.3756]]
    xf = 1.37
    fx = polynomial_interpolation(inter_t, xf)
    now = datetime.now()
    str = '{0}{1}{2}'.format(now.day, now.hour, now.minute)
    print("The close value of the point {0} by polynomial interpolation method is : {1:.5}00000{2}".format(xf, fx, str))
    fx = neville_interpolation(inter_t, xf)
    print("The close value of the point {0} by neville interpolation method is : {1:.5}00000{2}".format(xf, fx, str))


main35()
