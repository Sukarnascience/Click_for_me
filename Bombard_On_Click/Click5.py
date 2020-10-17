#Please Don't Forget to read README.md otherwise you will fall in trouble
import pyautogui
import time

X_Axis=int(input("Enter X axis:-"))
Y_Axis=int(input("Enter Y axis:-"))

print("It Will Start Bombarding in 10sec")
print("Clear the place where it wants to click")
time.sleep(10)
print("u have more 5sec extra for clearing the place of clicking")
time.sleep(5)
print("starting")
while True:
    pyautogui.leftClick(x=X_Axis,y=Y_Axis)
