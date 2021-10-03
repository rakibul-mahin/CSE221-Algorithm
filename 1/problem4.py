'''
PROBLEM: 4
MATRIX MULTIPLICATION
'''

'''
A = [
        [1, 2],
        [3, 4]
    ]
B = [
        [1, 2],
        [3, 4]
    ]

============================================================================================
row x col
C[0][0] = A[0][0]*B[0][0] + A[0][1]*B[1][0]   C[0][1] = A[0][0]*B[0][1] + A[0][1]*B[1][1]
C[1][0] = A[1][0]*B[0][0] + A[1][1]*B[1][0]   C[1][1] = A[1][0]*B[0][1] + A[1][1]*B[1][1] 
============================================================================================
==================================
'''

'''
Rules of Matrix Multiplication:
A = row x col
B = row x col

if -> A_row is same as B_col:
    then, we can do Matrix multiplication
    
According to our question, both A and B
are n x n matrix:

So, if A = 2 x 2 then B = 2 x 2
thus, A_row == B_col

So, for any Valid input of A and B our program
can be executed.

And the resultant matrix C will also be 2 x 2

============================================================================================
row x col
C[0][0] = A[0][0]*B[0][0] + A[0][1]*B[1][0]   C[0][1] = A[0][0]*B[0][1] + A[0][1]*B[1][1]
C[1][0] = A[1][0]*B[0][0] + A[1][1]*B[1][0]   C[1][1] = A[1][0]*B[0][1] + A[1][1]*B[1][1] 
============================================================================================
'''


def create_matrix(data_to_pass, n, the_matrix_instance=[]):
    count = 0

    for i in range(n):
        temp_matrix = []
        input_index = 0

        for j in range(n):
            temp_matrix.append(int(data_to_pass[count][input_index]))
            input_index += 2

        count += 1
        the_matrix_instance.append(temp_matrix)

    return the_matrix_instance


def Multiply_matrix(A, B):
    # n is the size of the matrix
    n = len(A)
    C = create_final_matrix(n)

    for i in range(0, len(A)):
        for j in range(0, len(A)):
            for k in range(0, len(A)):
                C[i][j] += A[i][k] * B[k][j]

    return C


def create_final_matrix(size_of_matrix):
    final_matrix = []

    # This will create n rows, where n = size_of_matrix
    for row in range(size_of_matrix):
        blank_row = []
        final_matrix.append(blank_row)

    # This will insert 0's in final_matrix of size n, where n = size of matrix
    for nth_col in range(size_of_matrix):
        [final_matrix[nth_col].append(0) for _ in range(size_of_matrix)]

    return final_matrix


with open("input4.txt", "r") as input_file:
    each_line_from_input = []
    final_array_data = []

    [each_line_from_input.append(each_line) for each_line in input_file]

    for data in each_line_from_input:
        if data != '\n':
            final_array_data.append(data.replace("\n", ""))

    n = int(final_array_data[0])
    data_for_matrix_A = final_array_data[1:n + 1]
    data_for_matrix_B = final_array_data[n + 1:]

    A = []
    B = []

    A = create_matrix(data_for_matrix_A, n, A)
    B = create_matrix(data_for_matrix_B, n, B)
    C = Multiply_matrix(A, B)

    with open("output4.txt", "w") as output_file:
        for i in range(n):
            [output_file.write("{} ".format(C[i][j])) for j in range(n)]
            output_file.write("\n")