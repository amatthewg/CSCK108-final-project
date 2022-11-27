import csv
import os
import time

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


def CheckIfNameInDictionary(name):
    names = list(dictionary.keys())
    try:
        index = names.index(name)
    except ValueError:
        return False
    return True


def GenerateNewUser(name):
    data = [name, "None", "None", "None", "None"]
    with open("gamesavedata.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow(data)

def DeleteUser(name):
    pass

def GetUserData(name):
    data = list(dictionary[name].values())
    return data

def ScoreHandling(name, operation, score):
    # scoreAddition
    # scoreSubtraction
    # scoreMultiplication
    # scoreDivision
    tempDictionary = dictionary.get(name)
    print("DEBUG: Printing tempDictionary...")
    time.sleep(1)
    print(tempDictionary)
    time.sleep(5)
    if operation == "addition":
        if tempDictionary.get("scoreAddition") == "None":
            dictionary[name]["scoreAddition"] = score
        elif int(tempDictionary.get("scoreAddition")) < score:
            dictionary[name]["scoreAddition"] = score
    if operation == "subtraction":
        if tempDictionary.get("scoreSubtraction") == "None":
            dictionary[name]["scoreSubtraction"] = score
        elif int(tempDictionary.get("scoreSubtraction")) < score:
            dictionary[name]["scoreSubtraction"] = score
    if operation == "multiplication":
        if tempDictionary.get("scoreMultiplication") == "None":
            dictionary[name]["scoreMultiplication"] = score
        elif int(tempDictionary.get("scoreMultiplication")) < score:
            dictionary[name]["scoreMultiplication"] = score
    if operation == "division":
        if tempDictionary.get("scoreDivision") == "None":
            dictionary[name]["scoreDivision"] = score
        elif int(tempDictionary.get("scoreDivision")) < score:
            dictionary[name]["scoreDivision"] = score

    with open("gamesavedata.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        print("DEBUG: Opening save file to overwrite for ScoreHandling...")
        for key in dictionary:
            scoreAddition = dictionary.get(key).get("scoreAddition")
            scoreSubtraction = dictionary.get(key).get("scoreSubtraction")
            scoreMultiplication = dictionary.get(key).get("scoreMultiplication")
            scoreDivision = dictionary.get(key).get("scoreDivision")

            row = [key, scoreAddition, scoreSubtraction, scoreMultiplication, scoreDivision]

            writer.writerow(row)
    print("DEBUG: Finished overwriting, calling startup...")
    startup()



def ClearSaveData():
    with open("gamesavedata.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(header)
    startup()


startup()
