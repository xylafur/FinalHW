""" James Richardson
    1555520         """
import math as m

#puts the elements of the file into a list
def createMatrix(inFile, list):
    for row in inFile:
        list.append(row)
#calculates the distance between two rows.
#the parameters are two lists are made of either ints or strings containing ints
def eudDist(row1, row2):
    tempSum = 0
    for i in range(len(row1)):
        tempSum += ( (int(row1[i]) - int(row2[i]) ) ** 2 )
    return m.sqrt(tempSum)


inFile = open("Data.txt")
outFile = open("RowDistances.txt", 'w')
fileList = []
createMatrix(inFile, fileList)

for row1 in range(len(fileList) - 1 ):
    for row2 in range(row1 + 1, len(fileList) ):
        outFile.write("{}\t".format(eudDist(fileList[row1].split(), fileList[row2].split() )))
        #print(eudDist(fileList[row1].split(), fileList[row2].split() ), end=" ")
    outFile.write("\n")



inFile.close()
outFile.close()
