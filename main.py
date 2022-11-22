import TextGroup as txt
import UserDataHandling as saveFile
import GameMethods
# Text Variable Declarations
mainMenu = txt.mainMenu

userName = input("Enter your name: ")

if saveFile.CheckIfNameInDictionary(userName) == True:
    print(f"Welcome back, {userName}!")
else:
    print(f"Welcome, {userName}!\n"
          f"Your name does not indicate that you've played before.")

# print(saveFile.GetUserData("john")[0])
#dataList = saveFile.GetUserData("john")
print(saveFile.GetUserData("john")[0])