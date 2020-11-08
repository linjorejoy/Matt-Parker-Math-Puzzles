
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
    for a in range(rows):
        for b in range(cols):
            dx, dy = (i-a), (j-b)
            if (0 <= (i - dx) < rows and 
            0 <= (i - dy) < rows and 
            0 <= (i - dx - dy) < rows and 
            0 <= (j - dy) < cols and 
            0 <= (j + dx) < cols and 
            0 <= (j + dx - dy) < cols) :
                if GRID[i - dx, j - dy] == GRID[i - dy, j + dx] == GRID[i - dx - dy, j + dx - dy] == num:
                    return False
                    
    for a in range(rows):
        for b in range(cols):
            dx, dy = (i-a), (j-b)
            if (0 <= (i - dx) < rows and 
            0 <= (i + dy) < rows and 
            0 <= (i + dx - dy) < rows and 
            0 <= (j - dy) < cols and 
            0 <= (j - dx) < cols and 
            0 <= (j - dx - dy) < cols) :
                if GRID[i - dx, j - dy] == GRID[i + dy, j - dx] == GRID[i + dx - dy, j - dx - dy] == num:
                    return False
    
    
    
        
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
    cols = int(input("Number of Columns: "))
    global GRID
    GRID = np.zeros((rows, cols))
    # print(GRID.shape)
    getAllSolutions()
    print(count)
    pass


if __name__ == "__main__":
    main()