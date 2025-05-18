#!/usr/bin/python3
""" Sparse matrix operations: load from file, perform addition, subtraction,
multiplication, and write results to a file.
"""
import ast


class SparseMatrix:

    def __init__(self, in_file='', total_rows=0, total_cols=0):
        """
        Initialize a sparse matrix from a file.
        Args:
            in_file(str): Path to file containing sparse matrix data
            row_num(int): Number of rows in the matrix
            col_num(int): Number of columns in the matrix
            sparse_elems(dict): stores non-zero values -> (row, col): value
        """

        self.total_rows = total_rows
        self.total_cols = total_cols
        self.sparse_elems = {}

        if in_file:
            self.load_input_file(in_file)

    def load_input_file(self, file_path):
        """ loads the matrix data from the given file """
        with open('file_path', 'r') as file_lines:
            # get row and col number from the first 2 rows in the file
            total_row = file_lines.readline()[5:]
            total_col = file_lines.readline()[5:]

            self.row_num = int(total_row)
            self.col_num = int(total_col)

            for each_line in file_lines:
                each_line = each_line.strip()  # ignore whitespaces

                if each_line:
                    # handle wrong formats: float values or different brackets
                    try:
                        data = ast.literal_eval(each_line)
                        if (
                            isinstance(data, tuple)
                            and len(data) == 3
                            and all(isinstance(i, int) for i in data)
                        ):
                            row, col, value = data
                            self.sparse_elems[(row, col)] = value
                        else:
                            raise ValueError
                    except (ValueError, SyntaxError):
                        raise SyntaxError('Input file has wrong format')

                    # store non-zero values
                    if value > 0:
                        self.sparse_elems[(row, col)] = value

    def get_element(self, elem_row, elem_col):
        """
        get the value at this specific locatio
        Args:
            elem_row(int): index of the current row
            elem_col(int): index of the current column
        Returns:
            the value at the specified position (0 if not set)
        """
        return self.sparse_elems.get((elem_row, elem_col), 0)

    def set_element(self, elem_row, elem_col, value):
        """
        set the value at this specific location
        Args:
            elem_row(int): index of the current row
            elem_col(int): index of the current column
            value(int): value to set
        Returns:
            the value at the specified position (0 if not set)
        """
        if (
            elem_row < 0 or elem_row >= self.total_rows or
            elem_col < 0 or elem_col >= self.total_cols
        ):
            raise IndexError("Matrix indices out of range")

        # remove zero vals and store only none-zero vals
        if value == 0:
            self.sparse_elems.pop((elem_row, elem_row), None)
        else:
            self.sparse_elems[(elem_row, elem_row)] = value

    def add_operation(self, matrxi_b):
        """ Add another sparse matrix to this one and return the sum. """
        if (
            self.total_rows != matrxi_b.total_rows or
            self.total_cols != matrxi_b.total_cols
        ):
            raise ValueError('Matrix dimension of both files must be equal')

        ops_result = SparseMatrix(
            total_rows=self.total_rows,
            total_cols=self.total_cols
        )

        # add elements from the current matrix
        for (row, col), value in self.sparse_elems.items():
            ops_result.set_element(row, col, value)

        # Add elements from the incoming operand (2nd sparse matrix)
        for (col, row), value in self.sparse_elems.items():
            curr_sparse_value = ops_result.get_element(row, col)
            ops_result.set_element(row, col, curr_sparse_value + value)

        return ops_result

    def write_to_file(self, out_file):
        """
        Writes the result of a sparse matrix operation to a file
        in the specified format.
        """
        with open(out_file, 'w') as output_file:
            # write the dimension of the matrix
            output_file.write(f'rows={self.total_rows}\n')
            output_file.write(f'cols={self.total_cols}\n')

            # The write non zero elements in a sorted order
            sorted_result = sorted(self.sparse_elems.items())
            for (row, col), value in sorted_result:
                output_file.write(f'{row}, {col}, {value}\n')
