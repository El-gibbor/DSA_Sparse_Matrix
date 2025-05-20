#!/usr/bin/python3
""" Sparse matrix operations: perform addition, subtraction, multiplication """

from sparse_matrix import SparseMatrix


class SparseMatrixOperation:

    @staticmethod
    def add_ops(matrix_a: SparseMatrix, matrix_b: SparseMatrix):
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
            current = ops_result.get_element(row, col)
            ops_result.set_element(row, col, current + value)

        return ops_result

    @staticmethod
    def subtract_ops(matrix_a: SparseMatrix, matrix_b: SparseMatrix):
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
            current = ops_result.get_element(row, col)
            ops_result.set_element(row, col, current - value)

        return ops_result
