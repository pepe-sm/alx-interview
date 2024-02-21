def rotate_2d_matrix(matrix):
    """Rotates an m by n 2D matrix in place."""
    if not isinstance(matrix, list) or not matrix:
        return

    n = len(matrix)
    if not all(isinstance(row, list) and len(row) == n for row in matrix):
        return

    for layer in range(n // 2):
        first, last = layer, n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            # left -> top
            matrix[first][i] = matrix[last - offset][first]
            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]
            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]
            # top -> right
            matrix[i][last] = top
