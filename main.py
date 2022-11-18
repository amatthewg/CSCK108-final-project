import TextGroup as txt
import UserDataHandling as saveFile
# Text Variable Declarations
mainMenu = txt.mainMenu

saveFile.GenerateNewUser("paul")


if saveFile.CheckIfNameInDictionary("paul"):
    print("Name exists!")
else:
    print("Name doesn't exist!")

