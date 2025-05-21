#!/usr/bin/python3
""" Sparse matrix operations: load from file, get and set element at
a given row & column of a matrix and write results to a file.
"""


class SparseMatrix:

    def __init__(self, in_file='', total_rows=0, total_cols=0):
        """
        Initialize a sparse matrix from a file.
        Args:
            in_file(str): Path to file containing sparse matrix data
            total_rows(int): Number of rows in the matrix
            total_cols(int): Number of columns in the matrix
            sparse_elems(dict): stores non-zero values -> (row, col): value
        """
        self.total_rows = total_rows
        self.total_cols = total_cols
        self.sparse_elems = {}

        if in_file:
            self.load_input_file(in_file)

    def load_input_file(self, in_file):
        """ loads the matrix data from the given file """
        with open(in_file, 'r') as file_lines:
            # get row and col number from the first 2 rows in the file
            total_row = file_lines.readline()[5:]
            total_col = file_lines.readline()[5:]

            self.total_rows = int(total_row)
            self.total_cols = int(total_col)

            for each_line in file_lines:
                each_line = each_line.strip()  # ignore whitespaces

                if each_line:
                    try:
                        # Ensure format is (row, col, value)
                        if not (each_line[0] == '(' and each_line[-1] == ')'):
                            raise SyntaxError(
                                'Input file has wrong parenthesis format')

                        # Parse and strip each component
                        data = each_line[1:-1].split(',')
                        row_str, col_str, val_str = data

                        # Check if value is an int only (if dot is found in str -> float)
                        if (
                            '.' in row_str.strip() or
                            '.' in col_str.strip() or '.' in val_str.strip()
                        ):

                            raise ValueError('Matrix value cannot be float')

                        row, col, value = map(
                            int, [row_str.strip(), col_str.strip(),val_str.strip()]
                        )

                        self.set_element(row, col, value)

                    except (ValueError, SyntaxError):
                        raise ValueError(
                            'Input file has wrong format')

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
        # remove zero vals and store only none-zero vals
        if value == 0:
            self.sparse_elems.pop((elem_row, elem_col), None)
        else:
            self.sparse_elems[(elem_row, elem_col)] = value

    def write_to_file(self, out_file):
        """
        Writes the result of a sparse matrix operation to a file
        in the specified format.
        """
        with open(out_file, 'w') as output_file:
            # write the dimension of the matrix
            output_file.write(f'rows={self.total_rows}\n')
            output_file.write(f'cols={self.total_cols}\n')

            for (row, col), value in self.sparse_elems.items():
                output_file.write(f'({row}, {col}, {value})\n')
