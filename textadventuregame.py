#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 19:26:18 2019

@author: ibidapo
"""

"""
DocString:
    
Introduction
Welcome!!! The name of the game is called Cash Flow. The goal of the game is
to increase the value of your investment and make enough money to pay off your
credit at the end of the game by investing in various asset classes.

"""

import random
from sys import exit




#Game Start
print("""
          
     Welcome!!! 
     
     The name of the game is called Cash Flow. 
     The goal of the game is to increase the value of your investment and make enough money to pay off yourcredit at the end of the game by investing in various asset classes.
     """ )

print("""\n 
      Happy Investing!!! Please input your name to get started
      """)

player_name = input('Player name: ')

print(f""" 
      {player_name}!!, good times are here. 
      Congratulations!! The bank just approved $10,000 @7% for you to invest in any asset class like stocks, private equity funds, treasury bonds, and bonds or any combination that matches your preference
      """)

investment_fund = 10000

print(f"""
      To help you understand your options {player_name}, Jane, your superb fiancial advisor will some time to explain some concepts.
      """)

input( '< Press any key to continue > \n')

print(f"""
      Hi {player_name}, I'm Jane and I'm here to shed some light on your investment options. 
      
      If you're wondering what a stock is, it is basically an investment (or asset_class) that signifies proportionate ownership in the issuing corporation. Stocks are risky but provide above normal returns on your investments.
      
      Private equity fund is an investment (or asset_class) that signifies proportionate ownership in the issuing in private companies. More risky than stocks but also provide above normal returns.
      
      You see, it is quite straight forward
      
      {'-'* 50}
      """)

input( '< Press enter to proceed > \n')

print(f"""
      Dear {player_name},
      
      In addition to the options we discussed in our last meeting. Please find outlined below your other options.

      Treasury bond is a fixed rate investment that pays certain percentage of interest based on principal principal invested. It is usually tenor is less than a year.
      Lastly a Bond is fixed rate investment that pays certain percentage of interest based on principal.The tenor is more than a year.
      
      Sincerely,
      
      Jane
      """)

#Bonds: [fixed rate investment that pays certain percentage of 
#interest based on principal. usually tenor is more than a year.]
      
input(' < Please press any key to continue >')      




     
print("""
      You have $10,000 bank given to you as a loan and running at the rate of 7% per annum. Remember you need to make enough money to pay back both principal and interest.
      
      Now, you have to decide on your first investment and how much you would like to apportion.
      
      """)

input(' < Please press any key to continue >')    

investment_fund_option_1 = input('How much would you like to invest: ')


print(f"Awesome!!! You have decided on investing {investment_fund_option_1}")


investment_fund_option_1 = int(float(f"{investment_fund_option_1}"))
    
if investment_fund_option_1 >= investment_fund:
    
    print(f""" Error!!! Please input value less than {investment_fund}""")
    
    investment_fund_option_1 = input('How much would you like to invest: ')
        
    print(f""" Error!!! Please input value less than {investment_fund}""")
    
    investment_fund_option_1 = input('How much would you like to invest: ')
else:
    print(f'You have decided to invest {investment_fund_option_1} ')

option_1 = input( """
                 
      Please type an option to invest in.
      
      A: Treasury Bonds
      B: Bonds
      C: Stocks
      D: Private Equity
      
      select A, B, C or D
      """)


three_tbonds_rate = 0.01

six_tbonds_rate = 0.02

twelve_tbonds_rate = 0.03

two_years_bonds_rate = 0.04

three_years_bonds_rate = 0.05

five_years_bonds_rate = 0.06


while True:

    option_1 = input( """
                 
      Please type an option to invest in.
      
      A: Treasury Bonds
      B: Bonds
      C: Stocks
      D: Private Equity
      
      select A, B, C or D
      """)
    
    if option_1.upper() == "A":
    
            t_bonds_option_1 = input (f"""
           Would you like to invest in 
           A: 3 months treasury bonds @ {three_tbonds_rate}
           B: 6 months treasury bonds @ {six_tbonds_rate}
           C: 12 month treasury bonds @ {twelve_tbonds_rate}
           """)
            
            if t_bonds_option_1.upper()== "A":
        
                first_interest = (3/12) * int(investment_fund_option_1) * 1/100
        
                print(f'Your expected interest in 3 months is ${first_interest}. All things being equal. ')
                break
            
            elif t_bonds_option_1.upper() == "B":
        
                first_interest = (6/12) * int(investment_fund_option_1) *2/100
        
                print(f'Your expected interest in 6 months is ${first_interest}. All things being equal.  ')
                break
            
            elif t_bonds_option_1.upper() == "C":
        
                first_interest = int(investment_fund_option_1) * 3/100
        
                print(f'Your expected interest in 6 months is ${first_interest}.All things being equal.  ')
                break
            
            else:
                print("Error!! Please select option A, B or C")
                
    
    if option_1.upper() == "B":
    
        bonds_option_1 = input (f"""
                            
           Would you like to invest in 
           A: 2 years bonds @ {two_years_bonds_rate}
           B: 3 years bonds @ {three_years_bonds_rate}
           C: 5 years bonds @ {five_years_bonds_rate}
           """)
    
        if bonds_option_1.upper()== "A":
        
            first_interest = int(investment_fund_option_1) * 4/100
        
            print(f'Your expected interest per annum is ${first_interest} for the next 2 years. All things being equal. ')
            break
        
        elif bonds_option_1.upper() == "B":
        
            first_interest = int(investment_fund_option_1) * 5/100
        
            print(f'Your expected interest per annum is is ${first_interest} for the next 3 years. All things being equal.  ')
            break
        
        elif bonds_option_1.upper() == "C":
        
            first_interest = int(investment_fund_option_1) * 6/100
        
            print(f'Your expected interest per annum is ${first_interest} for the next 5 years. All things being equal.  ')
            break
            
        else:
            print("Error!! Please select option A, B or C")
        
            bonds_option_1 = input (f"""
                            
            Would you like to invest in 
           A: 2 years bonds @ {two_years_bonds_rate}
           B: 3 years bonds @ {three_years_bonds_rate}
           C: 5 years bonds @ {five_years_bonds_rate}
           """)
    elif option_1.upper() == "C":

        print(f"""
              You have invested ${investment_fund_option_1} in the S&P index stock fund.
              """)
        SP_guess = random.randint(1,3)
        if SP_guess == 1:
            first_interest= 1/100 * investment_fund_option_1
        elif SP_guess == 2:
            first_interest = 2/100 * investment_fund_option_1
            
        elif SP_guess == 3:
            first_interest = 2.5/100 * investment_fund_option_1
        break

    elif option_1.upper() == "D":
        first_interest= 1/100 * investment_fund_option_1
        print(" You have invested ${investment_fund_option_1} in the Private equity fund.")
        break

    else:     
        print("\n Error!! Please select option A, B, C or D. ")
        continue

    
input( '< Press enter to proceed > \n')

balance_after_option_1 = investment_fund - int(float(investment_fund_option_1))

print(f"""
      Your current invested amount is ${investment_fund_option_1} and you have ${balance_after_option_1} to invest in the next round.
      
      Good Job {player_name}. Happy investing and always remember when life throws you lemon, you do what?
      
      That's right, you make lemonades.
      
      Good luck on your next round of investments!!!
      
      """)

economic_variable = random.randint(1,9)

#investment_fund_option_1 = investment_fund_option_1 + first_interest

#other variables Economic conditions

if economic_variable == 1 :
    
    print("""
          News Flash: Inflation!!!
          
          The Federal Bureau of Statistics reports a general increase in prices of goods and services.
          Typically this leads to increase in rates and stock prices might decrease or increase
          """)
elif economic_variable == 2 :
    
    print("""
          News Flash: Deflation!!!
          
          The Federal Bureau of Statistics reports a general decrease in prices of goods and services.
          Typically this leads to decrease in rates and stock prices might decrease or increase
          """)
elif economic_variable == 3 :
    
    print("""
           News Flash: Economic Meltdown !!!
          
          The Federal Bureau of Statistics reports an Economic Meltdown!!!.
          temporary disruption in economic activities which leads to rates decrease and fall in stock prices.
          """)
elif economic_variable == 4 :
    
    print("""
           News Flash: Unemployment rate: high!!!
          
          The Federal Bureau of Statistics reports an increase the Unemployment rate.
            A rise in unemployment rate leads to decrease in rate and a fall in stock prices.
          """)
    
elif economic_variable == 5 :
    
    print("""
           News Flash: Unemployment rate: low!!!
          
           The Federal Bureau of Statistics reports an decrease the Unemployment rate.
          A fall in unemployment rate leads to an increase in rate and an increase in stock prices.
          """)
    
elif economic_variable == 6 :
    
    print("""
           News Flash: GDP: lower!!!
    
          The Federal Bureau of Statistics reports a decrease in GDP.
          Gross Domestic product is the summation of all economic goods and services produced by nationals of a country. 
          A rise in GDP leads to rise in stocks and fall in rates. 
          A fall in GDP leads more likely to a fall in stock prices and a rise in rates
          """)    

elif economic_variable == 7 :
    
    print("""
           News Flash: GDP: higher!!!
          
          The Federal Bureau of Statistics reports an increase in GDP.
          Gross Domestic product is the summation of all economic goods and services produced by nationals of a country. 
          A rise in GDP leads to more likely to rise in stocks and fall in rates. 
          
          """)   
elif economic_variable == 8 :
    
    print("""
           News Flash: Fire harzard dirupts economic activities !!!
          
          The Federal Bureau of Statistics reports an environmental disruption in the economy.
          Typically this leads likely to increase in rates and stock prices might decrease or increase
          """)       
    
elif economic_variable == 9 :
    
    print("""
           News Flash: Economy: Stable!!!
          
          The Federal Bureau of Statistics reports stabiliy and no threat to current status quo
          """)   

print("economic variable: ", economic_variable)

stocks_rise_fall = random.randint(0,1)

print("stock rise or fall: ", stocks_rise_fall)

if economic_variable == 1: 

    if option_1.upper() == "A" or "B":
    
        three_tbonds_rate = three_tbonds_rate - 0.005
    
        six_tbonds_rate = six_tbonds_rate - 0.005
    
        twelve_tbonds_rate = twelve_tbonds_rate - 0.005
    
        two_years_bonds_rate = two_years_bonds_rate - 0.005
    
        three_years_bonds_rate = three_years_bonds_rate - 0.005
    
        five_years_bonds_rate = five_years_bonds_rate - 0.005
    
    elif option_1.upper() == "C" or "D":
        
        if stocks_rise_fall == 1:
            
            investment_fund_option_1 = investment_fund_option_1 * 1.20
        
            print(f"""
              Invested amount in stocks or private equity fund has increased by 20% to 
              {investment_fund_option_1}    
                 """)
        elif stocks_rise_fall == 0:
            
            investment_fund_option_1 = investment_fund_option_1 * 0.95
        
            print(f"""
              Invested amount in stocks or private equity fund has decreased by 5% to 
              {investment_fund_option_1} 
              """)

if economic_variable == 2: 

    if option_1.upper() == "A" or "B":
    
        three_tbonds_rate = three_tbonds_rate + 0.005
    
        six_tbonds_rate = six_tbonds_rate + 0.005
    
        twelve_tbonds_rate = twelve_tbonds_rate + 0.005
    
        two_years_bonds_rate = two_years_bonds_rate + 0.005
    
        three_years_bonds_rate = three_years_bonds_rate + 0.005
    
        five_years_bonds_rate = five_years_bonds_rate + 0.005
    
    elif option_1.upper() == "C" or "D":
        
        if stocks_rise_fall == 1:
            
            investment_fund_option_1 = investment_fund_option_1 * 1.20
        
            print(f"""
              Invested amount in stocks or private equity fund has increased by 20% to 
              {investment_fund_option_1}    
                 """)
        elif stocks_rise_fall == 0:
            
            investment_fund_option_1 = investment_fund_option_1 * 0.95
        
            print(f"""
              Invested amount in stocks or private equity fund has decreased by 5% to 
              {investment_fund_option_1} 
              """)           

if economic_variable == 3: 

    if option_1.upper() == "A" or "B":
    
        three_tbonds_rate = three_tbonds_rate - 0.005
    
        six_tbonds_rate = six_tbonds_rate - 0.005
    
        twelve_tbonds_rate = twelve_tbonds_rate - 0.005
    
        two_years_bonds_rate = two_years_bonds_rate - 0.005
    
        three_years_bonds_rate = hree_years_bonds_rate - 0.005
    
        five_years_bonds_rate = five_years_bonds_rate - 0.005
    
    elif option_1.upper() == "C" or "D":
        
        investment_fund_option_1 = investment_fund_option_1 * 0.95
        
        print(f"""
              Invested amount in stocks or private equity fund has decreased by 5% to 
              {investment_fund_option_1} 
              """)
if economic_variable == 4: 

    if option_1.upper() == "A" or "B":
    
        three_tbonds_rate = three_tbonds_rate - 0.005
    
        six_tbonds_rate = six_tbonds_rate - 0.005
    
        twelve_tbonds_rate = twelve_tbonds_rate - 0.005
    
        two_years_bonds_rate = two_years_bonds_rate - 0.005
    
        three_years_bonds_rate = three_years_bonds_rate - 0.005
    
        five_years_bonds_rate = five_years_bonds_rate - 0.005
        
    
    elif option_1.upper() == "C" or "D":
        
        investment_fund_option_1 = investment_fund_option_1 * 0.95
        
        print(f"""
              Invested amount in stocks or private equity fund has decreased by 5% to 
              {investment_fund_option_1_eco}
              """)

if economic_variable == 5: 

    if option_1.upper() == "A" or "B":
    
        three_tbonds_rate = three_tbonds_rate + 0.005
    
        six_tbonds_rate = six_tbonds_rate + 0.005
    
        twelve_tbonds_rate = twelve_tbonds_rate + 0.005
    
        two_years_bonds_rate = two_years_bonds_rate + 0.005
    
        three_years_bonds_rate = hree_years_bonds_rate + 0.005
    
        five_years_bonds_rate = five_years_bonds_rate + 0.005
    
    elif option_1.upper() == "C" or "D":
            
            investment_fund_option_1 = investment_fund_option_1 * 1.20
        
            print(f"""
              Invested amount in stocks or private equity fund has increased by 20% to 
              {investment_fund_option_1_eco}    
                 """)
                 
            
if economic_variable == 6: 

    if option_1.upper() == "A" or "B":
    
        three_tbonds_rate = three_tbonds_rate + 0.005
    
        six_tbonds_rate = six_tbonds_rate + 0.005
    
        twelve_tbonds_rate = twelve_tbonds_rate + 0.005
    
        two_years_bonds_rate = two_years_bonds_rate + 0.005
    
        three_years_bonds_rate = three_years_bonds_rate + 0.005
    
        five_years_bonds_rate = five_years_bonds_rate + 0.005
    
    elif option_1.upper() == "C" or "D":
        
        investment_fund_option_1 = investment_fund_option_1 * 0.95
        
        print(f"""
              Invested amount in stocks or private equity fund has decreased by 5% to 
              {investment_fund_option_1}
              """)

if economic_variable == 7: 

    if option_1.upper() == "A" or "B":
    
        three_tbonds_rate = 0.01 - 0.005
    
        six_tbonds_rate = 0.02 - 0.005
    
        twelve_tbonds_rate = 0.03 - 0.005
    
        two_years_bonds_rate = 0.04 - 0.005
    
        three_years_bonds_rate = 0.05 - 0.005
    
        five_years_bonds_rate = 0.06 - 0.005
    
    elif option_1.upper() == "C" or "D":
         
        investment_fund_option_1_eco = investment_fund_option_1 * 1.20
        
        print(f"""
              Invested amount in stocks or private equity fund has increased by 20% to 
              {investment_fund_option_1_eco}    
              """)


if economic_variable == 8: 

    if option_1.upper() == "A" or "B":
    
        three_tbonds_rate = three_tbonds_rate + 0.005
    
        six_tbonds_rate = six_tbonds_rate + 0.005
    
        twelve_tbonds_rate = twelve_tbonds_rate + 0.005
    
        two_years_bonds_rate = two_years_bonds_rate + 0.005
    
        three_years_bonds_rate = three_years_bonds_rate + 0.005
    
        five_years_bonds_rate = five_years_bonds_rate + 0.005
    
    elif option_1.upper() == "C" or "D":
        
        if stocks_rise_fall == 1:
            
            investment_fund_option_1 = investment_fund_option_1 * 1.20
        
            print(f"""
              Invested amount in stocks or private equity fund has increased by 20% to 
              {investment_fund_option_1}    
                 """)
        elif stocks_rise_fall == 0:
            
            investment_fund_option_1 = investment_fund_option_1 * 0.95
        
            print(f"""
              Invested amount in stocks or private equity fund has decreased by 5% to 
              {investment_fund_option_1_eco}
              """) 

if economic_variable == 9: 
   
    print (f"Economy is stable for now {player_name}.")
    
    
input("Press enter to continue")

#ROUND 2

print(f""" Welcome {player_name}!!! to another round of investing. I'm sure you're getting a hang of it. Jane your financial advisor will send your your account info in a moment.
      """)

input("Press enter to continue")

print(f"""
      Dear {player_name},
      
      I hope the news flash hasn't bogged you down one bit.
      
      I just want to give you an update on how you doing so far.
     
      Sincerely,
      
      Jane
       
	Stage	Amount Invested_interest earned	Investment value	Interest earned and Investment value
round 1	        a	d			
round 2	        d	f			
round 3	        a	d			
round 4	        d	f			
round 5	        a	d			
round 6	        d	f			

""")

investment_fund_option_2 = balance_after_option_1

while True:

    option_2 = input( """
                 
      Please type an option to invest in.
      
      A: Treasury Bonds
      B: Bonds
      C: Stocks
      D: Private Equity
      
      select A, B, C or D
      """)
    
    if option_2.upper() == "A":
    
            t_bonds_option_2 = input (f"""
           Would you like to invest in 
           A: 3 months treasury bonds @ {three_tbonds_rate}
           B: 6 months treasury bonds @ {six_tbonds_rate}
           C: 12 month treasury bonds @ {twelve_tbonds_rate}
           """)
            
            if t_bonds_option_2.upper()== "A":
        
                second_interest = (3/12) * int(investment_fund_option_2) * three_tbonds_rate
        
                print(f'Your expected interest in 3 months is ${second_interest}. All things being equal. ')
                break
            
            elif t_bonds_option_2.upper() == "B":
        
                second_interest = (6/12) * int(investment_fund_option_2) *2/100
        
                print(f'Your expected interest in 6 months is ${second_interest}. All things being equal.  ')
                break
            
            elif t_bonds_option_2.upper() == "C":
        
                second_interest = int(investment_fund_option_2) * 3/100
        
                print(f'Your expected interest in 6 months is ${second_interest}.All things being equal.  ')
                break
            
            else:
                print("Error!! Please select option A, B or C")
                
    
    if option_2.upper() == "B":
    
        bonds_option_2 = input (f"""
                            
           Would you like to invest in 
           A: 2 years bonds @ {two_years_bonds_rate}
           B: 3 years bonds @ {three_years_bonds_rate}
           C: 5 years bonds @ {five_years_bonds_rate}
           """)
    
        if bonds_option_2.upper()== "A":
        
            second_interest = int(investment_fund_option_2) * 4/100
        
            print(f'Your expected interest per annum is ${second_interest} for the next 2 years. All things being equal. ')
            break
        
        elif bonds_option_2.upper() == "B":
        
            first_interest = int(investment_fund_option_2) * 5/100
        
            print(f'Your expected interest per annum is is ${second_interest} for the next 3 years. All things being equal.  ')
            break
        
        elif bonds_option_2.upper() == "C":
        
            second_interest = int(investment_fund_option_2) * 6/100
        
            print(f'Your expected interest per annum is ${second_interest} for the next 5 years. All things being equal.  ')
            break
            
        else:
            print("Error!! Please select option A, B or C")
        
            bonds_option_2 = input (f"""
                            
            Would you like to invest in 
           A: 2 years bonds @ {two_years_bonds_rate}
           B: 3 years bonds @ {three_years_bonds_rate}
           C: 5 years bonds @ {five_years_bonds_rate}
           """)
            
    elif option_2.upper() == "C":

        print(f"""
              You have invested ${investment_fund_option_2} in the S&P index stock fund.
              """)
        SP_guess = random.randint(1,3)
        if SP_guess == 1:
            second_interest= 1/100 * investment_fund_option_2
        elif SP_guess == 2:
            second_interest = 1.5/100 * investment_fund_option_2
            
        elif SP_guess == 3:
            second_interest = 2/100 * investment_fund_option_2
        break

    elif option_2.upper() == "D":
    
        print(f" You have invested ${investment_fund_option_2} in the Private equity fund.")
        second_interest= 1/100
        break

    else:     
        print("\n Error!! Please select option A, B, C or D. ")
        continue

    
input( '< Press enter to proceed > \n')

balance_after_option_2 = investment_fund - investment_fund_option_1-investment_fund_option_2

print(f"""
      Your current invested amount in round one and two is  ${investment_fund_option_1} and ${investment_fund_option_2} respectively and you have ${balance_after_option_2} to invest.
      
      Good Job {player_name}. Happy investing and always remember when life throws you lemon, you do what?
      
      That's right, you make lemonades.
      
      Good luck on your next round of investments!!!
      
      """)

input("Press enter to continue")

print(f"""
      Dear {player_name},
      
      I hope the news flash hasn't bogged you down one bit.
      
      I just want to give you an update on how you doing so far.
     
      Sincerely,
      
      Jane
       
	Stage	Amount Invested_interest earned	Investment value	Interest earned and Investment value
round 1	        a	d			
round 2	        d	f			
round 3	        a	d			
round 4	        d	f			
round 5	        a	d			
round 6	        d	f	
		
    """)
print (balance_after_option_2)

total_loan_repayment = int(investment_fund) * 1.07 * 1.07

player_investment_value = investment_fund_option_1 + balance_after_option_1 +investment_fund_2 + first_interest + second_interest


if player_investment_value < total_loan_repayment:
    
    print ("Game Over!!! Would you like to try again?")
    
    exit

#STAGE 2   ROUND 3
    
else: 
    print (f" Welcome to stage 2!!! You have ${player_investment_value}!!! Keep it up.")
    
    
input("Please press enter to continue")


economic_variable = random.randint(1,9)

#investment_fund_option_1 = investment_fund_option_1 + first_interest

#other variables Economic conditions

if economic_variable == 1 :
    
    print("""
           News Flash: Inflation!!!
          
          The Federal Bureau of Statistics reports a general increase in prices of goods and services.
          Typically this leads to increase in rates and stock prices might decrease or increase
          """)
elif economic_variable == 2 :
    
    print("""
          News Flash: Deflation!!!
          
          The Federal Bureau of Statistics reports a general decrease in prices of goods and services.
          Typically this leads to decrease in rates and stock prices might decrease or increase
          """)
elif economic_variable == 3 :
    
    print("""
           News Flash: Economic Meltdown !!!
          
          The Federal Bureau of Statistics reports an Economic Meltdown!!!.
          temporary disruption in economic activities which leads to rates decrease and fall in stock prices.
          """)
elif economic_variable == 4 :
    
    print("""
           News Flash: Unemployment rate: high!!!
          
          The Federal Bureau of Statistics reports an increase the Unemployment rate.
            A rise in unemployment rate leads to decrease in rate and a fall in stock prices.
          """)
    
elif economic_variable == 5 :
    
    print("""
           News Flash: Unemployment rate: low!!!
          
           The Federal Bureau of Statistics reports an decrease the Unemployment rate.
          A fall in unemployment rate leads to an increase in rate and an increase in stock prices.
          """)
    
elif economic_variable == 6 :
    
    print("""
           News Flash: GDP: lower!!!
    
          The Federal Bureau of Statistics reports a decrease in GDP.
          Gross Domestic product is the summation of all economic goods and services produced by nationals of a country. 
          A rise in GDP leads to rise in stocks and fall in rates. 
          A fall in GDP leads more likely to a fall in stock prices and a rise in rates
          """)    

elif economic_variable == 7 :
    
    print("""
           News Flash: GDP: higher!!!
          
          The Federal Bureau of Statistics reports an increase in GDP.
          Gross Domestic product is the summation of all economic goods and services produced by nationals of a country. 
          A rise in GDP leads to more likely to rise in stocks and fall in rates. 
          
          """)   
elif economic_variable == 8 :
    
    print("""
           News Flash: Fire harzard dirupts economic activities !!!
          
          The Federal Bureau of Statistics reports an environmental disruption in the economy.
          Typically this leads likely to increase in rates and stock prices might decrease or increase
          """)       
    
elif economic_variable == 9 :
    
    print("""
           News Flash: Economy: Stable!!!
          
          The Federal Bureau of Statistics reports stabiliy and no threat to current status quo in the economy
          """)   

print("economic variable: ", economic_variable)

stocks_rise_fall = random.randint(0,1)

print("stock rise or fall: ", stocks_rise_fall)

if economic_variable == 1: 

    if option_2.upper() == "A" or "B":
    
        three_tbonds_rate = three_tbonds_rate - 0.005
    
        six_tbonds_rate = six_tbonds_rate - 0.005
    
        twelve_tbonds_rate = twelve_tbonds_rate - 0.005
    
        two_years_bonds_rate = two_years_bonds_rate - 0.005
    
        three_years_bonds_rate = three_years_bonds_rate - 0.005
    
        five_years_bonds_rate =  five_years_bonds_rate - 0.005
    
    elif option_2.upper() == "C" or "D":
        
        if stocks_rise_fall == 1:
            
            investment_fund_option_2 = investment_fund_option_2 * 1.20
        
            print(f"""
              Invested amount in stocks or private equity fund has increased by 20% to 
              {investment_fund_option_2}    
                 """)
        elif stocks_rise_fall == 0:
            
            investment_fund_option_2 = investment_fund_option_2 * 0.95
        
            print(f"""
              Invested amount in stocks or private equity fund has decreased by 5% to 
              {investment_fund_option_2} 
              """)

if economic_variable == 2: 

    if option_2.upper() == "A" or "B":
    
        three_tbonds_rate = three_tbonds_rate + 0.005
    
        six_tbonds_rate = six_tbonds_rate + 0.005
    
        twelve_tbonds_rate = twelve_tbonds_rate + 0.005
    
        two_years_bonds_rate = two_years_bonds_rate + 0.005
    
        three_years_bonds_rate = three_years_bonds_rate + 0.005
    
        five_years_bonds_rate = five_years_bonds_rate + 0.005
    
    elif option_2.upper() == "C" or "D":
        
        if stocks_rise_fall == 1:
            
            investment_fund_option_2 = investment_fund_option_2 * 1.20
        
            print(f"""
              Invested amount in stocks or private equity fund has increased by 20% to 
              {investment_fund_option_2}    
                 """)
        elif stocks_rise_fall == 0:
            
            investment_fund_option_2 = investment_fund_option_2 * 0.95
        
            print(f"""
              Invested amount in stocks or private equity fund has decreased by 5% to 
              {investment_fund_option_2} 
              """)           

if economic_variable == 3: 

    if option_2.upper() == "A" or "B":
    
        three_tbonds_rate = three_tbonds_rate - 0.005
    
        six_tbonds_rate = six_tbonds_rate - 0.005
    
        twelve_tbonds_rate = twelve_tbonds_rate - 0.005
    
        two_years_bonds_rate = two_years_bonds_rate - 0.005
    
        three_years_bonds_rate = three_years_bonds_rate - 0.005
    
        five_years_bonds_rate = five_years_bonds_rate - 0.005
    
    elif option_2.upper() == "C" or "D":
        
        investment_fund_option_2 = investment_fund_option_2 * 0.95
        
        print(f"""
              Invested amount in stocks or private equity fund has decreased by 5% to 
              {investment_fund_option_2} 
              """)
if economic_variable == 4: 

    if option_2.upper() == "A" or "B":
    
        three_tbonds_rate = three_tbonds_rate - 0.005
    
        six_tbonds_rate = six_tbonds_rate - 0.005
    
        twelve_tbonds_rate = twelve_tbonds_rate - 0.005
    
        two_years_bonds_rate = two_years_bonds_rate - 0.005
    
        three_years_bonds_rate = three_years_bonds_rate - 0.005
    
        five_years_bonds_rate = five_years_bonds_rate - 0.005
        
    
    elif option_2.upper() == "C" or "D":
        
        investment_fund_option_2 = investment_fund_option_2 * 0.95
        
        print(f"""
              Invested amount in stocks or private equity fund has decreased by 5% to 
              {investment_fund_option_2}
              """)

if economic_variable == 5: 

    if option_2.upper() == "A" or "B":
    
        three_tbonds_rate = three_tbonds_rate + 0.005
    
        six_tbonds_rate = six_tbonds_rate + 0.005
    
        twelve_tbonds_rate = twelve_tbonds_rate + 0.005
    
        two_years_bonds_rate = two_years_bonds_rate+ 0.005
    
        three_years_bonds_rate = three_years_bonds_rate + 0.005
    
        five_years_bonds_rate = five_years_bonds_rate + 0.005
    
    elif option_2.upper() == "C" or "D":
            
            investment_fund_option_2 = investment_fund_option_2 * 1.20
        
            print(f"""
              Invested amount in stocks or private equity fund has increased by 20% to 
              {investment_fund_option_2}    
                 """)
                 
            
if economic_variable == 6: 

    if option_2.upper() == "A" or "B":
    
        three_tbonds_rate = three_tbonds_rate + 0.005
    
        six_tbonds_rate = six_tbonds_rate + 0.005
    
        twelve_tbonds_rate = twelve_tbonds_rate + 0.005
    
        two_years_bonds_rate = two_years_bonds_rate + 0.005
    
        three_years_bonds_rate = three_years_bonds_rate + 0.005
    
        five_years_bonds_rate = five_years_bonds_rate+ 0.005
    
    elif option_2.upper() == "C" or "D":
        
        investment_fund_option_2 = investment_fund_option_2 * 0.95
        
        print(f"""
              Invested amount in stocks or private equity fund has decreased by 5% to 
              {investment_fund_option_2}
              """)

if economic_variable == 7: 

    if option_2.upper() == "A" or "B":
    
        three_tbonds_rate = three_tbonds_rate - 0.005
    
        six_tbonds_rate = six_tbonds_rate - 0.005
    
        twelve_tbonds_rate = twelve_tbonds_rate - 0.005
    
        two_years_bonds_rate = two_years_bonds_rate - 0.005
    
        three_years_bonds_rate = three_years_bonds_rate - 0.005
    
        five_years_bonds_rate = five_years_bonds_rate - 0.005
    
    elif option_2.upper() == "C" or "D":
         
        investment_fund_option_2 = investment_fund_option_2 * 1.20
        
        print(f"""
              Invested amount in stocks or private equity fund has increased by 20% to 
              {investment_fund_option_2}    
              """)


if economic_variable == 8: 

    if option_2.upper() == "A" or "B":
    
        three_tbonds_rate = three_tbonds_rate + 0.005
    
        six_tbonds_rate = six_tbonds_rate + 0.005
    
        twelve_tbonds_rate = welve_tbonds_rate + 0.005
    
        two_years_bonds_rate = two_years_bonds_rate + 0.005
    
        three_years_bonds_rate = three_years_bonds_rate + 0.005
    
        five_years_bonds_rate = five_years_bonds_rate + 0.005
    
    elif option_2.upper() == "C" or "D":
        
        if stocks_rise_fall == 1:
            
            investment_fund_option_2 = investment_fund_option_2 * 1.20
        
            print(f"""
              Invested amount in stocks or private equity fund has increased by 20% to 
              {investment_fund_option_2}    
                 """)
        elif stocks_rise_fall == 0:
            
            investment_fund_option_2 = investment_fund_option_2 * 0.95
        
            print(f"""
              Invested amount in stocks or private equity fund has decreased by 5% to 
              {investment_fund_option_2}
              """) 

if economic_variable == 9: 
   
    print (f"Economy is stable for now {player_name}.")
    
    
input("Press enter to continue")


investment_fund_option_3 = input(f'How much would you like to invest from ${player_investment_value},your new approved loan amount: ')


print(f"Awesome!!! You have decided on investing {investment_fund_option_3}")


investment_fund_option_3 = int(float(f"{investment_fund_option_3}"))
    
if investment_fund_option_3 >= player_investment_value:
    
    print(f""" Error!!! Please input value less than {player_investment_value}""")
    
    investment_fund_option_3 = input('How much would you like to invest: ')
        
else:
    print(f'You have decided to invest {investment_fund_option_3} ')

option_3 = input( """
                 
      Please type an option to invest in.
      
      A: Treasury Bonds
      B: Bonds
      C: Stocks
      D: Private Equity
      
      select A, B, C or D
      """)


while True:

    option_3 = input( """
                 
      Please type an option to invest in.
      
      A: Treasury Bonds
      B: Bonds
      C: Stocks
      D: Private Equity
      
      select A, B, C or D
      """)
    
    if option_3.upper() == "A":
    
            t_bonds_option_3 = input (f"""
           Would you like to invest in 
           A: 3 months treasury bonds @ {three_tbonds_rate}
           B: 6 months treasury bonds @ {six_tbonds_rate}
           C: 12 month treasury bonds @ {twelve_tbonds_rate}
           """)
            
            if t_bonds_option_3.upper()== "A":
        
                third_interest = (3/12) * int(investment_fund_option_3) * 1/100
        
                print(f'Your expected interest in 3 months is ${third_interest}. All things being equal. ')
                break
            
            elif t_bonds_option_3.upper() == "B":
        
                third_interest = (6/12) * int(investment_fund_option_3) *2/100
        
                print(f'Your expected interest in 6 months is ${third_interest}. All things being equal.  ')
                break
            
            elif t_bonds_option_3.upper() == "C":
        
                third_interest = int(investment_fund_option_3) * 3/100
        
                print(f'Your expected interest in 6 months is ${third_interest}.All things being equal.  ')
                break
            
            else:
                print("Error!! Please select option A, B or C")
                
    
    if option_3.upper() == "B":
    
        bonds_option_3 = input (f"""
                            
           Would you like to invest in 
           A: 2 years bonds @ {two_years_bonds_rate}
           B: 3 years bonds @ {three_years_bonds_rate}
           C: 5 years bonds @ {five_years_bonds_rate}
           """)
    
        if bonds_option_3.upper()== "A":
        
            third_interest = int(investment_fund_option_3) * 4/100
        
            print(f'Your expected interest per annum is ${third_interest} for the next 2 years. All things being equal. ')
            break
        
        elif bonds_option_3.upper() == "B":
        
            third_interest = int(investment_fund_option_3) * 5/100
        
            print(f'Your expected interest per annum is is ${third_interest} for the next 3 years. All things being equal.  ')
            break
        
        elif bonds_option_3.upper() == "C":
        
            third_interest = int(investment_fund_option_3) * 6/100
        
            print(f'Your expected interest per annum is ${third_interest} for the next 5 years. All things being equal.  ')
            break
            
        else:
            print("Error!! Please select option A, B or C")
        
            bonds_option_3 = input (f"""
                            
            Would you like to invest in 
           A: 2 years bonds @ {two_years_bonds_rate}
           B: 3 years bonds @ {three_years_bonds_rate}
           C: 5 years bonds @ {five_years_bonds_rate}
           """)
    elif option_3.upper() == "C":

        print(f"""
              You have invested ${investment_fund_option_3} in the S&P index stock fund.
              """)
        SP_guess = random.randint(1,3)
        if SP_guess == 1:
            third_interest = 1/100 * investment_fund_option_3
        elif SP_guess == 2:
            third_interest = 1.1/100 * investment_fund_option_3
            
        elif SP_guess == 3:
            third_interest = 1.2/100 * investment_fund_option_3
        break

    elif option_3.upper() == "D":
        third_interest = 1/100 * investment_fund_option_3
        
        print(" You have invested ${investment_fund_option_3} in the Private equity fund.")
        break

    else:     
        print("\n Error!! Please select option A, B, C or D. ")
        continue

    
input( '< Press enter to proceed > \n')

balance_after_option_3 = player_investment_value - int(float(investment_fund_option_3))

print(f"""
      Your current invested amount is you have ${balance_after_option_3} to invest in the next round.
      
      Good Job {player_name}. Happy investing and always remember when life throws you lemon, you do what?
      
      That's right, you make lemonades.
      
      Good luck on your next round of investments!!!
      
      """)

#Round 4

economic_variable = random.randint(1,9)

#investment_fund_option_1 = investment_fund_option_1 + first_interest

#other variables Economic conditions

if economic_variable == 1 :
    
    print("""
          News Flash: Inflation!!!
          
          The Federal Bureau of Statistics reports a general increase in prices of goods and services.
          Typically this leads to increase in rates and stock prices might decrease or increase
          """)
elif economic_variable == 2 :
    
    print("""
          News Flash: Deflation!!!
          
          The Federal Bureau of Statistics reports a general decrease in prices of goods and services.
          Typically this leads to decrease in rates and stock prices might decrease or increase
          """)
elif economic_variable == 3 :
    
    print("""
           News Flash: Economic Meltdown !!!
          
          The Federal Bureau of Statistics reports an Economic Meltdown!!!.
          temporary disruption in economic activities which leads to rates decrease and fall in stock prices.
          """)
elif economic_variable == 4 :
    
    print("""
           News Flash: Unemployment rate: high!!!
          
          The Federal Bureau of Statistics reports an increase the Unemployment rate.
            A rise in unemployment rate leads to decrease in rate and a fall in stock prices.
          """)
    
elif economic_variable == 5 :
    
    print("""
           News Flash: Unemployment rate: low!!!
          
           The Federal Bureau of Statistics reports an decrease the Unemployment rate.
          A fall in unemployment rate leads to an increase in rate and an increase in stock prices.
          """)
    
elif economic_variable == 6 :
    
    print("""
           News Flash: GDP: lower!!!
    
          The Federal Bureau of Statistics reports a decrease in GDP.
          Gross Domestic product is the summation of all economic goods and services produced by nationals of a country. 
          A rise in GDP leads to rise in stocks and fall in rates. 
          A fall in GDP leads more likely to a fall in stock prices and a rise in rates
          """)    

elif economic_variable == 7 :
    
    print("""
           News Flash: GDP: higher!!!
          
          The Federal Bureau of Statistics reports an increase in GDP.
          Gross Domestic product is the summation of all economic goods and services produced by nationals of a country. 
          A rise in GDP leads to more likely to rise in stocks and fall in rates. 
          
          """)   
elif economic_variable == 8 :
    
    print("""
           News Flash: Fire harzard dirupts economic activities !!!
          
          The Federal Bureau of Statistics reports an environmental disruption in the economy.
          Typically this leads likely to increase in rates and stock prices might decrease or increase
          """)       
    
elif economic_variable == 9 :
    
    print("""
           News Flash: Economy: Stable!!!
          
          The Federal Bureau of Statistics reports stabiliy and no threat to current status quo
          """)   

print("economic variable: ", economic_variable)

stocks_rise_fall = random.randint(0,1)

print("stock rise or fall: ", stocks_rise_fall)

if economic_variable == 1: 

    if option_3.upper() == "A" or "B":
    
        three_tbonds_rate = three_tbonds_rate - 0.005
    
        six_tbonds_rate = six_tbonds_rate - 0.005
    
        twelve_tbonds_rate = twelve_tbonds_rate - 0.005
    
        two_years_bonds_rate = two_years_bonds_rate - 0.005
    
        three_years_bonds_rate = three_years_bonds_rate - 0.005
    
        five_years_bonds_rate = five_years_bonds_rate - 0.005
    
    elif option_3.upper() == "C" or "D":
        
        if stocks_rise_fall == 1:
            
            investment_fund_option_3 = investment_fund_option_3 * 1.20
        
            print(f"""
              Invested amount in stocks or private equity fund has increased by 20% to 
              {investment_fund_option_3}    
                 """)
        elif stocks_rise_fall == 0:
            
            investment_fund_option_3 = investment_fund_option_3 * 0.95
        
            print(f"""
              Invested amount in stocks or private equity fund has decreased by 5% to 
              {investment_fund_option_3} 
              """)

if economic_variable == 2: 

    if option_3.upper() == "A" or "B":
    
        three_tbonds_rate = three_tbonds_rate + 0.005
    
        six_tbonds_rate = six_tbonds_rate + 0.005
    
        twelve_tbonds_rate = twelve_tbonds_rate + 0.005
    
        two_years_bonds_rate = two_years_bonds_rate + 0.005
    
        three_years_bonds_rate = three_years_bonds_rate + 0.005
    
        five_years_bonds_rate = five_years_bonds_rate + 0.005
    
    elif option_3.upper() == "C" or "D":
        
        if stocks_rise_fall == 1:
            
            investment_fund_option_3 = investment_fund_option_3 * 1.20
        
            print(f"""
              Invested amount in stocks or private equity fund has increased by 20% to 
              {investment_fund_option_3}    
                 """)
        elif stocks_rise_fall == 0:
            
            investment_fund_option_3 = investment_fund_option_3 * 0.95
        
            print(f"""
              Invested amount in stocks or private equity fund has decreased by 5% to 
              {investment_fund_option_3} 
              """)           

if economic_variable == 3: 

    if option_3.upper() == "A" or "B":
    
        three_tbonds_rate = three_tbonds_rate - 0.005
    
        six_tbonds_rate = six_tbonds_rate - 0.005
    
        twelve_tbonds_rate = six_tbonds_rate - 0.005
    
        two_years_bonds_rate = two_years_bonds_rate- 0.005
    
        three_years_bonds_rate = three_years_bonds_rate - 0.005
    
        five_years_bonds_rate = five_years_bonds_rate - 0.005
    
    elif option_3.upper() == "C" or "D":
        
        investment_fund_option_3 = investment_fund_option_3 * 0.95
        
        print(f"""
              Invested amount in stocks or private equity fund has decreased by 5% to 
              {investment_fund_option_3} 
              """)
if economic_variable == 4: 

    if option_3.upper() == "A" or "B":
    
        three_tbonds_rate = three_tbonds_rate - 0.005
    
        six_tbonds_rate = six_tbonds_rate - 0.005
    
        twelve_tbonds_rate = twelve_tbonds_rate- 0.005
    
        two_years_bonds_rate = two_years_bonds_rate - 0.005
    
        three_years_bonds_rate = three_years_bonds_rate- 0.005
    
        five_years_bonds_rate = five_years_bonds_rate - 0.005
        
    
    elif option_3.upper() == "C" or "D":
        
        investment_fund_option_3 = investment_fund_option_3 * 0.95
        
        print(f"""
              Invested amount in stocks or private equity fund has decreased by 5% to 
              {investment_fund_option_3}
              """)

if economic_variable == 5: 

    if option_3.upper() == "A" or "B":
    
        three_tbonds_rate = 0.01 + 0.005
    
        six_tbonds_rate = 0.02 + 0.005
    
        twelve_tbonds_rate = 0.03 + 0.005
    
        two_years_bonds_rate = 0.04 + 0.005
    
        three_years_bonds_rate = 0.05 + 0.005
    
        five_years_bonds_rate = 0.06 + 0.005
    
    elif option_3.upper() == "C" or "D":
            
            investment_fund_option_3 = investment_fund_option_3 * 1.20
        
            print(f"""
              Invested amount in stocks or private equity fund has increased by 20% to 
              {investment_fund_option_3}    
                 """)
                 
            
if economic_variable == 6: 

    if option_1.upper() == "A" or "B":
    
        three_tbonds_rate = three_tbonds_rate + 0.005
    
        six_tbonds_rate = six_tbonds_rate + 0.005
    
        twelve_tbonds_rate = twelve_tbonds_rate + 0.005
    
        two_years_bonds_rate = 0.04 + 0.005
    
        three_years_bonds_rate = 0.05 + 0.005
    
        five_years_bonds_rate = 0.06 + 0.005
    
    elif option_1.upper() == "C" or "D":
        
        investment_fund_option_3 = investment_fund_option_3 * 0.95
        
        print(f"""
              Invested amount in stocks or private equity fund has decreased by 5% to 
              {investment_fund_option_3}
              """)

if economic_variable == 7: 

    if option_1.upper() == "A" or "B":
    
        three_tbonds_rate = three_tbonds_rate - 0.005
    
        six_tbonds_rate = six_tbonds_rate - 0.005
    
        twelve_tbonds_rate = twelve_tbonds_rate - 0.005
    
        two_years_bonds_rate = two_years_bonds_rate - 0.005
    
        three_years_bonds_rate = three_years_bonds_rate - 0.005
    
        five_years_bonds_rate = five_years_bonds_rate - 0.005
    
    elif option_1.upper() == "C" or "D":
         
        investment_fund_option_3 = investment_fund_option_3 * 1.20
        
        print(f"""
              Invested amount in stocks or private equity fund has increased by 20% to 
              {investment_fund_option_3}    
              """)


if economic_variable == 8: 

    if option_1.upper() == "A" or "B":
    
        three_tbonds_rate = three_tbonds_rate + 0.005
    
        six_tbonds_rate = six_tbonds_rate + 0.005
    
        twelve_tbonds_rate = twelve_tbonds_rate + 0.005
    
        two_years_bonds_rate = two_years_bonds_rate + 0.005
    
        three_years_bonds_rate = three_years_bonds_rate + 0.005
    
        five_years_bonds_rate = five_years_bonds_rate + 0.005
    
    elif option_1.upper() == "C" or "D":
        
        if stocks_rise_fall == 1:
            
            investment_fund_option_3 = investment_fund_option_3 * 1.20
        
            print(f"""
              Invested amount in stocks or private equity fund has increased by 20% to 
              {investment_fund_option_3}    
                 """)
        elif stocks_rise_fall == 0:
            
            investment_fund_option_1_eco = investment_fund_option_1 * 0.95
        
            print(f"""
              Invested amount in stocks or private equity fund has decreased by 5% to 
              {investment_fund_option_3}
              """) 

if economic_variable == 9: 
   
    print (f"Economy is stable for now {player_name}.")
    
    
input("Press enter to continue")

print(f""" Welcome {player_name}!!! to another round of investing. I'm sure you're getting a hang of it. Jane your financial advisor will send your your account info in a moment.
      """)

input("Press enter to continue")

print(f"""
      Dear {player_name},
      
      I hope the news flash hasn't bogged you down one bit.
      
      I just want to give you an update on how you doing so far.
     
      Sincerely,
      
      Jane
       
	Stage	Amount Invested_interest earned	Investment value	Interest earned and Investment value
round 1	        a	d			
round 2	        d	f			
round 3	        a	d			
round 4	        d	f			
round 5	        a	d			
round 6	        d	f			

""")

investment_fund_option_4 = balance_after_option_3

while True:

    option_4 = input( """
                 
      Please type an option to invest in.
      
      A: Treasury Bonds
      B: Bonds
      C: Stocks
      D: Private Equity
      
      select A, B, C or D
      """)
    
    if option_4.upper() == "A":
    
            t_bonds_option_4 = input (f"""
           Would you like to invest in 
           A: 3 months treasury bonds @ {three_tbonds_rate}
           B: 6 months treasury bonds @ {six_tbonds_rate}
           C: 12 month treasury bonds @ {twelve_tbonds_rate}
           """)
            
            if t_bonds_option_4.upper()== "A":
        
                fourth_interest = (3/12) * int(investment_fund_option_4) * three_tbonds_rate
        
                print(f'Your expected interest in 3 months is ${fourth_interest}. All things being equal. ')
                break
            
            elif t_bonds_option_2.upper() == "B":
        
                fourth_interest = (6/12) * int(investment_fund_option_4) * six_tbonds_rate
        
                print(f'Your expected interest in 6 months is ${fourth_interest}. All things being equal.  ')
                break
            
            elif t_bonds_option_2.upper() == "C":
        
                fourth_interest = int(investment_fund_option_4) * twelve_tbonds_rate
        
                print(f'Your expected interest in 6 months is ${fourth_interest}.All things being equal.  ')
                break
            
            else:
                print("Error!! Please select option A, B or C")
                
    
    if option_4.upper() == "B":
    
        bonds_option_4 = input (f"""
                            
           Would you like to invest in 
           A: 2 years bonds @ {two_years_bonds_rate}
           B: 3 years bonds @ {three_years_bonds_rate}
           C: 5 years bonds @ {five_years_bonds_rate}
           """)
    
        if bonds_option_4.upper()== "A":
        
            fourth_interest = int(investment_fund_option_4) * two_years_bonds_rate
        
            print(f'Your expected interest per annum is ${fourth_interest} for the next 2 years. All things being equal. ')
            break
        
        elif bonds_option_4.upper() == "B":
        
            fourth_interest = int(investment_fund_option_2) * three_years_bonds_rate
        
            print(f'Your expected interest per annum is is ${fourth_interest} for the next 3 years. All things being equal.  ')
            break
        
        elif bonds_option_4.upper() == "C":
        
            fourth_interest = int(investment_fund_option_2) * five_years_bonds_rate
        
            print(f'Your expected interest per annum is ${fourth_interest} for the next 5 years. All things being equal.  ')
            break
            
        else:
            print("Error!! Please select option A, B or C")
        
            bonds_option_4 = input (f"""
                            
            Would you like to invest in 
           A: 2 years bonds @ {two_years_bonds_rate}
           B: 3 years bonds @ {three_years_bonds_rate}
           C: 5 years bonds @ {five_years_bonds_rate}
           """)
            
    elif option_4.upper() == "C":

        print(f"""
              You have invested ${investment_fund_option_4} in the S&P index stock fund.
              """)
        SP_guess = random.randint(1,3)
        if SP_guess == 1:
            fourth_interest= -1/100 * investment_fund_option_1
        elif SP_guess == 2:
            fourth_interest = 1/100 * investment_fund_option_1
            
        elif SP_guess == 3:
            fourth_interest = 2/100 * investment_fund_option_1
        break

    elif option_4.upper() == "D":
    
        print(f" You have invested ${investment_fund_option_4} in the Private equity fund.")
        break

    else:     
        print("\n Error!! Please select option A, B, C or D. ")
        continue

    
input( '< Press enter to proceed > \n')

balance_after_option_4 = player_investment_value - investment_fund_option_1-investment_fund_option_2-investment_fund_option_3

print(f"""
      Your current invested amount in round one and two is  ${investment_fund_option_1} and ${investment_fund_option_2} respectively and you have ${balance_after_option_2} to invest.
      
      Good Job {player_name}. Happy investing and always remember when life throws you lemon, you do what?
      
      That's right, you make lemonades.
      
      Good luck on your next round of investments!!!
      
      """)

input("Press enter to continue")

print(f"""
      Dear {player_name},
      
      I hope the news flash hasn't bogged you down one bit.
      
      I just want to give you an update on how you doing so far.
     
      Sincerely,
      
      Jane
       
	Stage	Amount Invested_interest earned	Investment value	Interest earned and Investment value
round 1	        a	d			
round 2	        d	f			
round 3	        a	d			
round 4	        d	f			
round 5	        a	d			
round 6	        d	f	
		
    """)
print (balance_after_option_4)

total_loan_repayment = (int(investment_fund) * 1.07 * 1.07) + player_investment_value  * 1.10 * 1.10

player_investment_value_2 = player_investment_value + balance_after_option_3 + first_interest + second_interest + third_interest + fourth_interest


if player_investment_value_2 < total_loan_repayment:
    
    print ("Game Over!!! Would you like to try again?")
    
    exit
    
# STAGE 3  

else: 
    print (f" Welcome to the final stage!!! You have ${player_investment_value_2} in investment value!!! Keep it up.")
    
    
input("Please press enter to continue")


economic_variable = random.randint(1,9)

#investment_fund_option_1 = investment_fund_option_1 + first_interest

#other variables Economic conditions

if economic_variable == 1 :
    
    print("""
          Inflation!!!
          
          The Federal Bureau of Statistics reports a general increase in prices of goods and services.
          Typically this leads to increase in rates and stock prices might decrease or increase
          """)
elif economic_variable == 2 :
    
    print("""
          News Flash: Deflation!!!
          
          The Federal Bureau of Statistics reports a general decrease in prices of goods and services.
          Typically this leads to decrease in rates and stock prices might decrease or increase
          """)
elif economic_variable == 3 :
    
    print("""
          Economic Meltdown !!!
          
          The Federal Bureau of Statistics reports an Economic Meltdown!!!.
          temporary disruption in economic activities which leads to rates decrease and fall in stock prices.
          """)
elif economic_variable == 4 :
    
    print("""
          Unemployment rate: high!!!
          
          The Federal Bureau of Statistics reports an increase the Unemployment rate.
            A rise in unemployment rate leads to decrease in rate and a fall in stock prices.
          """)
    
elif economic_variable == 5 :
    
    print("""
          Unemployment rate: low!!!
          
           The Federal Bureau of Statistics reports an decrease the Unemployment rate.
          A fall in unemployment rate leads to an increase in rate and an increase in stock prices.
          """)
    
elif economic_variable == 6 :
    
    print("""
          GDP: lower!!!
    
          The Federal Bureau of Statistics reports a decrease in GDP.
          Gross Domestic product is the summation of all economic goods and services produced by nationals of a country. 
          A rise in GDP leads to rise in stocks and fall in rates. 
          A fall in GDP leads more likely to a fall in stock prices and a rise in rates
          """)    

elif economic_variable == 7 :
    
    print("""
          GDP: higher!!!
          
          The Federal Bureau of Statistics reports an increase in GDP.
          Gross Domestic product is the summation of all economic goods and services produced by nationals of a country. 
          A rise in GDP leads to more likely to rise in stocks and fall in rates. 
          
          """)   
elif economic_variable == 8 :
    
    print("""
          Fire harzard dirupts economic activities !!!
          
          The Federal Bureau of Statistics reports an environmental disruption in the economy.
          Typically this leads likely to increase in rates and stock prices might decrease or increase
          """)       
    
elif economic_variable == 9 :
    
    print("""
          Economy: Stable!!!
          
          The Federal Bureau of Statistics reports stabiliy and no threat to current status quo
          """)   

print("economic variable: ", economic_variable)

stocks_rise_fall = random.randint(0,1)

print("stock rise or fall: ", stocks_rise_fall)

if economic_variable == 1: 

    if option_4.upper() == "A" or "B":
    
        three_tbonds_rate = 0.01 - 0.005
    
        six_tbonds_rate = 0.02 - 0.005
    
        twelve_tbonds_rate = 0.03 - 0.005
    
        two_years_bonds_rate = 0.04 - 0.005
    
        three_years_bonds_rate = 0.05 - 0.005
    
        five_years_bonds_rate = 0.06 - 0.005
    
    elif option_4.upper() == "C" or "D":
        
        if stocks_rise_fall == 1:
            
            investment_fund_option_4 = investment_fund_option_4 * 1.10
        
            print(f"""
              Invested amount in stocks or private equity fund has increased by 20% to 
              {investment_fund_option_4}    
                 """)
        elif stocks_rise_fall == 0:
            
            investment_fund_option_4 = investment_fund_option_4 * 0.90
        
            print(f"""
              Invested amount in stocks or private equity fund has decreased by 5% to 
              {investment_fund_option_4} 
              """)

if economic_variable == 2: 

    if option_2.upper() == "A" or "B":
    
        three_tbonds_rate = 0.01 + 0.005
    
        six_tbonds_rate = 0.02 + 0.005
    
        twelve_tbonds_rate = 0.03 + 0.005
    
        two_years_bonds_rate = 0.04 + 0.005
    
        three_years_bonds_rate = 0.05 + 0.005
    
        five_years_bonds_rate = 0.06 + 0.005
    
    elif option_2.upper() == "C" or "D":
        
        if stocks_rise_fall == 1:
            
            investment_fund_option_4 = investment_fund_option_4 * 1.20
        
            print(f"""
              Invested amount in stocks or private equity fund has increased by 20% to 
              {investment_fund_option_4}    
                 """)
        elif stocks_rise_fall == 0:
            
            investment_fund_option_4 = investment_fund_option_4 * 0.95
        
            print(f"""
              Invested amount in stocks or private equity fund has decreased by 5% to 
              {investment_fund_option_4} 
              """)           

if economic_variable == 3: 

    if option_2.upper() == "A" or "B":
    
        three_tbonds_rate = 0.01 - 0.005
    
        six_tbonds_rate = 0.02 - 0.005
    
        twelve_tbonds_rate = 0.03 - 0.005
    
        two_years_bonds_rate = 0.04 - 0.005
    
        three_years_bonds_rate = 0.05 - 0.005
    
        five_years_bonds_rate = 0.06 - 0.005
    
    elif option_2.upper() == "C" or "D":
        
        investment_fund_option_4 = investment_fund_option_4 * 0.95
        
        print(f"""
              Invested amount in stocks or private equity fund has decreased by 5% to 
              {investment_fund_option_4} 
              """)
if economic_variable == 4: 

    if option_2.upper() == "A" or "B":
    
        three_tbonds_rate = 0.01 - 0.005
    
        six_tbonds_rate = 0.02 - 0.005
    
        twelve_tbonds_rate = 0.03 - 0.005
    
        two_years_bonds_rate = 0.04 - 0.005
    
        three_years_bonds_rate = 0.05 - 0.005
    
        five_years_bonds_rate = 0.06 - 0.005
        
    
    elif option_2.upper() == "C" or "D":
        
        investment_fund_option_4 = investment_fund_option_4 * 0.95
        
        print(f"""
              Invested amount in stocks or private equity fund has decreased by 5% to 
              {investment_fund_option_4}
              """)

if economic_variable == 5: 

    if option_2.upper() == "A" or "B":
    
        three_tbonds_rate = 0.01 + 0.005
    
        six_tbonds_rate = 0.02 + 0.005
    
        twelve_tbonds_rate = 0.03 + 0.005
    
        two_years_bonds_rate = 0.04 + 0.005
    
        three_years_bonds_rate = 0.05 + 0.005
    
        five_years_bonds_rate = 0.06 + 0.005
    
    elif option_2.upper() == "C" or "D":
            
            investment_fund_option_4 = investment_fund_option_4 * 1.20
        
            print(f"""
              Invested amount in stocks or private equity fund has increased by 20% to 
              {investment_fund_option_4}    
                 """)
                 
            
if economic_variable == 6: 

    if option_2.upper() == "A" or "B":
    
        three_tbonds_rate = 0.01 + 0.005
    
        six_tbonds_rate = 0.02 + 0.005
    
        twelve_tbonds_rate = 0.03 + 0.005
    
        two_years_bonds_rate = 0.04 + 0.005
    
        three_years_bonds_rate = 0.05 + 0.005
    
        five_years_bonds_rate = 0.06 + 0.005
    
    elif option_2.upper() == "C" or "D":
        
        investment_fund_option_4 = investment_fund_option_4 * 0.95
        
        print(f"""
              Invested amount in stocks or private equity fund has decreased by 5% to 
              {investment_fund_option_4}
              """)

if economic_variable == 7: 

    if option_2.upper() == "A" or "B":
    
        three_tbonds_rate = 0.01 - 0.005
    
        six_tbonds_rate = 0.02 - 0.005
    
        twelve_tbonds_rate = 0.03 - 0.005
    
        two_years_bonds_rate = 0.04 - 0.005
    
        three_years_bonds_rate = 0.05 - 0.005
    
        five_years_bonds_rate = 0.06 - 0.005
    
    elif option_2.upper() == "C" or "D":
         
        investment_fund_option_4 = investment_fund_option_4 * 1.20
        
        print(f"""
              Invested amount in stocks or private equity fund has increased by 20% to 
              {investment_fund_option_4}    
              """)


if economic_variable == 8: 

    if option_2.upper() == "A" or "B":
    
        three_tbonds_rate = 0.01 + 0.005
    
        six_tbonds_rate = 0.02 + 0.005
    
        twelve_tbonds_rate = 0.03 + 0.005
    
        two_years_bonds_rate = 0.04 + 0.005
    
        three_years_bonds_rate = 0.05 + 0.005
    
        five_years_bonds_rate = 0.06 + 0.005
    
    elif option_1.upper() == "C" or "D":
        
        if stocks_rise_fall == 1:
            
            investment_fund_option_4 = investment_fund_option_4 * 1.20
        
            print(f"""
              Invested amount in stocks or private equity fund has increased by 20% to 
              {investment_fund_option_4}    
                 """)
        elif stocks_rise_fall == 0:
            
            investment_fund_option_4 = investment_fund_option_4 * 0.95
        
            print(f"""
              Invested amount in stocks or private equity fund has decreased by 5% to 
              {investment_fund_option_4}
              """) 

if economic_variable == 9: 
   
    print (f"Economy is stable for now {player_name}.")
    
    
input("Press enter to continue")


investment_fund_option_5 = input(f'How much would you like to invest from ${player_investment_value}: ')


print(f"Awesome!!! You have decided on investing {investment_fund_option_3}")


investment_fund_option_5 = int(float(f"{investment_fund_option_5}"))
    
if investment_fund_option_5 >= player_investment_value_2:
    
    print(f""" Error!!! Please input value less than {player_investment_value_2}""")
    
    investment_fund_option_5 = input('How much would you like to invest: ')
        
else:
    print(f'You have decided to invest {investment_fund_option_5} ')

option_5 = input( """
                 
      Please type an option to invest in.
      
      A: Treasury Bonds
      B: Bonds
      C: Stocks
      D: Private Equity
      
      select A, B, C or D
      """)


while True:

    option_5 = input( """
                 
      Please type an option to invest in.
      
      A: Treasury Bonds
      B: Bonds
      C: Stocks
      D: Private Equity
      
      select A, B, C or D
      """)
    
    if option_5.upper() == "A":
    
            t_bonds_option_5 = input (f"""
           Would you like to invest in 
           A: 3 months treasury bonds @ {three_tbonds_rate}
           B: 6 months treasury bonds @ {six_tbonds_rate}
           C: 12 month treasury bonds @ {twelve_tbonds_rate}
           """)
            
            if t_bonds_option_5.upper()== "A":
        
                fifth_interest = (3/12) * int(investment_fund_option_5) * 1/100
        
                print(f'Your expected interest in 3 months is ${fifth_interest}. All things being equal. ')
                break
            
            elif t_bonds_option_5.upper() == "B":
        
                fifth_interest = (6/12) * int(investment_fund_option_5) *2/100
        
                print(f'Your expected interest in 6 months is ${fifth_interest}. All things being equal.  ')
                break
            
            elif t_bonds_option_5.upper() == "C":
        
                fifth_interest = int(investment_fund_option_5) * 3/100
        
                print(f'Your expected interest in 6 months is ${fifth_interest}.All things being equal.  ')
                break
            
            else:
                print("Error!! Please select option A, B or C")
                
    
    if option_5.upper() == "B":
    
        bonds_option_5 = input (f"""
                            
           Would you like to invest in 
           A: 2 years bonds @ {two_years_bonds_rate}
           B: 3 years bonds @ {three_years_bonds_rate}
           C: 5 years bonds @ {five_years_bonds_rate}
           """)
    
        if bonds_option_5.upper()== "A":
        
            fifth_interest = int(investment_fund_option_5) * 4/100
        
            print(f'Your expected interest per annum is ${fifth_interest} for the next 2 years. All things being equal. ')
            break
        
        elif bonds_option_5.upper() == "B":
        
            fifth_interest = int(investment_fund_option_5) * 5/100
        
            print(f'Your expected interest per annum is is ${fifth_interest} for the next 3 years. All things being equal.  ')
            break
        
        elif bonds_option_5.upper() == "C":
        
            fifth_interest = int(investment_fund_option_5) * 6/100
        
            print(f'Your expected interest per annum is ${third_interest} for the next 5 years. All things being equal.  ')
            break
            
        else:
            print("Error!! Please select option A, B or C")
        
            bonds_option_3 = input (f"""
                            
            Would you like to invest in 
           A: 2 years bonds @ {two_years_bonds_rate}
           B: 3 years bonds @ {three_years_bonds_rate}
           C: 5 years bonds @ {five_years_bonds_rate}
           """)
    elif option_3.upper() == "C":

        print(f"""
              You have invested ${investment_fund_option_5} in the S&P index stock fund.
              """)
        SP_guess = random.randint(1,3)
        if SP_guess == 1:
             fifth_interest = 1/100 * investment_fund_option_5
        elif SP_guess == 2:
             fifth_interest = 1/100 * investment_fund_option_5
            
        elif SP_guess == 3:
             fifth_interest = 1/100 * investment_fund_option_5
        break

    elif option_3.upper() == "D":
        fifth_interest_interest = 1/100 * investment_fund_option_3
        print(" You have invested ${investment_fund_option_5} in the Private equity fund.")
        break

    else:     
        print("\n Error!! Please select option A, B, C or D. ")
        continue

    
input( '< Press enter to proceed > \n')

balance_after_option_5 = player_investment_value_2 - int(float(investment_fund_option_5)) - (player_investment_value * 2)

print(f"""
      Your current invested amount is you have ${balance_after_option_5} to invest in the next round.
      
      Good Job {player_name}. Happy investing and always remember when life throws you lemon, you do what?
      
      That's right, you make lemonades.
      
      Good luck on your final round!!!
      
      """)

#Round 6

economic_variable = random.randint(1,9)

#investment_fund_option_1 = investment_fund_option_1 + first_interest

#other variables Economic conditions

if economic_variable == 1 :
    
    print("""
          News Flash: Inflation!!!
          
          The Federal Bureau of Statistics reports a general increase in prices of goods and services.
          Typically this leads to increase in rates and stock prices might decrease or increase
          """)
elif economic_variable == 2 :
    
    print("""
          News Flash: Deflation!!!
          
          The Federal Bureau of Statistics reports a general decrease in prices of goods and services.
          Typically this leads to decrease in rates and stock prices might decrease or increase
          """)
elif economic_variable == 3 :
    
    print("""
           News Flash: Economic Meltdown !!!
          
          The Federal Bureau of Statistics reports an Economic Meltdown!!!.
          temporary disruption in economic activities which leads to rates decrease and fall in stock prices.
          """)
elif economic_variable == 4 :
    
    print("""
           News Flash: Unemployment rate: high!!!
          
          The Federal Bureau of Statistics reports an increase the Unemployment rate.
            A rise in unemployment rate leads to decrease in rate and a fall in stock prices.
          """)
    
elif economic_variable == 5 :
    
    print("""
           News Flash: Unemployment rate: low!!!
          
           The Federal Bureau of Statistics reports an decrease the Unemployment rate.
          A fall in unemployment rate leads to an increase in rate and an increase in stock prices.
          """)
    
elif economic_variable == 6 :
    
    print("""
           News Flash: GDP: lower!!!
    
          The Federal Bureau of Statistics reports a decrease in GDP.
          Gross Domestic product is the summation of all economic goods and services produced by nationals of a country. 
          A rise in GDP leads to rise in stocks and fall in rates. 
          A fall in GDP leads more likely to a fall in stock prices and a rise in rates
          """)    

elif economic_variable == 7 :
    
    print("""
           News Flash: GDP: higher!!!
          
          The Federal Bureau of Statistics reports an increase in GDP.
          Gross Domestic product is the summation of all economic goods and services produced by nationals of a country. 
          A rise in GDP leads to more likely to rise in stocks and fall in rates. 
          
          """)   
elif economic_variable == 8 :
    
    print("""
           News Flash: Fire harzard dirupts economic activities !!!
          
          The Federal Bureau of Statistics reports an environmental disruption in the economy.
          Typically this leads likely to increase in rates and stock prices might decrease or increase
          """)       
    
elif economic_variable == 9 :
    
    print("""
           News Flash: Economy: Stable!!!
          
          The Federal Bureau of Statistics reports stabiliy and no threat to current status quo
          """)   

print("economic variable: ", economic_variable)

stocks_rise_fall = random.randint(0,1)

print("stock rise or fall: ", stocks_rise_fall)

if economic_variable == 1: 

    if option_5.upper() == "A" or "B":
    
        three_tbonds_rate = 0.01 - 0.005
    
        six_tbonds_rate = 0.02 - 0.005
    
        twelve_tbonds_rate = 0.03 - 0.005
    
        two_years_bonds_rate = 0.04 - 0.005
    
        three_years_bonds_rate = 0.05 - 0.005
    
        five_years_bonds_rate = 0.06 - 0.005
    
    elif option_5.upper() == "C" or "D":
        
        if stocks_rise_fall == 1:
            
            investment_fund_option_5 = investment_fund_option_5 * 1.20
        
            print(f"""
              Invested amount in stocks or private equity fund has increased by 20% to 
              {investment_fund_option_5}    
                 """)
        elif stocks_rise_fall == 0:
            
            investment_fund_option_5 = investment_fund_option_5 * 0.95
        
            print(f"""
              Invested amount in stocks or private equity fund has decreased by 5% to 
              {investment_fund_option_5} 
              """)

if economic_variable == 2: 

    if option_5.upper() == "A" or "B":
    
        three_tbonds_rate = 0.01 + 0.005
    
        six_tbonds_rate = 0.02 + 0.005
    
        twelve_tbonds_rate = 0.03 + 0.005
    
        two_years_bonds_rate = 0.04 + 0.005
    
        three_years_bonds_rate = 0.05 + 0.005
    
        five_years_bonds_rate = 0.06 + 0.005
    
    elif option_5.upper() == "C" or "D":
        
        if stocks_rise_fall == 1:
            
            investment_fund_option_5 = investment_fund_option_5 * 1.20
        
            print(f"""
              Invested amount in stocks or private equity fund has increased by 20% to 
              {investment_fund_option_5}    
                 """)
        elif stocks_rise_fall == 0:
            
            investment_fund_option_5 = investment_fund_option_5 * 0.95
        
            print(f"""
              Invested amount in stocks or private equity fund has decreased by 5% to 
              {investment_fund_option_5} 
              """)           

if economic_variable == 3: 

    if option_5.upper() == "A" or "B":
    
        three_tbonds_rate = 0.01 - 0.005
    
        six_tbonds_rate = 0.02 - 0.005
    
        twelve_tbonds_rate = 0.03 - 0.005
    
        two_years_bonds_rate = 0.04 - 0.005
    
        three_years_bonds_rate = 0.05 - 0.005
    
        five_years_bonds_rate = 0.06 - 0.005
    
    elif option_5.upper() == "C" or "D":
        
        investment_fund_option_5 = investment_fund_option_5 * 0.95
        
        print(f"""
              Invested amount in stocks or private equity fund has decreased by 5% to 
              {investment_fund_option_5} 
              """)
if economic_variable == 4: 

    if option_5.upper() == "A" or "B":
    
        three_tbonds_rate = 0.01 - 0.005
    
        six_tbonds_rate = 0.02 - 0.005
    
        twelve_tbonds_rate = 0.03 - 0.005
    
        two_years_bonds_rate = 0.04 - 0.005
    
        three_years_bonds_rate = 0.05 - 0.005
    
        five_years_bonds_rate = 0.06 - 0.005
        
    
    elif option_5.upper() == "C" or "D":
        
        investment_fund_option_5 = investment_fund_option_5 * 0.95
        
        print(f"""
              Invested amount in stocks or private equity fund has decreased by 5% to 
              {investment_fund_option_5}
              """)

if economic_variable == 5: 

    if option_5.upper() == "A" or "B":
    
        three_tbonds_rate = 0.01 + 0.005
    
        six_tbonds_rate = 0.02 + 0.005
    
        twelve_tbonds_rate = 0.03 + 0.005
    
        two_years_bonds_rate = 0.04 + 0.005
    
        three_years_bonds_rate = 0.05 + 0.005
    
        five_years_bonds_rate = 0.06 + 0.005
    
    elif option_5.upper() == "C" or "D":
            
            investment_fund_option_5 = investment_fund_option_5 * 1.20
        
            print(f"""
              Invested amount in stocks or private equity fund has increased by 20% to 
              {investment_fund_option_5}    
                 """)
                 
            
if economic_variable == 6: 

    if option_5.upper() == "A" or "B":
    
        three_tbonds_rate = 0.01 + 0.005
    
        six_tbonds_rate = 0.02 + 0.005
    
        twelve_tbonds_rate = 0.03 + 0.005
    
        two_years_bonds_rate = 0.04 + 0.005
    
        three_years_bonds_rate = 0.05 + 0.005
    
        five_years_bonds_rate = 0.06 + 0.005
    
    elif option_5.upper() == "C" or "D":
        
        investment_fund_option_5 = investment_fund_option_5 * 0.95
        
        print(f"""
              Invested amount in stocks or private equity fund has decreased by 5% to 
              {investment_fund_option_5}
              """)

if economic_variable == 7: 

    if option_5.upper() == "A" or "B":
    
        three_tbonds_rate = 0.01 - 0.005
    
        six_tbonds_rate = 0.02 - 0.005
    
        twelve_tbonds_rate = 0.03 - 0.005
    
        two_years_bonds_rate = 0.04 - 0.005
    
        three_years_bonds_rate = 0.05 - 0.005
    
        five_years_bonds_rate = 0.06 - 0.005
    
    elif option_5.upper() == "C" or "D":
         
        investment_fund_option_5 = investment_fund_option_5 * 1.20
        
        print(f"""
              Invested amount in stocks or private equity fund has increased by 20% to 
              {investment_fund_option_5}    
              """)


if economic_variable == 8: 

    if option_5.upper() == "A" or "B":
    
        three_tbonds_rate = 0.01 + 0.005
    
        six_tbonds_rate = 0.02 + 0.005
    
        twelve_tbonds_rate = 0.03 + 0.005
    
        two_years_bonds_rate = 0.04 + 0.005
    
        three_years_bonds_rate = 0.05 + 0.005
    
        five_years_bonds_rate = 0.06 + 0.005
    
    elif option_5.upper() == "C" or "D":
        
        if stocks_rise_fall == 1:
            
            investment_fund_option_5 = investment_fund_option_5 * 1.20
        
            print(f"""
              Invested amount in stocks or private equity fund has increased by 20% to 
              {investment_fund_option_5}    
                 """)
        elif stocks_rise_fall == 0:
            
            investment_fund_option_5 = investment_fund_option_5 * 0.95
        
            print(f"""
              Invested amount in stocks or private equity fund has decreased by 5% to 
              {investment_fund_option_5}
              """) 

if economic_variable == 9: 
   
    print (f"Economy is stable for now {player_name}.")
    
    
input("Press enter to continue")

print(f""" Welcome {player_name}!!! to another round of investing. I'm sure you're getting a hang of it. Jane your financial advisor will send your your account info in a moment.
      """)

input("Press enter to continue")

print(f"""
      Dear {player_name},
      
      I hope the news flash hasn't bogged you down one bit.
      
      I just want to give you an update on how you doing so far.
     
      Sincerely,
      
      Jane
       
	Stage	Amount Invested_interest earned	Investment value	Interest earned and Investment value
round 1	        a	d			
round 2	        d	f			
round 3	        a	d			
round 4	        d	f			
round 5	        a	d			
round 6	        d	f			

""")

investment_fund_option_6 = balance_after_option_4

while True:

    option_6 = input( """
                 
      Please type an option to invest in.
      
      A: Treasury Bonds
      B: Bonds
      C: Stocks
      D: Private Equity
      
      select A, B, C or D
      """)
    
    if option_6.upper() == "A":
    
            t_bonds_option_6 = input (f"""
           Would you like to invest in 
           A: 3 months treasury bonds @ {three_tbonds_rate}
           B: 6 months treasury bonds @ {six_tbonds_rate}
           C: 12 month treasury bonds @ {twelve_tbonds_rate}
           """)
            
            if t_bonds_option_6.upper()== "A":
        
                final_interest = (3/12) * int(investment_fund_option_6) * three_tbonds_rate
        
                print(f'Your expected interest in 3 months is ${final_interest}. All things being equal. ')
                break
            
            elif t_bonds_option_6.upper() == "B":
        
                final_interest = (6/12) * int(investment_fund_option_6) *2/100
        
                print(f'Your expected interest in 6 months is ${final_interest}. All things being equal.  ')
                break
            
            elif t_bonds_option_2.upper() == "C":
        
                final_interest = int(investment_fund_option_6) * 3/100
        
                print(f'Your expected interest in 6 months is ${final_interest}.All things being equal.  ')
                break
            
            else:
                print("Error!! Please select option A, B or C")
                
    
    if option_6.upper() == "B":
    
        bonds_option_6 = input (f"""
                            
           Would you like to invest in 
           A: 2 years bonds @ {two_years_bonds_rate}
           B: 3 years bonds @ {three_years_bonds_rate}
           C: 5 years bonds @ {five_years_bonds_rate}
           """)
    
        if bonds_option_6.upper()== "A":
        
            final_interest = int(investment_fund_option_6) * 4/100
        
            print(f'Your expected interest per annum is ${final_interest} for the next 2 years. All things being equal. ')
            break
        
        elif bonds_option_6.upper() == "B":
        
            final_interest = int(investment_fund_option_6) * 5/100
        
            print(f'Your expected interest per annum is is ${final_interest} for the next 3 years. All things being equal.  ')
            break
        
        elif bonds_option_4.upper() == "C":
        
            fourth_interest = int(investment_fund_option_6) * 6/100
        
            print(f'Your expected interest per annum is ${final_interest for the next 5 years. All things being equal.  ')
            break
            
        else:
            print("Error!! Please select option A, B or C")
        
            bonds_option_5 = input (f"""
                            
            Would you like to invest in 
           A: 2 years bonds @ {two_years_bonds_rate}
           B: 3 years bonds @ {three_years_bonds_rate}
           C: 5 years bonds @ {five_years_bonds_rate}
           """)
            
    elif option_5.upper() == "C":

        print(f"""
              You have invested ${investment_fund_option_4} in the S&P index stock fund.
              """)
        SP_guess = random.randint(1,3)
        if SP_guess == 1:
            final_interest=  1/100 * investment_fund_option_6
        elif SP_guess == 2:
            final_interest = 1/100 * investment_fund_option_6
            
        elif SP_guess == 3:
            final_interest = 1/100 * investment_fund_option_6
        break

    elif option_6.upper() == "D":
        final_interest = 1/100 * investment_fund_option_6
        
        print(f" You have invested ${investment_fund_option_6} in the Private equity fund.")
        break

    else:     
        print("\n Error!! Please select option A, B, C or D. ")
        continue

    
input( '< Press enter to proceed > \n')

balance_after_option_6 = player_investment_value_2 - investment_fund_option_5-investment_fund_option_6

print(f"""
      Your current invested amount in round one and two is  ${investment_fund_option_1} and ${investment_fund_option_2} respectively and you have ${balance_after_option_2} to invest.
      
      Good Job {player_name}. Happy investing and always remember when life throws you lemon, you do what?
      
      That's right, you make lemonades.
      
      Good luck on your next round of investments!!!
      
      """)

input("Press enter to continue")

print(f"""
      Dear {player_name},
      
      I hope the news flash hasn't bogged you down one bit.
      
      I just want to give you an update on how you doing so far.
     
      Sincerely,
      
      Jane
       
	Stage	Amount Invested_interest earned	Investment value	Interest earned and Investment value
round 1	        a	d			
round 2	        d	f			
round 3	        a	d			
round 4	        d	f			
round 5	        a	d			
round 6	        d	f	
		
    """)
print (balance_after_option_4)

total_loan_repayment_3 = (int(investment_fund) * 1.07 * 1.07) + (player_investment_value  * 1.10 * 1.10) + (player_investment_value_2  * 1.11 * 1.11)

player_investment_value_3 = player_investment_value + balance_after_option_3 + first_interest + second_interest + third_interest + fourth_interest+fifth_interest+final_interest


if player_investment_value_3 < total_loan_repayment:
    
    print ("Game Over!!! Would you like to try again?")
    
    exit
    
# STAGE 3  
else:
     print ("CONGRATS!!! PRO. YOU WIN. STELLAR PERFORMANCE I MUST SAY.")


      
   

     
            
            


    #investment_fund_option_1 = investment_fund_option_1 * ()
  
    
#
#Deflation = [General decrease in prices of goods and services. Typically leads to 
#decrease in rate and stock prices might decrease or increase].
#
#economic meltdown = [temporary disruption in economic activities which leads 
#to rates decrease and fall in stock prices]
#
#unemployment = [rise in unemployment rate leads to decrease in rate and a fall in stock prices.
#fall in unemployment rate leads to increase in stock prices and increase in rate]
#
#gdp = [Gross Domestic product is the summation of all economic goods and services produced
#by nationals of a country. A rise in GDP leads to rise in stocks and fall in rates. A
#fall in GDP leads to a fall in stock prices and a rise in rates]
#
#Economic disaster=[increase in rate; increase in stocks]
#
#normal condition= no changes in economic conditions

#print(economic_variable)





    
    
#asset_class = ['stocks','private_equity_fund','t_bills,bonds', 'nothing']
#
#print(asset_class)

#
#The player starts with a loan of $10,000 @ 7%
#
#

#
#Investment strategy =[ 'long' or 'short']
#
#Economic conditions =inflation, deflation, economic meltdown, unemployment, gdp
#environmental disater, normal conditions]
#
#Bank rate: floating rate: (5 years bond rate + 1%)
#
#VARIABLES
#stocks=['A stock is an investment (or asset_class) that signifies proportionate
#ownership in the issuing corporation. Stocks are risky but provide above normal returns.  '.]
#
#private_equity_fund= ['Private equity fund is an investment (or asset_class) that signifies 
#proportionate ownership in the issuing in private companies. More risky than 
#stocks but provide above normal returns.']
#
#Treasury_bonds: [' fixed rate investment that pays certain percentage of 
#interest based on principal. usually tenor is less than a year]
#
#Bonds: [fixed rate investment that pays certain percentage of 
#interest based on principal. usually tenor is more than a year.]
#
#other variables Economic conditions
#Inflation = [ General increase in prices of goods and services. Typically leads to 
#increase in rate and stock prices might decrease or increase]
#
#Deflation = [General decrease in prices of goods and services. Typically leads to 
#decrease in rate and stock prices might decrease or increase].
#
#economic meltdown = [temporary disruption in economic activities which leads 
#to rates decrease and fall in stock prices]
#
#unemployment = [rise in unemployment rate leads to decrease in rate and a fall in stock prices.
#fall in unemployment rate leads to increase in stock prices and increase in rate]
#
#gdp = [Gross Domestic product is the summation of all economic goods and services produced
#by nationals of a country. A rise in GDP leads to rise in stocks and fall in rates. A
#fall in GDP leads to a fall in stock prices and a rise in rates]
#
#Economic disaster=[increase in rate; increase in stocks]
#
#normal condition= no changes in economic conditions
#
#bank loan = 7% = [5 year bond rate + 1]
#
#1 year bond rate = 3%
#2 year bond rate = 4%
#3 year bond rate = 5%
#5 year bond rate = 6%
