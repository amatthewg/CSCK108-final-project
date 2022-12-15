import TextGroup as txt
import UserDataHandling as saveFile
import GameMethod
import time
import random

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
    # You'll see these loops all throughout the main file.
    # These are used to check to see not only if the user enters
    # a wrong menu number, but also to check and see if they enter
    # something like a word or letter, so that it doesn't throw a ValueError and
    # crash the program.
    while True:
        try:
            firstChoice = int(input())
            if firstChoice > 4 or firstChoice < 1:
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
        # This line below is actually running everything. We first call the ScoreHandling method, and we pass
        # multiple arguments to it. ScoreHandling needs three arguments: the username, the math operation,
        # and the user's score. So, we pass in userName, the math operation, and then we pass in a function as an
        # argument. We pass the mathGame method as an argument, because that method will ultimately return the user's
        # score. Once the mathGame method is complete and returns the score, everything goes over to the ScoreHandling
        # method, which handles everything accordingly.
        saveFile.ScoreHandling(userName, secondChoice, GameMethod.mathGame(secondChoice, difficultyChoice))
        displayStartMenu()
    elif firstChoice == 2:
        print("Getting your scores...")
        time.sleep(1.5)
        # Retrieve the user's scores and display them
        userData = saveFile.GetUserData(userName)

        print(f"Addition score: {userData[0]}")
        print(f"Subtraction score: {userData[1]}")
        print(f"Multiplication score: {userData[2]}")
        print(f"Division score: {userData[3]}")
        time.sleep(1.5)
        displayStartMenu()
    elif firstChoice == 3:
        # Quit the program
        print("Thanks for playing!")
        time.sleep(2)
        quit()
    elif firstChoice == 4:
        # This is the choice to clear all save data.
        # As a precaution, we generate a random number and ask the user to type it in
        # to avoid any accidental clearings of the save data.
        num = random.randint(5000, 100000)
        print("WARNING: You have chosen to clear all save data.")
        print("To continue, enter the following number. Otherwise, enter anything else:")
        print(num)

        while True:
            try:
                userNum = int(input())
            except:
                displayStartMenu()
            else:
                break
        if userNum == num:
            saveFile.ClearSaveData()
            print("Program must terminate when the save file is cleared.")
            time.sleep(1.5)
            quit()
        else:
            print("Incorrect number entered. Returning to main menu...")
            time.sleep(1.5)
            displayStartMenu()
    elif firstChoice > 4:
        print("Not a valid choice!")
        time.sleep(1.5)
        displayStartMenu()


# Call main function, this is all that's needed as everything
# else uses recursion to call itself during runtime.
if __name__ == "__main__":
    displayStartMenu()
