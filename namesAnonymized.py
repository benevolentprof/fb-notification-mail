"""This part isolates the names and create a unique ID for each of them"""
with open("example.csv") as dataIn, open('personsID.csv', 'w') as dataOut:
    nameTable = {}
    counter = 0
    for row in dataIn:
        splitRow = row.strip().split(",")
        persons = splitRow[0] #all names in the csv
        # print persons
        if persons in nameTable:
            id = nameTable[persons]
        else:
            nameTable[persons] = str(counter)
            id = counter
            counter += 1
    # print nameTable
    [dataOut.write('{0},{1}\n'.format(key, value)) for key, value in nameTable.items()] #create ID, PERSON Table

# """This part uses the newly created unique ID to substitute for the name section in the original file"""
# with open("example.csv") as dataIn, open("newAnonymizedTable.csv", 'w') as anonOut:
#     for row in dataIn:
#         splitRow = row.split(",") #no strip so that the newlines are preserved in the new file
#         splitRow[0] = nameTable[splitRow[0]] #replace the name with ID
#         joinAll = ",".join(splitRow)   #join the new ID column with the original file
#         anonOut.write(joinAll) #write the new line to the file