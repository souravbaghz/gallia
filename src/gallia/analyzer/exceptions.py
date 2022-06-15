"""
gallia-analyze Exceptions module
"""

if __name__ == "__main__":
    exit()


class EmptyTableException(Exception):
    """
    exception class for empty table error
    """

    def __init__(self):
        super().__init__("Empty Table.")


class ColumnMismatchException(Exception):
    """
    exception class for column mismatch
    """

    def __init__(self):
        super().__init__("Columns Mismatch.")
