import TableIt
from datetime import *


# create Identity matrix
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


# Returns Matrix - The result of multiplying two matrices
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


# Returns the result matrix of  matrix *  vector
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


# returns thr inverse matrix
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


# return element matrix for swap between row index1 to row in index2
def eMatForSwap(size, index1, index2):
    mat = identity_matrix(size)
    # swap rows
    tmp = mat[index1]
    mat[index1] = mat[index2]
    mat[index2] = tmp
    return mat


#  Calculates the "L" matrix and the "U" matrix
def LU(mat):
    size = len(mat)
    invert_mat = identity_matrix(len(mat))
    L = identity_matrix(size)
    for col in range(size):
        elem_mat = identity_matrix(size)
        if mat[col][col] == 0:  # Checks if there is zero on the diagonal
            max_row = max_val_index(mat, col)  # Returns the index of the row with the maximum value in the column
            invert_mat = mul_matrix(eMatForSwap(size, col, max_row), invert_mat)  # Elementary matrix for swap rows
            mat = mul_matrix(eMatForSwap(size, col, max_row), mat)  # swap between rows in case the pivot is
        pivot = mat[col][col]
        for row in range(col+1, size):
            if mat[row][col] != 0:
                elem_mat[row][col] = mat[row][col] / pivot * -1  # Calculate the appropriate elementary matrix
                L[row][col] = (mat[row][col] / pivot * -1)*-1

        mat = mul_matrix(elem_mat, mat)

    return L, mat


# returns the result of Ax=b
def LU_driver(L, U, b):
    L_inverse = inverse(L)
    print("L inverse: \n", L_inverse)
    U_inverse = inverse(U)
    print("U inverse: \n", U_inverse)
    y = mul_matrix_wVector(L_inverse, b)
    print("y = L^-1 * b :\n", y)
    x = mul_matrix_wVector(U_inverse, y)
    print("y * U^-1 : \n ", x)
    return x


def check_Dominant_diagonal(A):
    # checking if given matrix has dominant row
    mat_len = len(A)
    rowSum = 0
    for row in range(mat_len):
        for col in range(mat_len):
            if row != col:
                rowSum += abs(A[row][col])
        if abs(A[row][row]) < rowSum:
            return False
        rowSum = 0
    return True


def xchngRows(matrix, col, maxrow):
    # replace rows in matrix
    tempr = matrix[col]
    matrix[col] = matrix[maxrow]
    matrix[maxrow] = tempr


def org_pivot(matrix, B):
    #  organize to prevent instability
    size = len(matrix)
    for col in range(size):
        maxRow = max_val_index(matrix, col)
        if maxRow > col:
            xchngRows(matrix, col, maxRow)
            xchngRows(B, col, maxRow)


# Returns the row index with the maximum value
def max_val_index(mat, col):
    maxVal = abs(mat[col][col])
    index = col
    for row in range(col, len(mat)):
        if abs(mat[row][col]) > maxVal:
            maxVal = abs(mat[row][col])
            index = row
    return index


def simple_gaussian_seidel_method(A, b,xr):
    """
        Guassian-seidel iterative method will iterate over each row in the matrix
        and will calculate it's variables to provide a new solution.
        It will use the next solution of any non 0 variable from that row.
        Will deliver the result with less iterations than Jacobi iterative method.
        A - matrix assuming diagonally dominant.
        b - the result colum of the matrix
        xr - the result of last iteration

      Analytic Using Guassian-seidel iterative method:
      4X + 2Y = 2       ===> Xr+1 = (2-2*Yr-0*Zr)/4
      2X + 10Y + 4Z = 6 ===> Yr+1 =(6-2*Xr+1 - 4*Zr)/10
      4Y + 5Z = 5       ===> Zr+1 = (5-0*Xr+1 - 4*Yr+1)/5
        """
    size = len(A)
    var = list(xr)
    for col in range(size):
        res = b[col]
        for row in range(0, size):
            if col != row:
                res -= A[col][row] * var[row]
        var[col] = res / A[col][col]
    return var


def simple_jakobi_method(A, b, xr):
    """
       Jacobi iterative method will iterate over each row in the matrix
       and will calculate it's variables to provide a new solution.
       Will not use the next solution therefore may cause additional iterations.
       A - matrix assuming diagonally dominant.
       b - the result colum of the matrix
       xr - the result of last iteration

       Analytic example using Jacobi iterative method:
      4X + 2Y = 2          ===>  Xr+1 = (2-2*Yr-0*Zr)/4
      2X + 10Y + 4Z = 6    ===>  Yr+1 = (6-2*Xr - 4*Zr)/10
      4Y + 5Z = 5          ===>  Zr+1 = (5-0*Xr-4*Yr)/5
       """
    size = len(A)
    var = []
    for col in range(0, size):
        res = b[col]
        for row in range(0, size):
            if col != row:
                res -= A[col][row] * xr[row]
        var.append(res / A[col][col])

    return var

########################################################
# driver for all iterative method
########################################################


def iterative_method(iterative_method_name, A, b):
    cyan = (51, 255, 255)
    epsilon = 0.0001
    table = [["iteration", "x", "y", "z"]]
    count = 0
    xr = [0] * len(A)
    table.append([str(count) + " - first guess", round(xr[0], 5), round(xr[1], 5), round(xr[2], 5)])
    xr_next = iterative_method_name(A, b, xr)
    condition = True
    if iterative_method_name == simple_jakobi_method:
        TableIt.printTable([["jakobi method:"]], color=cyan)
    else:
        TableIt.printTable([["gaussian seidel method:"]], color=cyan)
    while condition:
        xr = xr_next
        xr_next = iterative_method_name(A, b, xr)
        table.append([str(count), round(xr[0], 5), round(xr[1], 5), round(xr[2], 5)])
        condition = (abs(xr_next[0] - xr[0])) > epsilon
        count += 1
    TableIt.printTable(table, useFieldNames=True, color=(26, 156, 171))

    return count, xr


def main():

    now = datetime.now()
    time = '{0}{1}{2}'.format(now.day, now.hour, now.minute)
    A = [[0, 1, 2], [-2, 1, 0.5], [1, -2, -0.5]]
    b = [0, 4, -4]
    org_pivot(A, b)
    print("=========================Reverse multiplication method============================================")
    print("Matrix A: \n", A)
    print("vector b: \n", b)
    A_inverse = inverse(A)
    print("A inverse: \n", A_inverse)
    x = mul_matrix_wVector(A_inverse, b)
    print("Accuracy level - 5 digits after the dot")
    print("The result of Ax = b using Reverse multiplication method is (x = {:.5f}00000{} , y = {:.5f}00000{} , z = {:.5f}00000{})".format(x[0], time,
                                                                                                       x[1], time,
                                                                                             x[2], time))
    print("\n\n")
    print("=========================iterative method============================================")

    print(A)
    print(b)
    if check_Dominant_diagonal(A):
        print("The matrix has a dominant diagonal - The result will converge")
    else:
        print("The matrix has no dominant diagonal - The result will not necessarily converge")
    jakobi_iter, result = iterative_method(simple_jakobi_method, A, b)
    print("Accuracy level - 5 digits after the dot")
    print("The result of Ax = b is (x = {:.5f}00000{} , y = {:.5f}00000{} , z = {:.5f}00000{})".format(result[0],time, result[1],time, result[2],time))
    print(f"It took {jakobi_iter} iterations to find the result using jakobi method")

    geussian_iter, result2 = iterative_method(simple_gaussian_seidel_method, A, b)
    print("Accuracy level - 5 digits after the dot")
    print("The result of Ax = b is (x = {:.5f}00000{} , y = {:.5f}00000{} , z = {:.5f}00000{})".format(result2[0], time,
                                                                                                       result2[1], time,
                                                                                                       result2[2], time))
    print(f"It took {geussian_iter} iterations to find the result using jakobi method")


main()