import pyautogui - #pip install pyautogui
user_input = 0
def user():
    global user_input
    user_input = int(input("How many times do you want to refresh? "))

try:
    user()
    wrong = False
except:
    wrong = True
    print("Wrong input! Please enter a number")
    while wrong == False:
        user()

# Setting a limit
while user_input > 25:
    print("Please enter a Number below 25".)
    user()

# Start + D - Dextop
pyautogui.keyDown('win')
pyautogui.keyDown('d')
pyautogui.keyUp('win')
pyautogui.keyUp('d')




for v in range(user_input):

    # Shift + F10 - Menue
    pyautogui.keyDown('shift')
    pyautogui.keyDown('f10')
    pyautogui.keyUp('f10')
    pyautogui.keyUp('shift')

    # Down arrow three times
    pyautogui.press('down', presses=3)

    # Enter
    pyautogui.press('enter')