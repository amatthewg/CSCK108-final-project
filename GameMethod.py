import random
import time
import datetime


# This file houses the dedicated methods to run each individual math game

def mathGame(operation, difficultyLevel):
    # for level 1, give numbers between 1-10 to add, give 1 pt per correct ans
    # for lv 2, give nums between 10-25 to add, give 2 pt per correct ans
    # for lv 3, give nums between 25 and 100, give 3 pt per correct ans
    # for lv 4, give nums between 100 and 500 to add, give 4 pt per correct ans
    # for lv 5, give nums between 500 and 1000, give 5 per ans


    if operation == 1:
        finalOperation = "Addition"
    elif operation == 2:
        finalOperation = "Subtraction"
    elif operation == 3:
        finalOperation = "Multiplication"
    elif operation == 4:
        finalOperation = "Division"



    # These lists are to make it easier to change the random number ranges
    # ***********ADDITION**************
    additionLevel1 = [0, 10]
    additionLevel2 = [10, 25]
    additionLevel3 = [25, 100]
    additionLevel4 = [100, 500]
    additionLevel5 = [500, 1000]
    # ***********SUBTRACTION***********
    subtLevel1 = [0, 10]
    subtLevel2 = [10, 25]
    subtLevel3 = [25, 100]
    subtLevel4 = [100, 500]
    subtLevel5 = [500, 1000]
    # ***********MULTIPLICATION********
    multLevel1 = [0, 10]
    multLevel2= [10, 25]
    multLevel3 = [25, 100]
    multLevel4 = [100, 500]
    multLevel5 = [500, 1000]
    # ***********DIVISION**************
    divLevel1 = [0, 10]
    divLevel2 = [10, 25]
    divLevel3 = [25, 100]
    divLevel4 = [100, 500]
    divLevel5 = [500, 1000]


    # put ready message here
    print(f"{finalOperation} Game, Level {difficultyLevel}, {difficultyLevel} points per correct answer")
    time.sleep(2)
    print("Starting in 5...")
    time.sleep(1)
    print("Starting in 4...")
    time.sleep(1)
    print("Starting in 3...")
    time.sleep(1)
    print("Starting in 2...")
    time.sleep(1)
    print("Starting in 1...")
    time.sleep(1)

    numQuestionsDisplayed = 0
    numCorrectAnswers = 0
    wrongAnswers = []

    startTime = time.time()
    startTime = int(startTime)
    endTime = startTime + 60

    warning45 = startTime + 15
    warning30 = startTime + 30
    warning15 = startTime + 45

    displayed45 = False
    displayed30 = False
    displayed15 = False

    while int(time.time()) <= endTime:

        if time.time() >= warning45 and not displayed45:
            print("45 seconds remaining...")
            displayed45 = True
        elif time.time() >= warning30 and not displayed30:
            print("30 seconds remaining...")
            displayed30 = True
        elif time.time() >= warning15 and not displayed15:
            print("15 seconds remaining...")
            displayed15 = True

        # placeholder: user input() line will go here, to get their answer
        if finalOperation == "Addition":
            if difficultyLevel == 1:
                firstNum = random.randint(additionLevel1[0], additionLevel1[1])
                secondNum = random.randint(additionLevel1[0], additionLevel1[1])
            elif difficultyLevel == 2:
                firstNum = random.randint(additionLevel2[0], additionLevel2[1])
                secondNum = random.randint(additionLevel2[0], additionLevel2[1])
            elif difficultyLevel == 3:
                firstNum = random.randint(additionLevel3[0], additionLevel3[1])
                secondNum = random.randint(additionLevel3[0], additionLevel3[1])
            elif difficultyLevel == 4:
                firstNum = random.randint(additionLevel4[0], additionLevel4[1])
                secondNum = random.randint(additionLevel4[0], additionLevel4[1])
            elif difficultyLevel == 5:
                firstNum = random.randint(additionLevel5[0], additionLevel5[1])
                secondNum = random.randint(additionLevel5[0], additionLevel5[1])

            equation = firstNum + secondNum
            equation = int(equation)
            print(f"{firstNum} + {secondNum}", end='')
            userAnswer = input()
            try:
                userAnswer = int(userAnswer)
            except:
                pass
            if userAnswer == equation:
                numCorrectAnswers += 1

            else:
                sentence = f"{firstNum} + {secondNum} equals {equation}, not {userAnswer}"
                wrongAnswers.append(sentence)
        # put timer has expired check after user input line
        elif finalOperation == "Subtraction":
            if difficultyLevel == 1:
                firstNum = random.randint(subtLevel1[0], subtLevel1[1])
                secondNum = random.randint(subtLevel1[0], subtLevel1[1])
            elif difficultyLevel == 2:
                firstNum = random.randint(subtLevel2[0], subtLevel2[1])
                secondNum = random.randint(subtLevel2[0], subtLevel2[1])
            elif difficultyLevel == 3:
                firstNum = random.randint(subtLevel3[0], subtLevel3[1])
                secondNum = random.randint(subtLevel3[0], subtLevel3[1])
            elif difficultyLevel == 4:
                firstNum = random.randint(subtLevel4[0], subtLevel4[1])
                secondNum = random.randint(subtLevel4[0], subtLevel4[1])
            elif difficultyLevel == 5:
                firstNum = random.randint(subtLevel5[0], subtLevel5[1])
                secondNum = random.randint(subtLevel5[0], subtLevel5[1])
            equation = firstNum - secondNum
            equation = int(equation)
            print(f"{firstNum} - {secondNum}", end='')
            userAnswer = input()
            try:
                userAnswer = int(userAnswer)
            except:
                pass
            if userAnswer == equation:
                numCorrectAnswers += 1

            else:
                sentence = f"{firstNum} - {secondNum} equals {equation}, not {userAnswer}"
                wrongAnswers.append(sentence)
        elif finalOperation == "Multiplication":
            if difficultyLevel == 1:
                firstNum = random.randint(multLevel1[0], multLevel1[1])
                secondNum = random.randint(multLevel1[0], multLevel1[1])
            elif difficultyLevel == 2:
                firstNum = random.randint(multLevel2[0], multLevel2[1])
                secondNum = random.randint(multLevel2[0], multLevel2[1])
            elif difficultyLevel == 3:
                firstNum = random.randint(multLevel3[0], multLevel3[1])
                secondNum = random.randint(multLevel3[0], multLevel3[1])
            elif difficultyLevel == 4:
                firstNum = random.randint(multLevel4[0], multLevel4[1])
                secondNum = random.randint(multLevel4[0], multLevel4[1])
            elif difficultyLevel == 5:
                firstNum = random.randint(multLevel5[0], multLevel5[1])
                secondNum = random.randint(multLevel5[0], multLevel5[1])
            equation = firstNum * secondNum
            equation = int(equation)
            print(f"{firstNum} * {secondNum}", end='')
            userAnswer = input()
            try:
                userAnswer = int(userAnswer)
            except:
                pass
            if userAnswer == equation:
                numCorrectAnswers += 1

            else:
                sentence = f"{firstNum} * {secondNum} equals {equation}, not {userAnswer}"
                wrongAnswers.append(sentence)
        elif finalOperation == "Division":
            # Division will be a bit different because I want the random numbers to divide evenly,
            # I don't want a problem like 100/14 which produces a weird decimal.

            if difficultyLevel == 1:
                # Below code will be the same for each difficulty branch of division, I'll explain it once here

                # First, generate two random numbers from set ranges
                firstNum = random.randint(divLevel1[0], divLevel1[1])
                secondNum = random.randint(divLevel1[0], divLevel1[1])

                # Enter this loop which will evaluate the numbers to make sure they divide evenly,
                # otherwise regenerate them
                while True:
                    if secondNum == 0 or firstNum % secondNum != 0:
                        firstNum = random.randint(divLevel1[0], divLevel1[1])
                        secondNum = random.randint(divLevel1[0], divLevel1[1])
                        continue
                    else:
                        break
            elif difficultyLevel == 2:
                firstNum = random.randint(divLevel2[0], divLevel2[1])
                secondNum = random.randint(divLevel2[0], divLevel2[1])

                while True:
                    if secondNum == 0 or firstNum % secondNum != 0:
                        firstNum = random.randint(divLevel2[0], divLevel2[1])
                        secondNum = random.randint(divLevel2[0], divLevel2[1])
                        continue
                    else:
                        break
            elif difficultyLevel == 3:
                firstNum = random.randint(divLevel3[0], divLevel3[1])
                secondNum = random.randint(divLevel3[0], divLevel3[1])

                while True:
                    if secondNum == 0 or firstNum % secondNum != 0:
                        firstNum = random.randint(divLevel3[0], divLevel3[1])
                        secondNum = random.randint(divLevel3[0], divLevel3[1])
                        continue
                    else:
                        break
            elif difficultyLevel == 4:
                firstNum = random.randint(divLevel4[0], divLevel4[1])
                secondNum = random.randint(divLevel4[0], divLevel4[1])

                while True:
                    if secondNum == 0 or firstNum % secondNum != 0:
                        firstNum = random.randint(divLevel4[0], divLevel4[1])
                        secondNum = random.randint(divLevel4[0], divLevel4[1])
                        continue
                    else:
                        break
            elif difficultyLevel == 5:
                firstNum = random.randint(divLevel5[0], divLevel5[1])
                secondNum = random.randint(divLevel5[0], divLevel5[1])
                #fixme this doesn't work, always generates the same two numbers
                while True:
                    print(f"DEBUG first num: {firstNum}")
                    print(f"DEBUG sec num: {secondNum}")
                    if secondNum == 0 or firstNum % secondNum != 0:
                        firstNum = random.randint(divLevel5[0], divLevel5[1])
                        secondNum = random.randint(divLevel5[0], divLevel5[1])
                        continue
                    else:
                        break
            equation = firstNum / secondNum
            equation = int(equation)
            print(f"{firstNum} / {secondNum}", end='')
            userAnswer = input()
            try:
                userAnswer = int(userAnswer)
            except:
                pass
            if userAnswer == equation:
                numCorrectAnswers += 1

            else:
                sentence = f"{firstNum} / {secondNum} equals {equation}, not {userAnswer}"
                wrongAnswers.append(sentence)
        if int(time.time()) > endTime:
            time.sleep(1.5)  # adding in these sleep calls to make the outputs more readable for the user
            print("Your final answer was rejected because the time already expired!")
            time.sleep(1.5)
            numQuestionsDisplayed += 1
        else:
            numQuestionsDisplayed += 1

    print("FINISHED!")
    time.sleep(1.5)
    print(f"Total questions displayed: {numQuestionsDisplayed}")
    time.sleep(1.5)
    print(f"Questions answered correctly: {numCorrectAnswers}")
    time.sleep(1.5)

    if len(wrongAnswers) == 0:
        print("No incorrect answers!")
    elif len(wrongAnswers) <= 30:
        print("Incorrect answers:")
        for x in wrongAnswers:
            print(x)
            time.sleep(0.5)
    elif len(wrongAnswers) > 30:
        print("Incorrect answers:")
        for x in wrongAnswers:
            print(x)
    time.sleep(1.5)
    print(f"Total score: {numCorrectAnswers}")  # score is the num of correct answers b/c points given is 1 per question for difficulty lvl 1

    # todo add in checkers to evaluate actual score and return the score
    return numCorrectAnswers


