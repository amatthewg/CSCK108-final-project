import time
# Grouping of texts

mainMenu = "Main Menu:\n" \
           "(1) Option one\n" \
           "(2) Option two\n" \
           "(3) Option three\n" \
           "(4) Option four\n"\
           "Enter number option: "

operationsMenu = "Choose the operation to play:\n" \
                 "(1) Addition\n" \
                 "(2) Subtraction\n" \
                 "(3) Multiplication\n" \
                 "(4) Division\n" \
                 "Enter number option: "

difficultyLevelPrompt = "Input your difficulty level (1-5):"

def displayCountdown(operation, difficultyLevel):
    print(f"Operation: {operation}, Level {difficultyLevel}")
    time.sleep(1.5)
    print("Answer as many as you can in 60 seconds!")
    time.sleep(1.5)
    i = 5
    while i > 0:
        print(f"Beginning in {i}...")
        i -= 1
        time.sleep(1)
    print("Go!")

