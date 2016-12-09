""" James Richardson
    1555520         """
import math as m

#puts the elements of the file into a list
def createMatrix(inFile, list):
    for row in inFile:
        list.append(row)
#makes columns rows
def flip(list):
    temp = [elm.split() for elm in list]
    retArr = []
    for colm in range(0,  5):
        temp2 = []
        for row in temp:
            temp2.append(row[colm])
        retArr.append(temp2)
    return retArr
#calculates the distance between two rows.
#the parameters are two lists are made of either ints or strings containing ints
def eudDist(row1, row2):
    tempSum = 0
    for i in range(len(row1)):
        tempSum += ( (int(row1[i]) - int(row2[i]) ) ** 2 )
    return m.sqrt(tempSum)


inFile = open("Data.txt")
outFile = open("ColumnDistances.txt", 'w')
fileList = []
createMatrix(inFile, fileList)
#print(fileList)
fileList = flip(fileList)

for row1 in range(len(fileList) - 1 ):
    for row2 in range(row1 + 1, len(fileList) ):
        outFile.write("{}\t".format(eudDist(fileList[row1], fileList[row2] )))
        #print(eudDist(fileList[row1].split(), fileList[row2].split() ), end=" ")
    outFile.write("\n")



inFile.close()
outFile.close()
