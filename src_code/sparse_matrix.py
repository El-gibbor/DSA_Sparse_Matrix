#!/usr/bin/python3

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
                        