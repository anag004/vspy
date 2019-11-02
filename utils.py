# This module has some utility functions used in other modules

# Compute the matrix rank of a 2d list
def matrix_rank(arr):
    rows = len(arr)
    cols = len(arr[0])

    # Check that the list is rectangular 
    for i in range(1, rows):
        if (len(arr[i]) != cols):
            raise Exception("Cannot find rank of non-rectangular list")
    
    # Iterate over each row
    row = 0
    col = 0
    ans = 0
    while (row < rows and col < cols):
        pivotElement = arr[row][col]
        if (pivotElement != pivotElement.zero()):
            # Divide each element in the current row by pivotElement
            for j in range(col, cols):
                arr[row][j] /= pivotElement
            
            # Subtract from each row above and below the current element
            for i in range(rows):
                if (i != row):
                    multFactor = arr[i][col]
                    for j in range(col, cols):
                        arr[i][j] -= multFactor * arr[row][j]

            # Move to the next row and column and increase the rank by 1
            row += 1
            col += 1
            ans += 1
        else:
            # Look for a row below which has a nonzero element
            swapRow = -1
            for i in range(row + 1, rows):
                if (arr[i][col] != pivotElement.zero()):
                    swapRow = i 
                    break

            if (swapRow == -1):
                # If we don't find a nonzero element move to the next column
                col += 1
            else:
                # Swap the two rows
                for i in range(cols):
                    tmp = arr[row][i]
                    arr[row][i] = arr[swapRow][i]
                    arr[swapRow][i] = tmp

    return ans