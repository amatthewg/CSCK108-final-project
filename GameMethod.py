import random
import time
import datetime


# This file houses the dedicated method to run each individual math game.
# This is the meat and potatoes of this program.
def mathGame(operation, difficultyLevel):
    # First, declare the finalOperation variable. This allows me to pass the number
    # rather than the word as an argument to this method, which makes it a lot
    # easier to call the method.
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
    multLevel2 = [10, 25]
    multLevel3 = [25, 100]
    multLevel4 = [100, 500]
    multLevel5 = [500, 1000]
    # ***********DIVISION**************
    # Division here is a bit different because the random number generator can't reliably generate numbers that divide
    # well, so I have to manually generate numbers to multiply and then display them as a division problem.
    divLevel1 = [1, 10]
    divLevel2 = [1, 20]
    divLevel3 = [1, 30]
    divLevel4 = [1, 40]
    divLevel5 = [1, 50]

    # Display ready message and countdown
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

    # Initialize needed score variables
    numQuestionsDisplayed = 0
    numCorrectAnswers = 0

    # Initialize a list called wrongAnswers,
    # this will be a list that is appended each time a user enters a wrong answer
    # so that it can be displayed to them at the end.
    wrongAnswers = []

    # Here is the timer logic. We use the time.time() method to get the time in seconds
    # since the Epoch, and then cast that as an integer because it comes as a huge decimal
    # by default. Then, declare an endTime variable that is just the startTime plus
    # 60 seconds.
    startTime = time.time()
    startTime = int(startTime)
    endTime = startTime + 60

    # Initialize three "warning" variables. These will be used to check
    # what the time is and display time warnings accordingly.
    warning45 = startTime + 15
    warning30 = startTime + 30
    warning15 = startTime + 45

    # Initialize three boolean values. These are used so that each time
    # warning is displayed only once.
    displayed45 = False
    displayed30 = False
    displayed15 = False

    # This is the big while loop that runs everything.
    # The loop first checks to see that the current time
    # does not exceed the previously declared endTime variable.
    while int(time.time()) <= endTime:

        # Check the time and display time warnings
        if time.time() >= warning45 and not displayed45:
            print("45 seconds remaining...")
            displayed45 = True
        elif time.time() >= warning30 and not displayed30:
            print("30 seconds remaining...")
            displayed30 = True
        elif time.time() >= warning15 and not displayed15:
            print("15 seconds remaining...")
            displayed15 = True

        # The below branch is roughly the same for each individual operation.
        # Essentially, find out what operation is being used, and generate
        # random numbers based on the difficulty level.
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

            # Actual math logic here
            # Make the equation and display it, get the user's answer, and check to see if it's correct.
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
                # Here's where the wrongAnswers list is utilized. When the user enters a wrong answer,
                # we make a new sentence that holds the correct answer, and append it to the wrongAnswers list.
                sentence = f"{firstNum} + {secondNum} equals {equation}, not {userAnswer}"
                wrongAnswers.append(sentence)
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

                # First, generate two random numbers from set ranges,
                # then multiply them together to get the answer. We can
                # then use the multiplication to display a division problem.
                firstNum = random.randint(divLevel1[0], divLevel1[1])
                secondNum = random.randint(divLevel1[0], divLevel1[1])
            elif difficultyLevel == 2:
                firstNum = random.randint(divLevel2[0], divLevel2[1])
                secondNum = random.randint(divLevel2[0], divLevel2[1])

            elif difficultyLevel == 3:
                firstNum = random.randint(divLevel3[0], divLevel3[1])
                secondNum = random.randint(divLevel3[0], divLevel3[1])

            elif difficultyLevel == 4:
                firstNum = random.randint(divLevel4[0], divLevel4[1])
                secondNum = random.randint(divLevel4[0], divLevel4[1])

            elif difficultyLevel == 5:
                firstNum = random.randint(divLevel5[0], divLevel5[1])
                secondNum = random.randint(divLevel5[0], divLevel5[1])

            firstEquation = firstNum * secondNum

            equation = firstEquation
            equation = int(equation)
            print(f"{firstEquation} / {secondNum}", end='')
            userAnswer = input()
            try:
                userAnswer = int(userAnswer)
            except:
                pass
            if userAnswer == firstNum:
                numCorrectAnswers += 1

            else:
                sentence = f"{firstEquation} / {secondNum} equals {equation}, not {userAnswer}"
                wrongAnswers.append(sentence)

        # At the end of each loop iteration, we must check to see if the time already expired. This
        # is because we are using an input() call inside the while loop, which means the entire program
        # is pausing at that point while waiting for the user's input. This means that if we didn't do this
        # check below, the user could sit there and not input anything, allowing the timer to run past
        # its allotted time, and it would break everything. So, once we get the user's input, we must
        # check to see if the time expired already. If it did, we reject the user's final answer.
        if int(time.time()) > endTime:
            time.sleep(1.5)  # adding in these sleep calls to make the outputs more readable for the user
            print("Your final answer was rejected because the time already expired!")
            time.sleep(1.5)
            numQuestionsDisplayed += 1
        else:
            numQuestionsDisplayed += 1

    # Once finished, display the total answers displayed and correct answers.
    print("FINISHED!")
    time.sleep(1.5)
    print(f"Total questions displayed: {numQuestionsDisplayed}")
    time.sleep(1.5)
    print(f"Questions answered correctly: {numCorrectAnswers}")
    time.sleep(1.5)

    # Here, we display all the user's incorrect answers.
    # If no incorrect answers, say that.
    if len(wrongAnswers) == 0:
        print("No incorrect answers!")
    elif len(wrongAnswers) <= 30:
        print("Incorrect answers:")
        # Loop through wrongAnswers
        for x in wrongAnswers:
            print(x)
            time.sleep(0.5)
    elif len(wrongAnswers) > 30:
        print("Incorrect answers:")
        for x in wrongAnswers:
            print(x)
    time.sleep(1.5)
    print(f"Total score: {numCorrectAnswers * difficultyLevel}")

    # Finally, return the user's score.
    return numCorrectAnswers * difficultyLevel
