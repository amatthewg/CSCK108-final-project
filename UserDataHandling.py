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
header = ["name", "best_score_addition", "best_score_subtraction",
          "best_score_multiplication", "best_score_division"]

dictionary = {}

# startup logic for save file
def startup():
    # this portion generates save file if it doesn't already exist
    if os.path.isfile("gamesavedata.csv"):
        print('DEBUG: File exists!')  # debug
    else:
        with open('gamesavedata.csv', 'a+') as file:
            csvWriter = csv.writer(file)
            csvWriter.writerow(header)

    # this portion opens the save file and puts everything into the dictionary
    with open('gamesavedata.csv', 'r') as saveFile:
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

            dictionary[name] = {
                "scoreAddition": addScore,
                "scoreSubtraction": subtScore,
                "scoreMultiplication": multScore,
                "scoreDivision": divScore
            }


def WriteToSaveFile(list):
    with open('gamesavedata.csv', 'a+') as f:
        writer = csv.writer(f)

        writer.writerow(list)
    startup()


def CheckIfNameInDictionary(name):
    names = list(dictionary.keys())
    try:
        index = names.index(name)
    except ValueError:
        return False
    return True


def GenerateNewUser(name):
    data = [name, "None", "None", "None", "None"]
    WriteToSaveFile(data)

def DeleteUser(name):
    pass

def GetUserData(name):
    data = list(dictionary[name].values())
    return data

def ScoreHandling(name, operation, score):
    print("Correct score: ", score)

def ClearSaveData():
    with open("gamesavedata.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(header)
    startup()


startup()
