from rich.console import Console
from rich.markdown import Markdown
import math

#Comment
console = Console()

def angle():

    def welcome_trigo():
            message = """# WELCOME TO ANGLE CONVERTER

            What operation do you want to perform:
            1. Degree to Radian
            2. Radian to Degree

            Please select operation from '1' and '2'
            """
            resultMsg = Markdown(message)
            console.print(resultMsg)
    welcome_trigo()

    def degToRad():
        value = float(input("Enter the angle in degree: "))
        result = math.radians(value)
        print(result)

    def radToDeg():
        value1 = float(input("Enter the angle in radian: "))
        result1 = math.degrees(value1)
        print(result1)
    

    def selection_trigo():
        choice = input(">> Enter your choice: ")
        print("")
        console.rule("")
        print("")

        if choice == '1':
            print("")         # these print are written to give space between line
            degToRad()
        elif choice == '2':
            print("")
            radToDeg()
        else:
            console.print("Please Enter a valid input", style="Red on black")
    selection_trigo()
    print("")
    


angle()