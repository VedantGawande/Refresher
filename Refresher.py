import pyautogui - #pip install pyautogui
# There is a default value of user_input to use in function# I put the refreshing part in a for loop of the range of user input(to Refresh as many times user said)
user_input = 0

def user():
    # I have made a function that has a global variabel user_input which takes input.
    global user_input
    user_input = int(input("How many times do you want to refresh? "))
# It takes the input again if the user inputs a string or aything else with the help of a while loop.
try:
    user()
    wrong = False
except:
    wrong = True
    print("Wrong input! Please enter a number")
    while wrong == True:
        user()

# I have also set a limit so that if user inputs large number it won't keep refreshing (you can change it)
while user_input > 25:
    print("Please enter a Number below 25".)
    user()

# With the help of pyautogui I pressed
# Start + D - Dextop
pyautogui.keyDown('win')
pyautogui.keyDown('d')
pyautogui.keyUp('win')
pyautogui.keyUp('d')



for v in range(user_input):

    # Shift + F10 - Menu
    pyautogui.keyDown('shift')
    pyautogui.keyDown('f10')
    pyautogui.keyUp('f10')
    pyautogui.keyUp('shift')
    
    # To reach refresh button and press enter -
    # Down arrow three times
    pyautogui.press('down', presses=3)

    # Enter
    pyautogui.press('enter')
