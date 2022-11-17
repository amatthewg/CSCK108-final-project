import csv
import os

# This file will be used to store/access user save data to a CSV file
#
# gamesavedata.csv will not be a file on github, will automatically generate when user runs
# the script on their machine


# generate save file with default headers

"""
We need methods for the following:
When user chooses to save session data,
    1. Write their data to the save file, then
    2. Generate new saveData dictionary from that file
So, make one method for saving data

ReadFromSaveFile will still run like normal, will automatically generate 
dictionary when program starts.

The save session data method will just overwrite that dictionary
with the more up-to-date data.

So, just make a dedicated method to generate a dictionary from the data file.
"""





# Header variable to be written into the save file
header = ["name", "best_score_addition", "best_score_subtraction",
          "best_score_multiplication", "best_score_division"]

# dictionary that will be loaded with save data from file
saveData = {}

# generates file if it doesn't exist already
def fileOnStartup():
    if os.path.isfile("gamesavedata.csv"):
        print('File exists!')
    else:
        with open('gamesavedata.csv', 'a') as file:
            csvWriter = csv.writer(file)
            csvWriter.writerow(header)




# generates save data dictionary to be used by program
def generateDictionary():
    with open('gamesavedata.csv') as saveFile:
        fileReader = csv.reader(saveFile, delimiter=',')

        firstRow = True
        for row in fileReader:
            if firstRow:
                firstRow = False
                continue
            try:
                name = row[0]
                addScore = row[1]
                subtScore = row[2]
                multScore = row[3]
                divScore = row[4]
            except IndexError:
                continue

            saveData[name] = {
                "scoreAddition" : addScore,
                "scoreSubtraction" : subtScore,
                "scoreMultiplication" : multScore,
                "scoreDivision" : divScore
            }


# function to write to save file, takes list as input
# for example: [name, score, score, score, score]
# above will be written as a row to the csv
def WriteToSaveFile(list):

    with open('gamesavedata.csv', 'w') as f:
        writer = csv.writer(f)

        writer.writerow(list)

# method will be called at beginning of program to load save file
def loadSaveFile():
    generateDictionary()


# these are called at program startup b/c this file is imported and executed in main.py
fileOnStartup()
loadSaveFile()



