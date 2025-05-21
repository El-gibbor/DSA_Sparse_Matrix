#!/usr/bin/python3

import os
from sparse_matrix import SparseMatrix
from matrix_operations import SparseMatrixOperation


def execute_sparse_matrix():
    print('\n******* Sparse Matrix Operation ********\n')
    print('(1). Addition of sparse matrix')
    print('(2). Subtraction of sparse matrix')
    print('(3). Multiplication of sparse matrix\n')
    print('=========================================')

    try:
        ops = int(input('Select operation by inputting 1, 2 or 3: '))
        if ops not in {1, 2, 3}:
            raise ValueError

        matrix_a_file = input('\nEnter path to first matrix file: ').strip()
        matrix_b_file = input('Enter path to second matrix file: ').strip()

        # Load the two sparse matrices
        matrix_a = SparseMatrix(in_file=matrix_a_file)
        matrix_b = SparseMatrix(in_file=matrix_b_file)

        # Validate/create output directory
        os.makedirs('result_outputs', exist_ok=True)

        # Create a filename based on input filenames
        file_a = os.path.splitext(os.path.basename(matrix_a_file))[0]
        file_b = os.path.splitext(os.path.basename(matrix_b_file))[0]

        # Perform selected operation
        if ops == 1:
            result_matrix = SparseMatrixOperation.add_ops(matrix_a, matrix_b)
            output_filename = f'sum_of_{file_a}_and_{file_b}.txt'
        elif ops == 2:
            result_matrix = SparseMatrixOperation.subtract_ops(matrix_a, matrix_b)
            output_filename = f'sub_of_{file_a}_and_{file_b}.txt'
        else:  # ops == 3
            result_matrix = SparseMatrixOperation.multiply_ops(matrix_a, matrix_b)
            output_filename = f'product_of_{file_a}_and_{file_b}.txt'

        # Write result to output file
        output_path = os.path.join('result_outputs', output_filename)
        result_matrix.write_to_file(output_path)

        print('\nSparse Matrix operation completed successfully!')
        print('\n=========================================================================')
        print(f'Output File: {output_path}')
        print('=========================================================================')

    except FileNotFoundError:
        print('\nError: One or both matrix files were not found!')
    except ValueError:
        print('\nError: Invalid operation input. Please enter 1, 2, or 3.')


if __name__ == '__main__':
    execute_sparse_matrix()
