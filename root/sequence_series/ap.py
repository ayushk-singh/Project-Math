import math  #unused
from sequence_series.gp import gp_last_term
from sequence_series.gp import gp_sum
from rich import console
from rich.console import Console

console = Console()

#Code for calculating the first and last term of any AP.

# Let a=First Term of the AP
#And l=Last term of the GP
#d=common difference
#n=number of terms
#We know Formula of AP, an=a+(n-1)d



def mainSqSeries(): 
    console.print("How may I help you!! :heart:",justify="center",style="bold underline yellow")
    console.print("")
    console.print("Chosse which operation you want to do :")
    console.print('''
    1. Find number of terms when First and last term of AP is given.
    2. Find last term when first term, number of term and common ratio given.
    3. Find the sum of nth term of GP.    
    ''')

    selectOption = input("Please select one of the option :")

    #Finding number of terms of a AP

    def number_of_terms():    
        a=float(input("Enter the first term of the AP :"))
        l=float(input("Enter the last :"))
        d=float(input("Enter the common difference :"))





        difference_of_1st_and_last_term=(l-a)
        number_of_terms_minus_1=difference_of_1st_and_last_term/d
        
        if difference_of_1st_and_last_term%d==0:
           number_of_terms_answer=number_of_terms_minus_1+1
           print("The number of terms in the AP is :",number_of_terms_answer)
        else:
            print("Wrong input provided")
            print("It is not an AP.")

        
    #Sum of n number of terms 
    
    def sum_of_number_of_terms():
        a=float(input("Enter the first term of the AP :"))
        l=float(input("Enter the last :"))
        n=float(input("Enter the number of terms of the A.P :"))


    #Formula for sum = n/2(a+l)

        ndividedby2=n/2
        sum_answer=ndividedby2*(a+l)
        print("The sum number of terms in the AP is :", sum_answer)
                                                                              


# ========================IF STATEMENT FOR EXECUTION OF CODE=========================

    if (selectOption == '1'):
        number_of_terms()
    elif (selectOption == '2'):
        gp_last_term()
    elif (selectOption == '3'):
        gp_sum()
    elif (selectOption == '4'):
        sum_of_number_of_terms()


#==================IGNORE=========================


#All the defined variables in this file are:
#selectOption = input("Please select one of the option :")
#a=float(input("Enter the first term of the AP :"))
#l=float(input("Enter the last :"))
#d=float(input("Enter the common difference :"))
#difference_of_1st_and_last_term=(l-a)
#number_of_terms_minus_1=difference_of_1st_and_last_term/d
#number_of_terms_answer=number_of_terms_minus_1+1
#ndividedby2=n/2
#sum_answer=ndividedby2*(a+l)
#==================xXx=============================