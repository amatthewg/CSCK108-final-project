import csv
import os
import time

"""
This is the file that will be used to store all the methods pertaining to storing/accessing
user save data.

Arguably the most important method here is the ScoreHandling method, as it is the method
that handles all the user scores for the various operation games. 

If the user runs the program on their machine for the first time, the program
will (should, hopefully) generate a CSV save file in the same directory as the 
rest of the files. 

If the user has already run the program on their machine, the program will
(should, hopefully) detect that the CSV file has already been generated and
will not overwrite it and make a new one. 
"""

# This is the header variable that is automatically written to the new file if it is generated.
header = ["name", "best_score_addition", "best_score_subtraction",
          "best_score_multiplication", "best_score_division"]

# Initialize an empty dictionary to store user data during runtime
dictionary = {}


# This is the startup method, which is not only called at the start of runtime,
# but also multiple times during runtime, as it is the method that actually
# accesses the CSV save file and translates it to the above dictionary for
# easy access during runtime.
def startup():
    # this portion generates save file if it doesn't already exist
    if os.path.isfile("gamesavedata.csv"):
        pass
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
            # Declare new nested dictionary names from the CSV file
            dictionary[name] = {
                "scoreAddition": addScore,
                "scoreSubtraction": subtScore,
                "scoreMultiplication": multScore,
                "scoreDivision": divScore
            }


# Method to check if a username is already in the dictionary.
# This method is called at the beginning of the program when
# the user enters their name to see if they have played before.
def CheckIfNameInDictionary(name):
    names = list(dictionary.keys())
    try:
        index = names.index(name)
    except ValueError:
        return False
    return True


# This method generates a new user and writes it the CSV file.
# This method is called at the beginning of runtime if a username
# does not exist when the user enters their name.
def GenerateNewUser(name):
    data = [name, "None", "None", "None", "None"]
    with open("gamesavedata.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow(data)


# Simple method that returns a list of user data by accessing the dictionary and using
# the username as a key.
def GetUserData(name):
    startup()
    data = list(dictionary[name].values())
    return data


# Here's the beast...
# When calling this method, we need three arguments: the username, the math operation,
# and the user's score.
def ScoreHandling(name, operation, score):
    # Here, we declare a temporary dictionary and access the nested dictionary and
    # put it in this new one. This is for ease of access, mainly so that I didn't have
    # to type things like dictionary.get(name).get("something"), which would get
    # very complicated quickly. It was a lot easier to use this tempDictionary to
    # access that information.
    tempDictionary = dictionary.get(name)

    # Here's the actual "score handling" aspect of the method.
    # Here, we first check to see what operation was passed as an argument.
    # Then, in each branch, we first check to see if a value of "None" is in
    # the place of the score. If the value is "None," that means we can
    # automatically write whatever score was passed in, as there is no score.

    # Otherwise, if there already is a score value there, we check to see
    # if the score passed as an argument is greater than the score already there.
    # If it is, overwrite the previous score with the new one.
    if operation == 1:
        if tempDictionary.get("scoreAddition") == "None":
            dictionary[name]["scoreAddition"] = score
        elif int(tempDictionary.get("scoreAddition")) < score:
            dictionary[name]["scoreAddition"] = score
    if operation == 2:
        if tempDictionary.get("scoreSubtraction") == "None":
            dictionary[name]["scoreSubtraction"] = score
        elif int(tempDictionary.get("scoreSubtraction")) < score:
            dictionary[name]["scoreSubtraction"] = score
    if operation == 3:
        if tempDictionary.get("scoreMultiplication") == "None":
            dictionary[name]["scoreMultiplication"] = score
        elif int(tempDictionary.get("scoreMultiplication")) < score:
            dictionary[name]["scoreMultiplication"] = score
    if operation == 4:
        if tempDictionary.get("scoreDivision") == "None":
            dictionary[name]["scoreDivision"] = score
        elif int(tempDictionary.get("scoreDivision")) < score:
            dictionary[name]["scoreDivision"] = score

    # Once we have checked the user score, we can open the save file and
    # write to it accordingly.
    with open("gamesavedata.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(header)

        for key in dictionary:
            scoreAddition = dictionary.get(key).get("scoreAddition")
            scoreSubtraction = dictionary.get(key).get("scoreSubtraction")
            scoreMultiplication = dictionary.get(key).get("scoreMultiplication")
            scoreDivision = dictionary.get(key).get("scoreDivision")

            row = [key, scoreAddition, scoreSubtraction, scoreMultiplication, scoreDivision]

            writer.writerow(row)

    startup()


# Simple method to clear all save data.
def ClearSaveData():
    with open("gamesavedata.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(header)
    startup()


# Call the startup method, this is called at the start of runtime
startup()
