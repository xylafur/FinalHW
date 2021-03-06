"""     James Richardson
        1555520
        COSC-1306           """
#puts the elements of the file into a list
def createMatrix(inFile, list):
    for row in inFile:
        list.append(row)
#calculates highest number in a list
def max(list):
    max = int(list[0])
    for num in list:
        if int(num) > max:
            max = int(num)
    return max
#calculates lowest number in a list
def min(list):
    min = int(list[0])
    for num in list:
        if int(num) <min:
            min = int(num)
    return min
#computes the average of a list, returns float
def mean(list):
    sum = 0
    for num in list:
        sum += int(num)
    return float(sum / len(list))
#just finds the range, did it the lazy way
def range(list):
    return max(list) - min(list)
#finds the median, he didn't say we couldn't use sort function
def median(list):
    list.sort()
    return (list[len(list) / 2])
#writes to file
def writeToFile(outFile, list):
    temp = []
    temp.append(min(list));temp.append(max(list))
    temp.append(mean(list));temp.append(range(list))
    temp.append(median(list))
    for elm in temp:
        outFile.write('{}\t'.format(elm))
    outFile.write('\n')


inFile = open("Data.txt")
outFile = open("RowStatistics.txt","w")
list = []

createMatrix(inFile, list)

for row in list:
    writeToFile(outFile, row.split() )



inFile.close()
outFile.close()
