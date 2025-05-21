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
    def multiply_ops(matrix_a: SparseMatrix, matrix_b: SparseMatrix):
        if matrix_a.total_cols != matrix_b.total_rows:
            raise ValueError(
                "Matrix A's columns must match Matrix B's rows for multiplication")
    
        ops_result = SparseMatrix(
            total_rows=matrix_a.total_rows, total_cols=matrix_b.total_cols
        )
    
        # Iterate over Matrix A's non-zero elements
        for (row_a, common), matrix_a_value in matrix_a.sparse_elems.items():
            # Directly scan Matrix B's elements for matching row_b == common
            for (row_b, col_b), matrix_b_value in matrix_b.sparse_elems.items():
                if row_b == common:
                    curr_val = ops_result.get_element(row_a, col_b)
                    ops_result.set_element(
                        row_a, col_b, curr_val + matrix_a_value * matrix_b_value)
    
        return ops_result

        return ops_result
