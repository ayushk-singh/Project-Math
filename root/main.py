# Rich is a python library which help to style output

from rich import prompt
from rich import style
from rich.style import Style
from calculator.calculator import calculator
from rich.console import Console 
from rich.markdown import Markdown
from sequence_series.ap import mainSqSeries
from rich.prompt import Prompt

console = Console()  # creating a console object


# initilizing x = y for while loop
x = "y"

while x == "y":

    def welcome():
        message = """# WELCOME TO MATH-LAB

        What operation do you want to perform:
        1. Sequence and Series
        2. Complex Number
        3. Basic Calculator
        4. Finding the value of trignometric ratio

        Please select operation from '1' '2' '3' or '4'
        """
        resultMsg = Markdown(message)
        console.print(resultMsg)
    

    welcome()



    def selection():
        choice = input(">> Enter your choice: ")
        print("")
        console.rule("")
        print("")

        if choice == '1':
            print("")         # these print are written to give space between line
            mainSqSeries()
        elif choice == '2':
            print("")
            print("Working2")
        elif choice == '3':
            print("")
            calculator()
        elif choice == '4':
            print("")
            print("Working4")
        else:
            console.print("Please Enter a valid input", style="Red on black")

    selection()
    print("")
    x = Prompt.ask("🚀 [bold red]Enter y to continue or any key to exit: [/bold red]")
    console.print("Thanks for using Math Lab 💻",justify="center",style="bold underline green")








