#Go to Command prompt and type "pip install PyAutoGUI"
#To install this library
import pyautogui

#give the porition of the axis where you want to click
X_Axis=int(input("Enter X axis:-"))
Y_Axis=int(input("Enter Y axis:-"))

while True:
    Start=input("Lets Start Clicking press [s] key:-")
    print("To stop the code in between press Ctrl-C")
    if(Start=='s' or Start=='S'):
        print("Starting")  
        try:
            while True:
                pyautogui.leftClick(x=X_Axis,y=Y_Axis)
                print("clicked")
        except KeyboardInterrupt:
            pass
        print("Stopped working")
    else:
        print("Sorry Fail to start press again [s] key")
        continue
