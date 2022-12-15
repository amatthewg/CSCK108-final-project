import TextGroup as txt
import UserDataHandling as saveFile
import GameMethod
import time

# Aiden Grimsey
# CSC K 108
# 12/15/22
# Final project

# Startup, where we get the user's name
userName = input("Enter your name: ")
print(f"Welcome, {userName}!")

# Check if user has played before
if saveFile.CheckIfNameInDictionary(userName) == True:
    print("It looks like you have played before.")
    time.sleep(1.5)
# If they haven't played before, generate a new spot in the CSV for them
else:
    print("It looks like this is your first time playing.")
    print("Generating your user save data...")
    saveFile.GenerateNewUser(userName)
    time.sleep(1.5)


# Declare text variables from text file

mainMenu = txt.mainMenu
operationsMenu = txt.operationsMenu
difficultyPrompt = txt.difficultyLevelPrompt

# Method to display startup menu

def displayStartMenu():
    print(mainMenu)

    # Get user input, reject if invalid
    while True:
        try:
            firstChoice = int(input())
            if firstChoice > 3 or firstChoice < 1:
                print("Not a valid choice!")
                time.sleep(1.5)
                continue
        except ValueError:
            print("Not a valid choice!")
            time.sleep(1.5)
            continue
        else:
            break

    # Handle user's first choice
    if firstChoice == 1:
        print(operationsMenu)
        while True:
            try:
                secondChoice = int(input())
                if secondChoice > 4 or secondChoice < 1:
                    print("Not a valid choice!")
                    time.sleep(1.5)
                    continue
            except ValueError:
                print("Not a valid choice!")
                continue
            else:
                break
        print(difficultyPrompt)
        while True:
            try:
                difficultyChoice = int(input())
                if difficultyChoice > 5 or difficultyChoice < 1:
                    print("Not a valid choice!")
                    time.sleep(1.5)
                    continue
            except ValueError:
                print("Not a valid choice!")
                continue
            else:
                break
        saveFile.ScoreHandling(userName, secondChoice, GameMethod.mathGame(secondChoice, difficultyChoice))
        displayStartMenu()
    if firstChoice == 2:
        print("Getting your scores...")
        time.sleep(1.5)
        userData = saveFile.GetUserData(userName)

        print(f"Addition score: {userData[0]}")
        print(f"Subtraction score: {userData[1]}")
        print(f"Multiplication score: {userData[2]}")
        print(f"Division score: {userData[3]}")
        time.sleep(1.5)
        displayStartMenu()
    if firstChoice == 3:
        print("Thanks for playing!")
        time.sleep(2)
        quit()
    if firstChoice > 3:
        print("Not a valid choice!")
        time.sleep(1.5)
        displayStartMenu()


# Call main function, this is all that's needed as everything
# else uses recursion to call itself during runtime.
if __name__ == "__main__":
    displayStartMenu()