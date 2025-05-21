#!/usr/bin/python3
""" Sparse matrix operations: perform addition, subtraction, multiplication """

from sparse_matrix import SparseMatrix


class SparseMatrixOperation:

    @staticmethod
    def add_ops(matrix_a: SparseMatrix, matrix_b: SparseMatrix):
        """adds and retuns a new sparse matrix with the sum of the sparse matrix values """
        if (
            matrix_a.total_rows != matrix_b.total_rows or
            matrix_a.total_cols != matrix_b.total_cols
        ):
            raise ValueError('Matrix dimension of both files must be equal')

        ops_result = SparseMatrix(
            total_rows=matrix_a.total_rows, total_cols=matrix_a.total_cols
        )

        # Copy all elements from matrix A
        for (row, col), value in matrix_a.sparse_elems.items():
            ops_result.set_element(row, col, value)

        # Add values from matrix B to the existing ones
        for (row, col), value in matrix_b.sparse_elems.items():
            curr_val = ops_result.get_element(row, col)
            ops_result.set_element(row, col, curr_val + value)

        return ops_result

    @staticmethod
    def subtract_ops(matrix_a: SparseMatrix, matrix_b: SparseMatrix):
        """Subtracts the values of sparse matrix b from sparse matrix a"""
        if (
            matrix_a.total_rows != matrix_b.total_rows or
            matrix_a.total_cols != matrix_b.total_cols
        ):
            raise ValueError('Matrix dimension of both files must be equal')

        ops_result = SparseMatrix(
            total_rows=matrix_a.total_rows, total_cols=matrix_a.total_cols
        )

        # Start with all elements from matrix A
        for (row, col), value in matrix_a.sparse_elems.items():
            ops_result.set_element(row, col, value)

        # Subtract elements from matrix B
        for (row, col), value in matrix_b.sparse_elems.items():
            curr_val = ops_result.get_element(row, col)
            ops_result.set_element(row, col, curr_val - value)

        return ops_result

    @staticmethod
    def multiply_ops(matrix_a:SparseMatrix, matrix_b: SparseMatrix):
        if matrix_a.total_cols != matrix_b.total_rows:
            raise SyntaxError(
                'the first matrix total column must be the same as matrix_b total rows'
            )

        ops_result = SparseMatrix(total_rows=matrix_a.total_rows, total_cols=matrix_b.total_cols)

        # Group all non-zero elements of 'matrix_b' by their row index
        matrix_b_row_idx = {}

        for (b_row, b_col), value in matrix_b.sparse_elems.items():
            if b_row not in matrix_b_row_idx:
                matrix_b_row_idx[b_row] = []
            matrix_b_row_idx[b_row].append((b_col, value))

        temp = {}  # holds computed result temporarily

        for (a_row, a_col), a_value in matrix_a.sparse_elems.items():
            # this will process only when theres matching rows in matrix b
            if a_col in matrix_b_row_idx:
                for b_col, b_value in matrix_b_row_idx[a_col]:
                    ops_result_key = (a_row, b_col)

                    if ops_result_key in temp:
                        temp[ops_result_key] += a_value * b_value
                    else:
                        temp[ops_result_key] = a_value * b_value

        # Set all nonzero values
        for (row, col), value in temp.items():
            if value != 0:
                ops_result.set_element(row, col, value)

        return ops_result


