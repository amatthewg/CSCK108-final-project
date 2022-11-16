import csv

# This file will be used to store/access user save data to a CSV file
# gamesavedata.csv will not be a file on github, will automatically generate when user runs
# the script on their machine


# generate save file with default headers
header = ["name", "best_score_addition", "best_score_subtraction",
          "best_score_multiplication", "best_score_division"]

# dictionary that will be loaded with save data from file
saveData = {


}

def generateSaveFile():
    with open('gamesavedata.csv', 'w') as f:

        # create csv writer
        writer = csv.writer(f)


        # write row to csv
        writer.writerow(header)

def WriteToSaveFile(data):

    with open('gamesavedata.csv', 'w') as f:
        writer = csv.writer(f)

        writer.writerow(data)


# will read contents of save file to a dictionary to use

with open('gamesavedata.csv') as saveFile:
    try:
        csvReader = csv.reader(saveFile)
        for row in csvReader:
            print(row[0])
    except IndexError:
        pass


