
import numpy as np

GRID = np.zeros((2,2))
count = 0
# print(GRID)
# print(GRID[1,2] )

# for l in ([-1,1]):
#     print(l)


def possible(i, j, num):
    global GRID
    rows, cols = GRID.shape
    # Check Straight n x n Squares TL
    for a in range(1, min(GRID.shape)):
        if i + a < rows and j + a < cols:
            if GRID[i + a, j + a] == GRID[i + a, j] == GRID[i, j + a] == num:
                return False
        else:
            break
    # Check Straight n x n Squares TR
    for a in range(1, min(GRID.shape)):
        if i + a < rows and j - a >= 0:
            if GRID[i + a, j - a] == GRID[i + a, j] == GRID[i, j - a] == num:
                return False
        else:
            break
    # Check Straight n x n Squares BL
    for a in range(1, min(GRID.shape)):
        if i - a >= 0 and j + a < cols:
            if GRID[i - a, j + a] == GRID[i - a, j] == GRID[i, j + a] == num:
                return False
        else:
            break
    # Check Straight n x n Squares BR
    for a in range(1, min(GRID.shape)):
        if i - a >= 0 and j - a >= 0:
            if GRID[i - a, j - a] == GRID[i - a, j] == GRID[i, j - a] == num:
                return False
        else:
            break


    # Check Diagonal n x n Squares L
    for a in range(1, min(GRID.shape)):
        if i + a < rows and i - a >= 0 and j + 2*a < cols:
            if GRID[i + a, j + a] == GRID[i - a, j + a] == GRID[i, j + 2*a] == num:
                return False
        else:
            break

    # Check Diagonal n x n Squares T
    for a in range(1, min(GRID.shape)):
        if i + 2*a < rows and j - a >= 0 and j + a < cols:
            if GRID[i + a, j + a] == GRID[i + a, j - a] == GRID[i + 2*a, j] == num:
                return False
        else:
            break

    # Check Diagonal n x n Squares R
    for a in range(1, min(GRID.shape)):
        if i + a < rows and i - a >= 0 and j - 2*a >= 0:
            if GRID[i + a, j - a] == GRID[i - a, j - a] == GRID[i, j - 2*a] == num:
                return False
        else:
            break

    # Check Diagonal n x n Squares B
    for a in range(1, min(GRID.shape)):
        if i - 2*a >= 0 and j - a >= 0 and j + a < cols:
            if GRID[i - a, j + a] == GRID[i - a, j - a] == GRID[i - 2*a, j] == num:
                return False
        else:
            break
    
    
        
    unique, counts = np.unique(GRID, return_counts=True)
    dictionary = dict(zip(unique, counts))

    try:
        if abs(dictionary.get(-1.0) - dictionary.get(1.0)) > 1:
            return False
    except:
        pass
    del dictionary

    return True


def getAllSolutions():
    global GRID
    global count
    rows, cols = GRID.shape
    for i in range(rows):
        for j in range(cols):
            if GRID[i, j] == 0:
                for num in [-1, 1]:
                    if possible(i, j, num):
                        GRID[i, j] = num
                        getAllSolutions()
                        GRID[i, j] = 0
                return

    print(GRID)
    count += 1


def main():
    rows = int(input("Number of Rows: "))
    cols = int(input("NUmber of Columns: "))
    global GRID
    GRID = np.zeros((rows, cols))
    print(GRID.shape)
    getAllSolutions()
    print(count)
    pass


if __name__ == "__main__":
    main()
    pass