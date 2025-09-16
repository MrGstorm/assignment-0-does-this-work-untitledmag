###############################################################################
#  Program Name   : Assignment 1: Madlib
#  Author         : Manreet Singh
#  Date           : 2025-09-16
#  Class/Section  : ICS3U, Section 01
#  Description    : This programs gets data from user by using input variables and prints it out in console. Includes error handeling.
#  Input          : Name Of Places, Duration, Adjective, Time
#  Output         : A program which outputs all the data entered by user in a paragraph.
###############################################################################

# import some dependecies to make it more interesting
from colorama import Fore, Style
import asyncio
from datetime import datetime

#create coroutine main function
async def main():
    print(f'{Fore.BLUE}Welcome to Manreet\'s MadLib{Style.RESET_ALL}\n')
    try:
        #Get Name Of 
        place = input(
            'Enter a name of place: '
        )
        #Get time
        time = int(
            input(
                'Enter a duration which will be minutes i.e 15: '
            )
        )
        #Get the name of second place
        secondPlace = input(
            'Enter the name of second place: '
        )
        #Get Adjective
        adjective = input(
            'Enter an adjective: '
        )
        #Get the second time
        secondTime = input(
            'Enter the second time (in 24hr format) ie {timehour}: '.format(timehour=datetime.now().hour)
        )
        #Print it all together
        print(
            f"\n{Fore.GREEN}"
            "This weekend, I am planning to go to {place} where I can spend around {time} minutes.\n".format(place=place, time=time),
            "I heard there is a {secondPlace} where I can eat and enjoy. Also there's a waterfall which is very {adjective}.\n".format(secondPlace=secondPlace, adjective=adjective),
            "I will come home around {secondTime}.".format(secondTime=secondTime),
            f"\n{Style.RESET_ALL}"
        )
    #Ignores the KeyboardInterrupt exception as we are already handeling it below.
    except KeyboardInterrupt:
        pass
    #Asks user to enter correct integer values
    except ValueError:
        print(f"\n{Fore.RED}Make sure to enter correct integer duration!!{Style.RESET_ALL}")
    #Prints Exception
    except Exception as e:
        print(f"\n{Fore.RED}An error occured while processing this request : {e}{Style.RESET_ALL}")
try:
    #runs the coroutine function
    asyncio.run(main())
#Exits if we press `CTRL + C`
except KeyboardInterrupt:
    print(f"\n{Fore.RED}Script closed manually!!{Style.RESET_ALL}")