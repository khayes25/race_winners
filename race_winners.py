"""
@author: Keon Hayes
"""

name1 = input("Please enter the name of runner #1: ")                               #Prompts user for runner #1's name.
time1 = float(input("Please enter " + name1 + "'s finish time (in minutes): "))     #Prompts for their time.
while time1 <= 0 :                                                                  #Has to be more than 0.
    print("Invalid entry. Try again.")                                              #If it isn't, display error message.
    time1 = float(input("Please enter " + name1 + "'s finish time (in minutes): ")) #Prompts for runner #1's time again.

name2 = input("Please enter the name of runner #2: ")                               #Prompts user for runner #2's name.
time2 = float(input("Please enter " + name2 + "'s finish time (in minutes): "))     #Prompts for their time.
while time2 <= 0 :                                                                  #Has to be more than 0.
    print("Invalid entry. Try again.")                                              #If it isn't, display error message.
    time2 = float(input("Please enter " + name2 + "'s finish time (in minutes): ")) #Prompts for runner #2's time again.

name3 = input("Please enter the name of runner #3: ")                               #Prompts user for runner #3's name.
time3 = float(input("Please enter " + name3 + "'s finish time (in minutes): "))     #Prompts for their time.
while time3 <= 0 :                                                                  #Has to be more than 0.
    print("Invalid entry. Try again.")                                              #If it isn't, display error message.
    time3 = float(input("Please enter " + name3 + "'s finish time (in minutes): ")) #Prompts for runner #3's time again.

if time1 < time2 and time1 < time3 :                                                #To win Gold, runner #1's time must be less than both runner #2 and runner #3.                                            
    print("Gold Medal Winner:", name1)                                              #If so, print that runner #1 won Gold.
if time2 < time1 and time2 < time3 :                                                #To win Gold, runner #2's time must be less than both runner #1 and runner #3.                                           
    print("Gold Medal Winner:", name2)                                              #If so, print that runner #2 won Gold.
if time3 < time1 and time3 < time2 :                                                #To win Gold, runner #3's time must be less than both runner #1 and runner #2.
    print("Gold Medal Winner:", name3)                                              #If so, print that runner #3 won Gold.

if time2 < time1 and time1 < time3 or time3 < time1 and time1 < time2 :             #To win Silver, runner #1's time must be more than #2's and less than #3's, or more than #3's and less than #2's.
    print("Silver Medal Winner:", name1)                                            #If so, print that runner #1 won Silver.
if time1 < time2 and  time2 < time3 or time3 < time2 and time2 < time1 :            #To win Silver, runner #2's time must be more than #1's and less than #3's, or more than #3's and less than #1's.                         
    print("Silver Medal Winner:", name2)                                            #If so, print that runner #2 won Silver.
if time1 < time3 and time3 < time2 or time2 < time3 and time3 < time1 :             #To win Silver, runner #3's time must be more than #1's and less than #2's, or more than #2's and less than #1's.
    print("Silver Medal Winner:", name3)                                            #If so, print that runner #3 won Silver.

if time1 > time2 and time1 > time3 :                                                #To win Bronze, runner #1's time must be more than both runner #2 and runner #3.                                                                                 
    print("Bronze Medal Winner:", name1)                                            #If so, print that runner #1 won Bronze.
if time2 > time1 and time2 > time3 :                                                #To win Bronze, runner #2's time must be more than both runner #1 and runner #3.
    print("Bronze Medal Winner:", name2)                                            #If so, print that runner #2 won Bronze.
if time3 > time1 and time3 > time2 :                                                #To win Bronze, runner #3's time must be more than both runner #1 and runner #2.
    print("Bronze Medal Winner:", name3)                                            #If so, print that runner #3 won Bronze.
