import csv

# QUICK INFO!
# Made reading from CSV file in main for now, we can move it somewhere else later

if __name__ == '__main__':

    # Declaration of lists that will be used to store column names and data (data in a list of lists)
    columnNamesList = []
    listOfDataLists = []

    # Read CSV file
    with open('dataset.csv', newline='') as csvfile:
        file = csv.reader(csvfile, delimiter=' ', quotechar='|')

        # Counter is for checking whether it is the first row or not
        counter = 0

        for row in file:

            # Find all column names or data from string row[0] that contains them separated by commas
            dataFromRow = row[0].split(',')

            # For first row of the file get the title of each column
            if counter == 0:
                for columnName in dataFromRow:
                    columnNamesList.append(columnName)
                    # Adding new empty lists here cuz it only executes at the beginning of the reading
                    listOfDataLists.append([])

            # For all other rows that contain data get data - add data to lists (representing columns of the dataset)
            # that are in the listOfDataLists, each of these has a columnCounter index, eg. HeartDiseaseOrAttack is on
            # index 0 (column no. 0), so add values to a list that is on this index
            else:
                columnCounter = 0
                for data in dataFromRow:
                    listOfDataLists[columnCounter].append(data)
                    columnCounter = columnCounter + 1

            counter = counter + 1

        # Print number of data values from all of the columns to check if all the data got in
        # (should be 253680 values per column in an unedited Heart Disease Health Indicators Dataset from the site)
        for i in range (0, len(columnNamesList)):
            print(columnNamesList[i] + " : " + str(len(listOfDataLists[i])))

