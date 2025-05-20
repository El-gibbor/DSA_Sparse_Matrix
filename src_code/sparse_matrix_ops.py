#!/usr/bin/python3
""" Sparse matrix operations: perform addition, subtraction, multiplication """

from sparse_matrix import SparseMatrix

class SparseMatrixOperation:

    @staticmethod
    def add_ops(matrix_a: SparseMatrix, matrix_b: SparseMatrix) -> SparseMatrix:
        if (
            matrix_a.total_rows != matrix_b.total_rows or
            matrix_a.total_cols != matrix_b.total_cols
        ):
            raise ValueError('Matrix dimension of both files must be equal')

        result = SparseMatrix(total_rows=matrix_a.total_rows, total_cols=matrix_a.total_cols)

        all_positions = set(matrix_a.sparse_elems.keys()) | set(matrix_b.sparse_elems.keys())

        for row, col in all_positions:
            value = matrix_a.get_element(row, col) + matrix_b.get_element(row, col)
            result.set_element(row, col, value)

        return result

    @staticmethod
    def subtract_ops(matrix_a: SparseMatrix, matrix_b: SparseMatrix) -> SparseMatrix:
        if (
            matrix_a.total_rows != matrix_b.total_rows or
            matrix_a.total_cols != matrix_b.total_cols
        ):
            raise ValueError('Matrix dimension of both files must be equal')

        result = SparseMatrix(total_rows=matrix_a.total_rows, total_cols=matrix_a.total_cols)

        all_positions = set(matrix_a.sparse_elems.keys()) | set(matrix_b.sparse_elems.keys())

        for row, col in all_positions:
            value = matrix_a.get_element(row, col) - matrix_b.get_element(row, col)
            result.set_element(row, col, value)

        return result
