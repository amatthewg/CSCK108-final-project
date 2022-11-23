import TextGroup as txt
import UserDataHandling as saveFile
import GameMethods


saveFile.GenerateNewUser("paul")

print(saveFile.GetUserData("paul")[0])