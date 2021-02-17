# Jhonatan Becerra
# HW4 - last-to-start

# name of the file to be read
fileToRead = "act.txt"

# number of sets
nSets = 0

# activities per set
nActivities = []

# start time for a given activity
startTime = []

# end time for a given activity
endTime = []

# activity number
activityNum = []

# starting index for a given set
indexForSet = []
indexForSet.append(0)


# read file
def readFile(fileName):
    # open the file
    file = open(fileName, "r")

    # array to hold lines read from file
    fileLine = []

    # read the file lines into an array
    for x in file:
        fileLine.append(x)

    #close the file
    file.close()

    return fileLine


# create property arrays of items from array of lines
def parseLines(lineArray):
    # get the number of sets
    global nSets
    nSets = int(lineArray[0])

    # offsets the index in the line
    counter = 2

    # go through every line and split it into its parts
    for x in range(1,len(lineArray)):
        # split the line into pieces
        y = lineArray[x].split(" ")

        # if the length is 1, must be number
        # of activities for set
        if len(y) == 1:
            # track the number of activities for that set (remove newline)
            nActivities.append(int(y[0].replace('\n','')))

            # track the start index for an activity in a set
            # only do it if it's not the first index
            if x != 1:
                indexForSet.append(x - counter)
                counter += 1
        else:
            # track the activity number
            activityNum.append(int(y[0]))

            # track the start time for activity
            startTime.append(int(y[1]))

            # track the end time for activity
            endTime.append(int(y[2].replace('\n', '')))
    return

# sort file
def sort(startIndex, endIndex):
    for i in range(startIndex+1,endIndex+1):
        # get current element
        currentElem = startTime[i]
        currentActivity = activityNum[i]
        currentEnd = endTime[i]

        # get previous index
        prevIndex = i - 1

        # if current element is greater than the last element
        while prevIndex >= startIndex and startTime[prevIndex] < currentElem:
            # swap the elements
            startTime[prevIndex+1] = startTime[prevIndex]
            activityNum[prevIndex+1] = activityNum[prevIndex]
            endTime[prevIndex+1] = endTime[prevIndex]

            # check the elements before
            prevIndex = prevIndex -1

            startTime[prevIndex+1] = currentElem
            activityNum[prevIndex+1] = currentActivity
            endTime[prevIndex+1] = currentEnd

# print file
def schedule(startIndex, endIndex):
    i = startIndex
    tempArray = []

    # first one will always be selected
    tempArray.append(activityNum[startIndex])

    # check all other values
    for j in range(startIndex+1, endIndex+1):
        # if the end time of the current value is
        # less than or equal to the start time of the
        # previous activity, save it
        if endTime[j] <= startTime[i]:
            tempArray.append(activityNum[j])
            i = j;
    return tempArray


if __name__ == "__main__":
    # read the file
    lines = readFile(fileToRead)

    # break file lines into array values
    parseLines(lines)

    # sort the subsets in the arrays
    for k in range(0, nSets):
        tempArr = []
        print("Set {}".format(k + 1))
        if k == (nSets-1):
            sort(indexForSet[k], len(startTime)-1)
            tempArr = schedule(indexForSet[k], len(startTime)-1)
        else:
            sort(indexForSet[k], indexForSet[k+1]-1)
            tempArr = schedule(indexForSet[k], indexForSet[k+1]-1)

        # reverse array sorting
        tempArr.reverse()
        print("Number of activities selected = {}".format(len(tempArr)))
        print("Activities: {}".format(tempArr))