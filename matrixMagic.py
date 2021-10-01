defaultMatrixX = 5
defaultMatrixY = 5
mat1 = [[]]
mat2 = [[]]

def printMatrix(mat):
    for x in range(len(mat)):
        print(mat[x])    

def buildDefaultMatrix(defaultMatSizeX,defaultMatSizeY):
    if (defaultMatSizeX == 0):
        defaultMatSizeX = int(input("Matrix x size: "))
    if (defaultMatSizeY == 0):
        defaultMatSizeY = int(input("Matrix y size: "))
    return [[ x + (y * defaultMatSizeX) for x in range(defaultMatSizeX)] for y in range(defaultMatSizeY)]
    
def addMatrixes(mat1,mat2):
    return [[ mat1[x][y] + mat2[x][y] for y in range(len(mat1[x]))] for x in range(len(mat1))]

def subtractMatrixes(mat1,mat2):
    return [[ mat1[x][y] - mat2[x][y] for y in range(len(mat1[x]))] for x in range(len(mat1))]
   
def multiplyMatrixes(mat1,mat2):
    return [[ mat1[x][y] * mat2[x][y] for y in range(len(mat1[x]))] for x in range(len(mat1))]

def _devideIfNotZero(numOne,numTwo):
    if numOne != 0 and numTwo != 0:
        return numOne/numTwo
    else:
        return "NAN"

def devideMatrixes(mat1,mat2):
    return [[ [_devideIfNotZero(mat1[x][y], mat2[x][y])] for y in range(len(mat1[x]))] for x in range(len(mat1))]



if __name__ == "__main__":  
    if(mat1 == [[]] or mat2 == [[]]): 
        mat1 = buildDefaultMatrix(defaultMatrixX,defaultMatrixY)
        mat2 = mat1
        
    print("mat1:")
    printMatrix(mat1)
    print("mat2:")
    printMatrix(mat2)
    
    print("Added Matrixes:")
    printMatrix(addMatrixes(mat1,mat2))
    
    print("Subtracted Matrixes:")
    printMatrix(subtractMatrixes(mat1,mat2))
    
    print("Multiplyed Matrixes:")
    printMatrix(multiplyMatrixes(mat1,mat2))
    
    print("Devided Matrixes:")
    printMatrix(devideMatrixes(mat1,mat2))
