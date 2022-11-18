import random
import time
import datetime
# This file houses the dedicated methods to run each individual math game

def additionGame(difficultyLevel):
    # for level 1, give numbers between 1-10 to add, give 1 pt per correct ans
    # for lv 2, give nums between 10-25 to add, give 2 pt per correct ans
    # for lv 3, give nums between 25 and 100, give 3 pt per correct ans
    # for lv 4, give nums between 100 and 500 to add, give 4 pt per correct ans
    # for lv 5, give nums between 500 and 1000, give 5 per ans





    if difficultyLevel == 1:
        numQuestionsDisplayed = 0
        numCorrectAnswers = 0

        startTime = time.time()
        startTime = int(startTime)
        endTime = startTime + 60

        i = 60
        while int(time.time()) != endTime:
            if i <= 45:
                print(f"{i} seconds remaining...")
            elif i <= 30:
                print(f"{i} seconds remaining...")
            elif i <= 15:
                print(f"{i} seconds remaining...")
            time.sleep(1)

            # placeholder: user input() line will go here, to get their answer
            userInput = input() #fixme this is broken now
            # put timer has expired check after user input line
            if int(time.time()) > endTime:
                time.sleep(1.5) # adding in these sleep calls to make the outputs more readable for the user
                print("Your final answer was rejected because the time already expired!")
                time.sleep(1.5)
            else:
                pass # this will be where we increment questions displayed, etc
            i -= 1
        print("FINISHED!")
        time.sleep(1.5)
        print(f"Total questions displayed: {numQuestionsDisplayed}")
        time.sleep(1.5)
        print(f"Questions answered correctly: {numCorrectAnswers}")
        time.sleep(1.5)
        print(f"Total score: {numCorrectAnswers}") # score is the num of correct answers b/c points given is 1 per question for difficulty lvl 1




    elif difficultyLevel == 2:
        pass
    elif difficultyLevel == 3:
        pass
    elif difficultyLevel == 4:
        pass
    elif difficultyLevel == 5:
        pass

additionGame(1)