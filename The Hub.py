#The Hub. Make sure to pip install, donwload webdriver from here:                                         and save webdriver and file in same place.
from time import sleep
from selenium import webdriver
import math
import random
import requests
from datetime import datetime


i = 1

print('''Hi! Welcome to The Hub!''')
while True:
    hubselect = input('''\nSelect a option : 
    1 = Waether Machine
    2 = Time Waster
    3 = Calculator
    4 = Square and square root
    5 = NumbAkinator
    6 = Number Guessing Game
    7 = Crypto Prices'
    8 = Dice
    : ''')

    if hubselect == '1':
        driver = webdriver.Chrome()
        print('Welcome to Waether! This is an automated GUI that gives you the weather!')
        city = str(input("Enter the name of the city you want the weather forecast for: ")).replace(" ","-")

        try:
            driver.get("https://www.weather-forecast.com/locations/"+city+"/forecasts/latest")
            print(driver.find_elements_by_class_name("b-forecast__table-description-content")[0].text)
            sleep(0.25)
            print('''Thanks for using Waether

''')
        except:
                print("Something went wrong")
                

    if hubselect == '2':
        i = 1
        

        print('How much time do you want to waste?') #ask for Wastetime
        myWastetime = input()
        limittime = int(myWastetime)
        while i <= limittime:
            print(i)
            sleep(1)
            i = i+1
        print('You have wasted ' + str(myWastetime) + ' seconds of your life.')
        sleep(1)
        while True:
            print('Do you want to waste more time?') #ask for Yesno
            myYesno = input()
            if myYesno == 'Yes' or myYesno == 'YES' or myYesno == 'yes':
                print('Then how much time do you want to waste?') #ask for Wastetime2
                i = 1
                myWastetime2 = input()
                limittime2 = int(myWastetime2)
                while i <= limittime2:
                    print(i)
                    sleep(1)
                    i = i+1
                print('You have wasted ' + str(myWastetime2) + ' more seconds of your life.')
            else:
                endgame = str(i)
                print('Then, thank you for wasting some time!')
                sleep(0.9)
                print('''You have wasted approximately ''' + myWastetime + ''' seconds of your life today

''')
                break
            break
        
    



                       

                
    


    if hubselect == '3':
            print('Welcome to PyCal!')
            opr = str(input('Give me an operator.'))
            firstnum = float(input('Give me the first number.'))
            secnum = float(input('Give me the second number'))
            if opr == '/':
                print(firstnum / secnum)
                print('Thanks for using PyCal')
                
                
            if opr == '*':
                print(firstnum * secnum)
                print('Thanks for using PyCal')
                
            if opr == '+':
                print(firstnum + secnum)
                print('Thanks for using PyCal')
                
            if opr == '-':
                print(firstnum - secnum)
                print('Thanks for using PyCal')
                
        
           
        
    
            
        
    if hubselect == '4':
        print('Welcome to the Square Root/Square calculator extension of PyCal!')
        xnum = int(input('Give me a number to square or square root.'))
        operator = str(input('Give me the operator! sqrt for Square Root and sqr for Square'))
        if operator == 'sqrt':
            xnumsqrt = math.sqrt(xnum)
            print('The Answer is...')
            sleep(0.25)
            print(xnumsqrt)
            sleep(1)
            
        if operator == 'sqr':
            xnumsqr = xnum * xnum
            print('The Answer is...')
            print(xnumsqr)
            sleep(1)
        print('''Thanks for using the Square/Square Root extension of Pycal.

''')
                   
        
        
        
        
    if hubselect == '5':
        #Computer guesses number game
        from time import sleep
        print('Hello! Welcome to Number Akinator! Here, you are to pick a number from 1 to 63(including 63)')
        print ('If your number is in one of the lists, type in "yes" ')
        sleep(3)
        print ('But if your number isn\'t in the list, type "no" ')
        sleep(3)
        print ('Ok! let\'s go!')

        myAnswer = 0
        firstans = input('1, 3, 5, 7, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63')
        if firstans == 'yes':
            myAnswer = myAnswer + 1
        sleep(2)
        secans = input('2 3 6 7 10 11 14 15 18 19 22  23 26 27 30 31 34 35 38 39 42 43 46 47 50 51 54 55 58 59 62 63')
        if secans == 'yes':
            myAnswer = myAnswer + 2
        sleep(2)
        thirdans = input('4 5 6 7 12 13 14 15 20 21 22 23 28 29 30 31 36 37 38 39  44 45 46 47 52 53 54 55 60 61 62 63')
        if thirdans == 'yes':
            myAnswer = myAnswer + 4
        sleep(2)
        fourthans = input('8 9 10 11 12 13 14 15 24 25 26 27 28 29 30 31 40 41 42 43 44 45 46 47  56 57 58 59 60 61 62 63')
        if fourthans == 'yes':
            myAnswer = myAnswer + 8
        sleep(2)
        fifthans = input('16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63')
        if fifthans == 'yes':
            myAnswer = myAnswer + 16
        sleep(2)
        sixthans = input('32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63')
        if sixthans == 'yes':
            myAnswer = myAnswer + 32
        sleep(2)
        print('Your number was...')
        sleep(1.25)
        print(myAnswer)
        sleep(0.25)
        print('''Thank you for using NumbAkinator!

''')
    if hubselect == '6':
        import random

        amountGuess = 0

        from time import sleep

        hiddenNumber = random.randrange(1, 51)
        #answer

        print('Welcome to the Number Guessing Game!')
        sleep(1)
        print('The aim of the game is to guess a number between 1 and 50.')
        sleep(2)
        print('But not any random number, you have to guess the number I\'m thinking of.')
        sleep(2.5)
        print('You will only get five guesses, so use them wisely.')
        sleep(1)

        guess = int(input('Now, please enter your guess:'))

        amountGuess = amountGuess +1

        if guess == hiddenNumber:
            print('')
            print('Calculating...')
            sleep(0.8)
            print('You got it!')
            sleep(0.8)
            print('')
            print('Thank you for playing!')
            sleep(2)
            
            while True:
                sleep(1)
                break
        elif guess < hiddenNumber:
            print('')
            print('Calculating...')
            sleep(0.8)
            print('The number I\'m thinking of is higher.')
        else:
            print('')
            print('Calculating...')
            sleep(0.8)
            print('The number I\'m thinking of is lower.')

        while amountGuess <= 3:
            guess2 = int(input('Now, please enter another guess:'))

            amountGuess = amountGuess +1

            if guess2 == hiddenNumber:
                print('')
                print('Calculating...')
                sleep(0.8)
                print('You got it!')
                sleep(0.8)
                print('')
                print('Thank you for playing!')
                sleep(2)
                
                while True:
                    
                    sleep(1)
                    break
            elif guess2 < hiddenNumber:
                print('')
                print('Calculating...')
                sleep(0.8)
                print('The number I\'m thinking of is higher.')
            else:
                print('')
                print('Calculating...')
                sleep(0.8)
                print('The number I\'m thinking of is lower.')

        guess3 = int(input('Now, please enter your final guess:'))

        if guess3 == hiddenNumber:
            print('')
            print('Calculating...')
            sleep(0.8)
            print('You got it!')
            sleep(0.8)
            print('')
            print('Thank you for playing!')
            sleep(2)
            
            while True:
                
                sleep(1)
                break
        elif guess3 < hiddenNumber:
            print('')
            print('Calculating...')
            sleep(0.8)
            print('The number I\'m thinking of is higher.')
            print('Good try! The number was...')
            sleep(1)
            print(hiddenNumber)
        else:
            print('')
            print('Calculating...')
            sleep(0.8)
            print("The number I'm thinking of is lower.")
            print('Good try! The number was...')
            sleep(1)
            print(hiddenNumber)
            
        print('''
        Thank you for playing this game!''') #ask for Endless
    if hubselect == 'credits':
        print('''
Idea: Anthony Pi
Coder, implementer: Shashank Rangaraj, Anthony Pi
Code-Giver: Anthony Pi
Betatesters: William Lee, Benjamin Chambers
Random Guy who shouted memes in my face: Yuhoong 'Yeethong' How.''')
        break
    
    if hubselect == '7':
        #Description: Get the current price of Bitcoin



        #Resource: 
        #1. https://realpython.com/python-bitcoin-ifttt/
        #2. https://www.saltycrane.com/blog/2008/06/how-to-get-current-date-and-time-in/

        #Import libraries
        
        #Get the URL ticker to get the .json files of the crypto currencies
        TICKER_API_URL = 'https://api.coinmarketcap.com/v1/ticker/'

        cryptoType = input('What cryptocurrency\'s price do you want? ')
        
        #Function to get the latest crypto currency price of a specific 'crypto' e.g bitcoin, litecoin, etc.
        # crypto = {bitcoin, litecoin, ethereum, ...}
        def get_latest_crypto_price( crypto ):
            response = requests.get(TICKER_API_URL+crypto)
            response_json = response.json()
            # Convert the price to a floating point number
            return float(response_json[0]['price_usd'])

        #Test the function
        get_latest_crypto_price(str(cryptoType))

        BITCOIN_PRICE_THRESHOLD = 0

        def main():
          
          #Set last_price to -1 to indicate the last price hasn't been recorded yet
          last_price = -1
          
         
          crypto = str(cryptoType)
          price = get_latest_crypto_price(str(cryptoType))
          now = datetime.now()
          now.strftime("%Y-%m-%d %H:%M")#Returns format (YYYY-mm-DDTHH:MM:SS.MS)
                
          #Check if the crypto currency price is less than your threshold
          if price < BITCOIN_PRICE_THRESHOLD:
              print('The Crypto is lower than your threshold')
                
                  #Print the price of bitcoin only if the current price is different from the last price
          if price != last_price:
              print(now.isoformat() , cryptoType,' = ',price)
              last_price = price #update last_price to be the current price
            

        main()
        sleep(2)
    
    
    if hubselect == '8':
        print('Welcome to pyDice')
        randint = random.randint(1,6)
        randint = str(randint)
        print('Your random integer is '+randint+'.')
        sleep(2)
        
    if hubselect >= '9':
        print('''Invalid Input


''')
        
