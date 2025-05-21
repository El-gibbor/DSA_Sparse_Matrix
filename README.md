## Sparse Matrix Operations
A simple command-line tool to **add, subtract, or multiply sparse matrices** stored in plain text files using an efficient internal representation.

### Matrix File Format

Each matrix file must follow this format:

```
rows=3
cols=4
(0, 1, 5)
(1, 2, 8)
(2, 3, -2)
```

* The first two lines define the matrix dimensions.
* Each tuple represents a non-zero value at `(row, column, value)`.

---

### How to Run

```bash
python3 main.py
```

* Choose an operation:  
  `1` = Addition of sparse matrix  
  `2` = Subtraction of sparse matrix  
  `3` = Multiplication of sparse matrix  

* Provide paths to two matrix files.

* The result will be saved in the `result_outputs/` directory with an auto-generated filename.
