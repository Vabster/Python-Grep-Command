import sys
import glob

# Author: Dillon McCullough

""" Takes command line arguments and returns lines and their files based on these args """

#Initializes numOfArgs to the number of command line args
numOfArgs = len(sys.argv)
#Initializes bool values to false that later can be true based on command line args
reverseSearch = False
exactSearch = False
#argIndex will be used to determine which arg we are extracting
argIndex = 1

#Checks if their are 4 args, if so then sets one of the bool values to true or exits.
if numOfArgs == 4:
    if sys.argv[argIndex] == "-v":
        reverseSearch = True
    elif sys.argv[argIndex] == "-x":
        exactSearch = True
    else:
        print "Invalid flag parameter"
        sys.exit()
    argIndex += 1
elif numOfArgs != 3:
    print "Invalid number of arguments"
    sys.exit()

#Sets directoryList based on the glob parameter given in the command line
directoryList = glob.glob(sys.argv[argIndex + 1])
if directoryList == []:
    print "No such file(s) exist."

for fileName in directoryList:
    """Loop Comment: opens file from directoryList and displays all lines from file based on command line args"""
    try:
        f = open(fileName, 'r')
    except:
        #Occurs when contents can't be opened (such as a directory)
        #print fileName + ": can not be read"
        #dummy statement
        x = 0

    #Decides which for loop to enter based on bool values reverseSearch and exactSearch
    if (reverseSearch == False and exactSearch == False):
        for line in f:
            """Loop Comment: Displays a single line from file f based on command line args"""
            if sys.argv[argIndex] in line:
                print fileName + ": " + line.rstrip('\n')
    elif exactSearch == True:
        for line in f:
            """Loop Comment: Displays a single line from file f based on command line args"""
            strippedLine = line.rstrip()
            if sys.argv[argIndex] == strippedLine:
                print fileName + ": " + line.rstrip('\n')
    elif reverseSearch == True:
        for line in f:
            """Loop Comment: Displays a single line from file f based on command line args"""
            if sys.argv[argIndex] not in line:
                print fileName + ": " + line.rstrip('\n')
