
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 01:29:17 2018

@author: Chris Otter
"""
import pymsgbox

#variables for sales and county tax
s = 0.025 #sales tax
c = 0.05 #county tax

#calculate function
def calculate():
        # asks the user to input the amount of the purchase
        price = float(pymsgbox.prompt('Please input the amount of the purchase to calculate the total cost for the item after taxes:', 'Price of Item'))
        total = float(price * s * c + price)
        #calculates full price with taxes and outputs it
        pymsgbox.alert("Your new price is: $" + str(total))
        "OK"
        return again()

#loop function
def again():
    while True:
        #asks to check price with taxes
        again = pymsgbox.confirm('Check the price of another item after taxes?', 'Price Check', ["Yes", 'No'])
        if again not in {"Yes","No"}:
            print("please enter valid input")               
        elif again == "No":
            return pymsgbox.alert("Thank you for using my calculator!")
        elif again == "Yes":
            # call function to start the calc again
            return calculate()
calculate()





