""" James Richardson
    1555520         """
#Matrix = [6][5]
#Computer euclid distance between columns


def EuclidDistances(inputfile, outputfile):
    deltaSquared = [] #should be len 6 and each sublist len 4
    for line in inputfile:
        numbers = [int(ch) for ch in line.strip().split()]
        i = 0
        listnum = []
        while (i < len(numbers) - 1):
            listnum.append((numbers[i] - numbers[i+1])**2)
            i += 1
        deltaSquared.append(listnum)

    for i in range(len(deltaSquared[0])):
        sum = 0
        for n in range(len(deltaSquared)):
            sum += deltaSquared[n][i]

        outputfile.write(str(sum ** 0.5) + " ")
    outputfile.write("\n")

# MAIN ==================================================================
infile = open('Data.txt', 'r')
outfile = open('EuclidDistances.txt', 'w')

EuclidDistances(infile, outfile)

infile.close()
outfile.close()
