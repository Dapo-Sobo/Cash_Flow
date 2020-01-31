#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 21:27:20 2019

@author: ibidapo
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 11:11:22 2019

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

def game_start():

   
    
    print("""
              
         Welcome!!! 
         
         The name of the game is called Cash Flow. 
         The goal of the game is to increase the value of your investment and make enough money to pay off yourcredit at the end of the game by investing in various asset classes.
         """ )         
         
    stage_1()
        
    #ROUND ONE   
        
def stage_1 ():
    global player_name
    global investment_fund_option_1
    global investment_fund_option_1end
    global investment_fund_option_2
    global investment_fund_option_2end
    global investment_fund_option_3
    global investment_fund_option_3end
    global investment_fund_option_5
    global investment_fund_option_6
    global first_interest
    global second_interest
    global third_interest
    global fourth_interest
    global fifth_interest
    global final_interest
    global player_investment_value
    global player_investment_value_2
    global total_loan_repayment
    global option_1
    global option_2
    global option_3
    global option_4
    global option_5
    global option_6
    global three_tbonds_rate 
    global six_tbonds_rate
    global twelve_tbonds_rate
    global two_years_bonds_rate
    global three_years_bonds_rate
    global five_years_bonds_rate
    global balance_after_option_1
    global balance_after_option_2
    global balance_after_option_3
    global balance_after_option_4
    global balance_after_option_5
    global balance_after_option_6
    global investment_fund
    
    three_tbonds_rate = 0.01
    six_tbonds_rate = 0.02
    twelve_tbonds_rate = 0.03 
    two_years_bonds_rate = 0.04 
    three_years_bonds_rate = 0.05
    five_years_bonds_rate = 0.06
    investment_fund = 10000
 
    print("Cash FLow")  
    
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
          To help you understand your options {player_name}, Jane, your superb fiancial advisor will take some time to explain some concepts.
          """)
    
    input( '< Press any key to continue > \n')
    
    print(f"""
          Hi {player_name}, I'm Jane and I'm here to shed some light on your investment options. 
          
          If you're wondering what a stock is,it is basically an investment (or asset_class) that signifies proportionate ownership in the issuing corporation. Stocks are risky but provide above normal returns on your investments.
          
          Private equity fund is an investment (or asset_class) that signifies proportionate ownership in the issuing in private companies. More risky than stocks but also provide above normal returns.
          
          You see, it is quite straight forward.
          
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
          
    input(f""" Please press any key to continue 
          {'-'* 50}
          """)  
    
    print("""\n
          You have $10,000 bank given to you as a loan and running at the rate of 7% per annum. Remember you need to make enough money to pay back both principal and interest.
          
          Now, you have to decide on your first investment and how much you would like to apportion per round.
          
          """)
    
    input(' < Please press any key to continue >')    
    
    
    investment_fund_option_1 = input('How much would you like to invest: ') 
    
    while True:
        
        try:
            
            
            
            TypeError
            
            investment_fund_option_1 = input('How much would you like to invest? Please enter a figure less han $10,000: ')
            
            break
        
        except: ValueError
        
        print=('figures please')
        
    
    
    print(f"Awesome!!! You have decided on investing {investment_fund_option_1}")
    
    if investment_fund_option_1 >= investment_fund:
        
        print(f""" Error!!! Please input value less than {investment_fund}""")
        
        investment_fund_option_1 = input('How much would you like to invest: ')
            
        print(f""" Error!!! Please input value less than {investment_fund}""")
        
        investment_fund_option_1 = input('How much would you like to invest: ')
    else:
        print(f"\nAwesome!!! You have decided on investing {investment_fund_option_1}")
    
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
    
    investment_fund_option_1 = int(float(f"{investment_fund_option_1}"))
    
    
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
            
                    first_interest =  int(investment_fund_option_1) * three_tbonds_rate
            
                    print(f'Your expected interest in 3 months is ${first_interest}. All things being equal. ')
                    break
                
                if t_bonds_option_1.upper() == "B":
            
                    first_interest =  int(investment_fund_option_1) *six_tbonds_rate
            
                    print(f'Your expected interest in 6 months is ${first_interest}. All things being equal.  ')
                    break
                
                if t_bonds_option_1.upper() == "C":
            
                    first_interest = int(investment_fund_option_1) * twelve_tbonds_rate
            
                    print(f'Your expected interest in 12 months is ${first_interest}.All things being equal.  ')
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
            
                first_interest = int(investment_fund_option_1) * two_years_bonds_rate
            
                print(f'Your expected interest per annum is ${first_interest} for the next 2 years. All things being equal. ')
                break
            
            if bonds_option_1.upper() == "B":
            
                first_interest = int(investment_fund_option_1) * three_years_bonds_rate
            
                print(f'Your expected interest per annum is is ${first_interest} for the next 3 years. All things being equal.  ')
                break
            
            if bonds_option_1.upper() == "C":
            
                first_interest = int(investment_fund_option_1) * five_years_bonds_rate
            
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
                first_interest= three_tbonds_rate * int(investment_fund_option_1)
            if SP_guess == 2:
                first_interest = six_tbonds_rate * int(investment_fund_option_1)
                
            if SP_guess == 3:
                first_interest = three_years_bonds_rate * int(investment_fund_option_1)
            break
    
        elif option_1.upper() == "D":
            
            first_interest= three_tbonds_rate * int(investment_fund_option_1)
            print(f" You have invested ${investment_fund_option_1} in the Private equity fund.")
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
    if economic_variable == 2 :
        
        print("""
              News Flash: Deflation!!!
              
              The Federal Bureau of Statistics reports a general decrease in prices of goods and services.
              Typically this leads to decrease in rates and stock prices might decrease or increase
              """)
    if economic_variable == 3 :
        
        print("""
               News Flash: Economic Meltdown !!!
              
              The Federal Bureau of Statistics reports an Economic Meltdown!!!.
              temporary disruption in economic activities which leads to rates decrease and fall in stock prices.
              """)
    if economic_variable == 4 :
        
        print("""
               News Flash: Unemployment rate: high!!!
              
              The Federal Bureau of Statistics reports an increase the Unemployment rate.
                A rise in unemployment rate leads to decrease in rate and a fall in stock prices.
              """)
        
    if economic_variable == 5 :
        
        print("""
               News Flash: Unemployment rate: low!!!
              
               The Federal Bureau of Statistics reports an decrease the Unemployment rate.
              A fall in unemployment rate leads to an increase in rate and an increase in stock prices.
              """)
        
    if economic_variable == 6 :
        
        print("""
               News Flash: GDP: lower!!!
        
              The Federal Bureau of Statistics reports a decrease in GDP.
              Gross Domestic product is the summation of all economic goods and services produced by nationals of a country. 
              A rise in GDP leads to rise in stocks and fall in rates. 
              A fall in GDP leads more likely to a fall in stock prices and a rise in rates
              """)    
    
    if economic_variable == 7 :
        
        print("""
               News Flash: GDP: higher!!!
              
              The Federal Bureau of Statistics reports an increase in GDP.
              Gross Domestic product is the summation of all economic goods and services produced by nationals of a country. 
              A rise in GDP leads to more likely to rise in stocks and fall in rates. 
              
              """)   
    if economic_variable == 8 :
        
        print("""
               News Flash: Fire harzard dirupts economic activities !!!
              
              The Federal Bureau of Statistics reports an environmental disruption in the economy.
              Typically this leads likely to increase in rates and stock prices might decrease or increase
              """)       
        
    if economic_variable == 9 :
        
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
            
            investment_fund_option_1end = investment_fund_option_1
        
        if option_1.upper() == "C" or "D":
            
            if stocks_rise_fall == 1:
                
                investment_fund_option_1end = int(investment_fund_option_1) * 1.20
            
                print(f"""
                  Invested amount in stocks or private equity fund has increased by 20% to 
                  {investment_fund_option_1end}    
                     """)
            if stocks_rise_fall == 0:
                
                investment_fund_option_1end = int(investment_fund_option_1) * 0.95
            
                print(f"""
                  Invested amount in stocks or private equity fund has decreased by 5% to 
                  {investment_fund_option_1end} 
                  """)
    
    if economic_variable == 2: 
    
        if option_1.upper() == "A" or "B":
        
            three_tbonds_rate = three_tbonds_rate + 0.005
        
            six_tbonds_rate = six_tbonds_rate + 0.005
        
            twelve_tbonds_rate = twelve_tbonds_rate + 0.005
        
            two_years_bonds_rate = two_years_bonds_rate + 0.005
        
            three_years_bonds_rate = three_years_bonds_rate + 0.005
        
            five_years_bonds_rate = five_years_bonds_rate + 0.005
            
            investment_fund_option_1end = investment_fund_option_1
        
        if option_1.upper() == "C" or "D":
            
            if stocks_rise_fall == 1:
                
                investment_fund_option_1end = investment_fund_option_1 * 1.20
            
                print(f"""
                  Invested amount in stocks or private equity fund has increased by 20% to 
                  {investment_fund_option_1end}    
                     """)
            if stocks_rise_fall == 0:
                
                investment_fund_option_1end = investment_fund_option_1 * 0.95
            
                print(f"""
                  Invested amount in stocks or private equity fund has decreased by 5% to 
                  {investment_fund_option_1end} 
                  """)           
    
    if economic_variable == 3: 
    
        if option_1.upper() == "A" or "B":
        
            three_tbonds_rate = three_tbonds_rate - 0.005
        
            six_tbonds_rate = six_tbonds_rate - 0.005
        
            twelve_tbonds_rate = twelve_tbonds_rate - 0.005
        
            two_years_bonds_rate = two_years_bonds_rate - 0.005
        
            three_years_bonds_rate = three_years_bonds_rate - 0.005
        
            five_years_bonds_rate = five_years_bonds_rate - 0.005
            
            investment_fund_option_1end = investment_fund_option_1
        
        if option_1.upper() == "C" or "D":
            
            investment_fund_option_1end = investment_fund_option_1 * 0.95
            
            print(f"""
                  Invested amount in stocks or private equity fund has decreased by 5% to 
                  {investment_fund_option_1end} 
                  """)
    if economic_variable == 4: 
    
        if option_1.upper() == "A" or "B":
        
            three_tbonds_rate = three_tbonds_rate - 0.005
        
            six_tbonds_rate = six_tbonds_rate - 0.005
        
            twelve_tbonds_rate = twelve_tbonds_rate - 0.005
        
            two_years_bonds_rate = two_years_bonds_rate - 0.005
        
            three_years_bonds_rate = three_years_bonds_rate - 0.005
        
            five_years_bonds_rate = five_years_bonds_rate - 0.005
            
            investment_fund_option_1end = investment_fund_option_1
            
        
        if option_1.upper() == "C" or "D":
            
            investment_fund_option_1end = investment_fund_option_1 * 0.95
            
            print(f"""
                  Invested amount in stocks or private equity fund has decreased by 5% to 
                  {investment_fund_option_1end}
                  """)
    
    if economic_variable == 5: 
    
        if option_1.upper() == "A" or "B":
        
            three_tbonds_rate = three_tbonds_rate + 0.005
        
            six_tbonds_rate = six_tbonds_rate + 0.005
        
            twelve_tbonds_rate = twelve_tbonds_rate + 0.005
        
            two_years_bonds_rate = two_years_bonds_rate + 0.005
        
            three_years_bonds_rate = three_years_bonds_rate + 0.005
        
            five_years_bonds_rate = five_years_bonds_rate + 0.005
            
            investment_fund_option_1end = investment_fund_option_1
        
        if option_1.upper() == "C" or "D":
                
                investment_fund_option_1end = investment_fund_option_1 * 1.20
            
                print(f"""
                  Invested amount in stocks or private equity fund has increased by 20% to 
                  {investment_fund_option_1end}    
                     """)
                     
                
    if economic_variable == 6: 
    
        if option_1.upper() == "A" or "B":
        
            three_tbonds_rate = three_tbonds_rate + 0.005
        
            six_tbonds_rate = six_tbonds_rate + 0.005
        
            twelve_tbonds_rate = twelve_tbonds_rate + 0.005
        
            two_years_bonds_rate = two_years_bonds_rate + 0.005
        
            three_years_bonds_rate = three_years_bonds_rate + 0.005
        
            five_years_bonds_rate = five_years_bonds_rate + 0.005
            
            investment_fund_option_1end = investment_fund_option_1
        
        if option_1.upper() == "C" or "D":
            
            investment_fund_option_1end = investment_fund_option_1 * 0.95
            
            print(f"""
                  Invested amount in stocks or private equity fund has decreased by 5% to 
                  {investment_fund_option_1end}
                  """)
    
    if economic_variable == 7: 
    
        if option_1.upper() == "A" or "B":
        
            three_tbonds_rate = three_tbonds_rate - 0.005
        
            six_tbonds_rate = six_tbonds_rate - 0.005
        
            twelve_tbonds_rate = twelve_tbonds_rate  - 0.005
        
            two_years_bonds_rate = two_years_bonds_rate  - 0.005
        
            three_years_bonds_rate = three_years_bonds_rate - 0.005
        
            five_years_bonds_rate = five_years_bonds_rate - 0.005
            
            investment_fund_option_1end = investment_fund_option_1
        
        if option_1.upper() == "C" or "D":
             
            investment_fund_option_1end = investment_fund_option_1 * 1.20
            
            print(f"""
                  Invested amount in stocks or private equity fund has increased by 20% to 
                  {investment_fund_option_1end}    
                  """)
    
    
    if economic_variable == 8: 
    
        if option_1.upper() == "A" or "B":
        
            three_tbonds_rate = three_tbonds_rate + 0.005
        
            six_tbonds_rate = six_tbonds_rate + 0.005
        
            twelve_tbonds_rate = twelve_tbonds_rate + 0.005
        
            two_years_bonds_rate = two_years_bonds_rate + 0.005
        
            three_years_bonds_rate = three_years_bonds_rate + 0.005
        
            five_years_bonds_rate = five_years_bonds_rate + 0.005
            
            investment_fund_option_1end = investment_fund_option_1
        
        if option_1.upper() == "C" or "D":
            
            if stocks_rise_fall == 1:
                
                investment_fund_option_1end = investment_fund_option_1 * 1.20
            
                print(f"""
                  Invested amount in stocks or private equity fund has increased by 20% to 
                  {investment_fund_option_1end}    
                     """)
            if stocks_rise_fall == 0:
                
                investment_fund_option_1end = investment_fund_option_1 * 0.95
            
                print(f"""
                  Invested amount in stocks or private equity fund has decreased by 5% to 
                  {investment_fund_option_1end}
                  """) 
    
    if economic_variable == 9: 
       
        print (f"Economy is stable for now {player_name}.")
        
                            
        three_tbonds_rate = three_tbonds_rate
        
        six_tbonds_rate = six_tbonds_rate
        
        twelve_tbonds_rate = twelve_tbonds_rate
        
        two_years_bonds_rate = two_years_bonds_rate 
        
        three_years_bonds_rate = three_years_bonds_rate 
        
        five_years_bonds_rate = five_years_bonds_rate
        
        investment_fund_option_1end = investment_fund_option_1
        
        
    input("Press enter to continue")
    
    total_value_round_1 = investment_fund_option_1end + first_interest   
    
    #ROUND 2
    
    print(f""" Welcome {player_name}!!! to another round of investing. I'm sure you're getting a hang of it. Jane your financial advisor will send your your account info in a moment.
          """)
    
    input("Press enter to continue")
    
    print(f"""
          Dear {player_name},
          
          This the end of the first stage.
          
          I hope the news flash hasn't bogged you down one bit.
          
          I just want to give you an update on how you have done so far.
         
          
{'-'* 50}          
Stage   |       Investment value	                 Interest earned           Total value 

ROUND1  |       ${investment_fund_option_1end}     {first_interest}        {total_value_round_1}

{'-'* 50} 	
 
          Sincerely,
          
          Jane
 		
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
            
                    second_interest = int(investment_fund_option_2) * three_tbonds_rate
            
                    print(f'Your expected interest is ${second_interest}. All things being equal. Good luck')
                    break
                
                elif t_bonds_option_2.upper() == "B":
            
                    second_interest = int(investment_fund_option_2) *six_tbonds_rate
            
                    print(f'Your expected interest is ${second_interest}. All things being equal. Good luck  ')
                    break
                
                elif t_bonds_option_2.upper() == "C":
            
                    second_interest = (investment_fund_option_2) * twelve_tbonds_rate
            
                    print(f'Your expected interest is ${second_interest}.All things being equal. Good luck ')
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
            
                second_interest = int(investment_fund_option_2) * two_years_bonds_rate
            
                print(f'Your expected interest is ${second_interest} . All things being equal. Good luck ')
                break
            
            elif bonds_option_2.upper() == "B":
            
                first_interest = int(investment_fund_option_2) * three_years_bonds_rate
            
                print(f'Your expected interest is is ${second_interest}. All things being equal. Good luck  ')
                break
            
            elif bonds_option_2.upper() == "C":
            
                second_interest = int(investment_fund_option_2) * five_years_bonds_rate
            
                print(f'Your expected interest is ${second_interest} . All things being equal. Good luck ')
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
                second_interest= three_tbonds_rate * investment_fund_option_2
                print(f'Your expected profit is ${second_interest} . All things being equal. Good luck ')
            if SP_guess == 2:
                second_interest = three_years_bonds_rate * investment_fund_option_2
                print(f'Your expected profit is ${second_interest} . All things being equal. Good luck ')
                
            if SP_guess == 3:
                second_interest = six_tbonds_rate * investment_fund_option_2
                print(f'Your expected profit is ${second_interest} . All things being equal. Good luck ')
            break
    
        elif option_2.upper() == "D":
        
            print(f" You have invested ${investment_fund_option_2} in the Private equity fund.")
            second_interest= three_tbonds_rate  * investment_fund_option_2
            print(f'Your expected profit is ${second_interest} . All things being equal. Good luck ')
            break
    
        else:     
            print("\n Error!! Please select option A, B, C or D. ")
            continue
    
        
    input( '< Press enter to proceed > \n')
    
    balance_after_option_2 = investment_fund - investment_fund_option_1 - investment_fund_option_2
    
    
    total_value_round_2 = investment_fund_option_2 + second_interest
    
    print(f"""
          Your current invested amount in round one and two is  ${investment_fund_option_1} and ${investment_fund_option_2} respectively and you have ${balance_after_option_2} unused.
          
          Good Job {player_name}. Happy investing and always remember when life throws you lemon, you do what?
          
          That's right, you make lemonades.
          
          Good luck !!!
          
          """)
    
    input("Press enter to continue")
    
    print(f"""
          Dear {player_name},
          
          This the end of the first stage.
          
          I hope the news flash hasn't bogged you down one bit.
          
          I just want to give you an update on how you have done so far.
         
          
{'-'* 80} 
         
Stage   |       Investment value	                 Interest earned           Total value 

ROUND1  |       ${investment_fund_option_1end}     {first_interest}        {total_value_round_1}
	
ROUND2  |       ${investment_fund_option_2}     {second_interest}       {total_value_round_2}

{'-'* 80}     
          Sincerely,
          
          Jane
	
        """)
    
    input("Press enter to continue")
      
    print (balance_after_option_2)
    
    total_loan_repayment = int(investment_fund) * 1.05
    
    print( f""" 
          {'-'* 50} 
    Total loan replayment amount is ${total_loan_repayment}"
          {'-'* 50} 
          """)
    
    
    player_investment_value = investment_fund_option_1end +investment_fund_option_2 + (first_interest )+ second_interest
    
    
    if player_investment_value < total_loan_repayment:
        
        difference = total_loan_repayment - player_investment_value
        
        print (f"Game Over!!! You are ${difference} short.")
        
        fail()
        exit
        
    stage_2(stage_1)
    
    
def fail():
    print(f"""
              Cash Flow
             
                    """)
    
    print(f"Would you like to play again? (Yes/No)")
    replay = input("> ")
    replay = replay.lower()
    
    if replay == 'yes':
        stage_1()
        
    else:
        print(f" Thanks for playing ")
        exit(0)

    

#STAGE 2   ROUND 3
        
def stage_2(stage_1):   
    global player_name
    global investment_fund_option_1
    global investment_fund_option_1end
    global investment_fund_option_2
    global investment_fund_option_3
    global investment_fund_option_4
    global investment_fund_option_5
    global investment_fund_option_6
    global first_interest
    global second_interest
    global third_interest
    global fourth_interest
    global fifth_interest
    global final_interest
    global player_investment_value
    global player_investment_value_2
    global total_loan_repayment
    global option_1
    global option_2
    global option_3
    global option_4
    global option_5
    global option_6
    global three_tbonds_rate 
    global six_tbonds_rate
    global twelve_tbonds_rate
    global two_years_bonds_rate
    global three_years_bonds_rate
    global five_years_bonds_rate
    global balance_after_option_1
    global balance_after_option_2
    global balance_after_option_3
    global balance_after_option_4
    global balance_after_option_5
    global balance_after_option_6
    global investment_fund
     
    print (f"""" Welcome to stage 2!!! Congrats you made it
           You have ${player_investment_value}!!! Keep it up.
           """)
   
    input("Please press enter to continue")
    
    three_tbonds_rate = 0.01
    six_tbonds_rate = 0.02
    twelve_tbonds_rate = 0.03 
    two_years_bonds_rate = 0.04 
    three_years_bonds_rate = 0.05
    five_years_bonds_rate = 0.06
    
    
    economic_variable = random.randint(1,9)
    
    #investment_fund_option_1 = investment_fund_option_1 + first_interest
    
    #other variables Economic conditions
    
    if economic_variable == 1 :
        
        print("""
               News Flash: Inflation!!!
              
              The Federal Bureau of Statistics reports a general increase in prices of goods and services.
              Typically this leads to increase in rates and stock prices might decrease or increase
              """)
    if economic_variable == 2 :
        
        print("""
              News Flash: Deflation!!!
              
              The Federal Bureau of Statistics reports a general decrease in prices of goods and services.
              Typically this leads to decrease in rates and stock prices might decrease or increase
              """)
    if economic_variable == 3 :
        
        print("""
               News Flash: Economic Meltdown !!!
              
              The Federal Bureau of Statistics reports an Economic Meltdown!!!.
              temporary disruption in economic activities which leads to rates decrease and fall in stock prices.
              """)
    if economic_variable == 4 :
        
        print("""
               News Flash: Unemployment rate: high!!!
              
              The Federal Bureau of Statistics reports an increase the Unemployment rate.
                A rise in unemployment rate leads to decrease in rate and a fall in stock prices.
              """)
        
    if economic_variable == 5 :
        
        print("""
               News Flash: Unemployment rate: low!!!
              
               The Federal Bureau of Statistics reports an decrease the Unemployment rate.
              A fall in unemployment rate leads to an increase in rate and an increase in stock prices.
              """)
        
    if economic_variable == 6 :
        
        print("""
               News Flash: GDP: lower!!!
        
              The Federal Bureau of Statistics reports a decrease in GDP.
              Gross Domestic product is the summation of all economic goods and services produced by nationals of a country. 
              A rise in GDP leads to rise in stocks and fall in rates. 
              A fall in GDP leads more likely to a fall in stock prices and a rise in rates
              """)    
    
    if economic_variable == 7 :
        
        print("""
               News Flash: GDP: higher!!!
              
              The Federal Bureau of Statistics reports an increase in GDP.
              Gross Domestic product is the summation of all economic goods and services produced by nationals of a country. 
              A rise in GDP leads to more likely to rise in stocks and fall in rates. 
              
              """)   
    if economic_variable == 8 :
        
        print("""
               News Flash: Fire harzard dirupts economic activities !!!
              
              The Federal Bureau of Statistics reports an environmental disruption in the economy.
              Typically this leads likely to increase in rates and stock prices might decrease or increase
              """)       
        
    if economic_variable == 9 :
        
                            
        three_tbonds_rate_2 = three_tbonds_rate
        
        six_tbonds_rate_2 = six_tbonds_rate
        
        twelve_tbonds_rate_2 = twelve_tbonds_rate
        
        two_years_bonds_rate_2 = two_years_bonds_rate 
        
        three_years_bonds_rate_2 = three_years_bonds_rate 
        
        five_years_bonds_rate_2 = five_years_bonds_rate
        
        investment_fund_option_2end = investment_fund_option_2
        
        print("""
               News Flash: Economy: Stable!!!
              
              The Federal Bureau of Statistics reports stabiliy and no threat to current status quo in the economy
              """)   
    
    print("economic variable: ", economic_variable)
    
    stocks_rise_fall = random.randint(0,1)
    
    print("stock rise or fall: ", stocks_rise_fall)
    
    if economic_variable == 1: 
    
        if option_2.upper() == "A" or "B":
        
            three_tbonds_rate_2 = three_tbonds_rate - 0.005
            six_tbonds_rate_2 = six_tbonds_rate - 0.005
        
            twelve_tbonds_rate_2= twelve_tbonds_rate - 0.005
        
            two_years_bonds_rate_2= two_years_bonds_rate - 0.005
        
            three_years_bonds_rate_2= three_years_bonds_rate - 0.005
        
            five_years_bonds_rate_2=  five_years_bonds_rate - 0.005
            
            investment_fund_option_2end = investment_fund_option_2
        
        if option_2.upper() == "C" or "D":
            
            if stocks_rise_fall == 1:
                
                investment_fund_option_2end = investment_fund_option_2 * 1.20
            
                print(f"""
                  Invested amount in stocks or private equity fund has increased by 20% to 
                  {investment_fund_option_2end}    
                     """)
            if stocks_rise_fall == 0:
                
                investment_fund_option_2end = investment_fund_option_2 * 0.95
            
                print(f"""
                  Invested amount in stocks or private equity fund has decreased by 5% to 
                  {investment_fund_option_2end} 
                  """)
    
    if economic_variable == 2: 
    
        if option_2.upper() == "A" or "B":
        
            three_tbonds_rate_2 = three_tbonds_rate + 0.005
        
            six_tbonds_rate_2 = six_tbonds_rate + 0.005
        
            twelve_tbonds_rate_2 = twelve_tbonds_rate + 0.005
        
            two_years_bonds_rate_2 = two_years_bonds_rate + 0.005
        
            three_years_bonds_rate_2 = three_years_bonds_rate + 0.005
        
            five_years_bonds_rate_2 = five_years_bonds_rate + 0.005
            
            investment_fund_option_2end = investment_fund_option_2
        
        if option_2.upper() == "C" or "D":
            
            if stocks_rise_fall == 1:
                
                investment_fund_option_2end = investment_fund_option_2 * 1.20
            
                print(f"""
                  Invested amount in stocks or private equity fund has increased by 20% to 
                  {investment_fund_option_2end}    
                     """)
            if stocks_rise_fall == 0:
                
                investment_fund_option_2end = investment_fund_option_2 * 0.95
            
                print(f"""
                  Invested amount in stocks or private equity fund has decreased by 5% to 
                  {investment_fund_option_2end} 
                  """)           
    
    if economic_variable == 3: 
    
        if option_2.upper() == "A" or "B":
        
            three_tbonds_rate_2 = three_tbonds_rate - 0.005
        
            six_tbonds_rate_2 = six_tbonds_rate - 0.005
        
            twelve_tbonds_rate_2 = twelve_tbonds_rate - 0.005
        
            two_years_bonds_rate_2 = two_years_bonds_rate - 0.005
        
            three_years_bonds_rate_2 = three_years_bonds_rate - 0.005
        
            five_years_bonds_rate_2 = five_years_bonds_rate - 0.005
            
            investment_fund_option_2end = investment_fund_option_2
        
        if option_2.upper() == "C" or "D":
            
            investment_fund_option_2end = investment_fund_option_2 * 0.95
            
            print(f"""
                  Invested amount in stocks or private equity fund has decreased by 5% to 
                  {investment_fund_option_2end} 
                  """)
    if economic_variable == 4: 
    
        if option_2.upper() == "A" or "B":
        
            three_tbonds_rate_2 = three_tbonds_rate - 0.005
        
            six_tbonds_rate_2= six_tbonds_rate - 0.005
        
            twelve_tbonds_rate_2 = twelve_tbonds_rate - 0.005
        
            two_years_bonds_rate_2 = two_years_bonds_rate - 0.005
        
            three_years_bonds_rate_2 = three_years_bonds_rate - 0.005
        
            five_years_bonds_rate_2 = five_years_bonds_rate - 0.005
            
            investment_fund_option_2end = investment_fund_option_2
            
        
        if option_2.upper() == "C" or "D":
            
            investment_fund_option_2end = investment_fund_option_2 * 0.95
            
            print(f"""
                  Invested amount in stocks or private equity fund has decreased by 5% to 
                  {investment_fund_option_2end}
                  """)
    
    if economic_variable == 5: 
    
        if option_2.upper() == "A" or "B":
        
            three_tbonds_rate_2 = three_tbonds_rate + 0.005
        
            six_tbonds_rate_2 = six_tbonds_rate + 0.005
        
            twelve_tbonds_rate_2 = twelve_tbonds_rate + 0.005
        
            two_years_bonds_rate_2 = two_years_bonds_rate+ 0.005
        
            three_years_bonds_rate_2 = three_years_bonds_rate + 0.005
        
            five_years_bonds_rate_2 = five_years_bonds_rate + 0.005
            
            investment_fund_option_2end = investment_fund_option_2
        
        if option_2.upper() == "C" or "D":
                
                investment_fund_option_2end = investment_fund_option_2 * 1.20
            
                print(f"""
                  Invested amount in stocks or private equity fund has increased by 20% to 
                  {investment_fund_option_2end}    
                     """)
                     
                
    if economic_variable == 6: 
    
        if option_2.upper() == "A" or "B":
        
            three_tbonds_rate_2 = three_tbonds_rate + 0.005
        
            six_tbonds_rate_2 = six_tbonds_rate + 0.005
        
            twelve_tbonds_rate_2 = twelve_tbonds_rate + 0.005
        
            two_years_bonds_rate_2 = two_years_bonds_rate + 0.005
        
            three_years_bonds_rate_2 = three_years_bonds_rate + 0.005
        
            five_years_bonds_rate_2 = five_years_bonds_rate+ 0.005
            
            investment_fund_option_2end = investment_fund_option_2
        
        if option_2.upper() == "C" or "D":
            
            investment_fund_option_2end = investment_fund_option_2 * 0.95
            
            print(f"""
                  Invested amount in stocks or private equity fund has decreased by 5% to 
                  {investment_fund_option_2end}
                  """)
    
    if economic_variable == 7: 
    
        if option_2.upper() == "A" or "B":
        
            three_tbonds_rate_2 = three_tbonds_rate - 0.005
        
            six_tbonds_rate_2 = six_tbonds_rate - 0.005
        
            twelve_tbonds_rate_2 = twelve_tbonds_rate - 0.005
        
            two_years_bonds_rate_2 = two_years_bonds_rate - 0.005
        
            three_years_bonds_rate_2 = three_years_bonds_rate - 0.005
        
            five_years_bonds_rate_2 = five_years_bonds_rate - 0.005
            
            investment_fund_option_2end = investment_fund_option_2
        
        if option_2.upper() == "C" or "D":
             
            investment_fund_option_2end = investment_fund_option_2 * 1.20
            
            print(f"""
                  Invested amount in stocks or private equity fund has increased by 20% to 
                  {investment_fund_option_2end}    
                  """)
    
    
    if economic_variable == 8: 
    
        if option_2.upper() == "A" or "B":
        
            three_tbonds_rate_2 = three_tbonds_rate + 0.005
        
            six_tbonds_rate_2 = six_tbonds_rate + 0.005
        
            twelve_tbonds_rate_2 = twelve_tbonds_rate + 0.005
        
            two_years_bonds_rate_2 = two_years_bonds_rate + 0.005
        
            three_years_bonds_rate_2 = three_years_bonds_rate + 0.005
        
            five_years_bonds_rate_2 = five_years_bonds_rate + 0.005
            
            investment_fund_option_2end = investment_fund_option_2
        
        if option_2.upper() == "C" or "D":
            
            if stocks_rise_fall == 1:
                
                investment_fund_option_2end = investment_fund_option_2 * 1.20
            
                print(f"""
                  Invested amount in stocks or private equity fund has increased by 20% to 
                  {investment_fund_option_2end}    
                     """)
            if stocks_rise_fall == 0:
                
                investment_fund_option_2end = investment_fund_option_2 * 0.95
            
                print(f"""
                  Invested amount in stocks or private equity fund has decreased by 5% to 
                  {investment_fund_option_2end}
                  """) 
    
    if economic_variable == 9: 
       
        print (f"Economy is stable for now {player_name}.")
                    
        three_tbonds_rate_2 = three_tbonds_rate
        
        six_tbonds_rate_2 = six_tbonds_rate
        
        twelve_tbonds_rate_2 = twelve_tbonds_rate
        
        two_years_bonds_rate_2 = two_years_bonds_rate 
        
        three_years_bonds_rate_2 = three_years_bonds_rate 
        
        five_years_bonds_rate_2 = five_years_bonds_rate
        
        investment_fund_option_2end = investment_fund_option_2
        
        
    input("Press enter to continue")
    
    
    investment_fund_option_3 = input(f'How much would you like to invest from ${player_investment_value},your new approved loan amount: ')
    
    while True:
        
        try:
            investment_fund_option_3 = input('How much would you like to invest? Please enter a figure: ')  
        
            ValueError
            TypeError
            break
        
        except:
        
            print(f"Awesome!!! You have decided on investing {investment_fund_option_3}")
            break
        
    
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
               A: 3 months treasury bonds @ {three_tbonds_rate_2}
               B: 6 months treasury bonds @ {six_tbonds_rate_2}
               C: 12 month treasury bonds @ {twelve_tbonds_rate_2}
               """)
                
                if t_bonds_option_3.upper()== "A":
            
                    third_interest = int(investment_fund_option_3) * three_tbonds_rate_2
            
                    print(f'Your expected interest is ${third_interest}. All things being equal. ')
                    break
                
                elif t_bonds_option_3.upper() == "B":
            
                    third_interest =  int(investment_fund_option_3) *six_tbonds_rate_2
            
                    print(f'Your expected interest is ${third_interest}. All things being equal.  ')
                    break
                
                elif t_bonds_option_3.upper() == "C":
            
                    third_interest = int(investment_fund_option_3) * twelve_tbonds_rate_2
            
                    print(f'Your expected interest is ${third_interest}.All things being equal.  ')
                    break
                
                else:
                    print("Error!! Please select option A, B or C")
                    
        
        if option_3.upper() == "B":
        
            bonds_option_3 = input (f"""
                                
               Would you like to invest in 
               A: 2 years bonds @ {two_years_bonds_rate_2}
               B: 3 years bonds @ {three_years_bonds_rate_2}
               C: 5 years bonds @ {five_years_bonds_rate_2}
               """)
        
            if bonds_option_3.upper()== "A":
            
                third_interest = int(investment_fund_option_3) * two_years_bonds_rate_2
            
                print(f'Your expected interest per annum is ${third_interest} for the next 2 years. All things being equal. ')
                break
            
            elif bonds_option_3.upper() == "B":
            
                third_interest = int(investment_fund_option_3) * three_years_bonds_rate_2
            
                print(f'Your expected interest per annum is is ${third_interest} for the next 3 years. All things being equal.  ')
                break
            
            elif bonds_option_3.upper() == "C":
            
                third_interest = int(investment_fund_option_3) * five_years_bonds_rate_2
            
                print(f'Your expected interest per annum is ${third_interest} for the next 5 years. All things being equal.  ')
                break
                
            else:
                print("Error!! Please select option A, B or C")
            
                bonds_option_3 = input (f"""
                                
                Would you like to invest in 
               A: 2 years bonds @ {two_years_bonds_rate_2}
               B: 3 years bonds @ {three_years_bonds_rate_2}
               C: 5 years bonds @ {five_years_bonds_rate_2}
               """)
        elif option_3.upper() == "C":
    
            print(f"""
                  You have invested ${investment_fund_option_3} in the S&P index stock fund.
                  """)
            SP_guess = random.randint(1,3)
            if SP_guess == 1:
                third_interest = three_tbonds_rate_2 * investment_fund_option_3
            elif SP_guess == 2:
                third_interest = three_tbonds_rate_2 * investment_fund_option_3
                
            elif SP_guess == 3:
                third_interest = six_tbonds_rate_2 * investment_fund_option_3
            break
    
        elif option_3.upper() == "D":
            third_interest = three_tbonds_rate_2 * investment_fund_option_3
            
            print(f" You have invested ${investment_fund_option_3} in the Private equity fund.")
            break
    
        else:     
            print("\n Error!! Please select option A, B, C or D. ")
            continue
    
        
    input( '< Press enter to proceed > \n')
    
    balance_after_option_3 = player_investment_value - int(float(investment_fund_option_3))
    
    total_value_round_1 = investment_fund_option_1 + first_interest
    total_value_round_2 = investment_fund_option_2end + second_interest
    total_value_round_3a = investment_fund_option_3 + third_interest
    
    print(f"""
          Your current invested amount is you have ${balance_after_option_3} to invest in the next round.
          
          Good Job {player_name}. Happy investing and always remember when life throws you lemon, you do what?
          
          That's right, you make lemonades.
          
          Good luck on your next round of investments!!!
          
          """)
    
    input( '< Press enter to proceed > \n')
    
    print(f"""
          Dear {player_name},
          
          This the end of the first stage.
          
          I hope the news flash hasn't bogged you down one bit.
          
          I just want to give you an update on how you have done so far.
         
          
{'-'* 80} 
         
Stage   |       Investment value	                 Interest earned           Total value 

ROUND1  |       ${investment_fund_option_1}         {first_interest}        {total_value_round_1}
	
ROUND2  |       ${investment_fund_option_2end}      {second_interest}       {total_value_round_2}

ROUND3  |       ${investment_fund_option_3}         {first_interest}        {total_value_round_3a}

{'-'* 80}     
          Sincerely,
          
          Jane
	
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
        
            three_tbonds_rate_3 = three_tbonds_rate - 0.005
            six_tbonds_rate_3 = six_tbonds_rate - 0.005
        
            twelve_tbonds_rate_3= twelve_tbonds_rate - 0.005
        
            two_years_bonds_rate_3= two_years_bonds_rate - 0.005
        
            three_years_bonds_rate_3= three_years_bonds_rate - 0.005
        
            five_years_bonds_rate_3=  five_years_bonds_rate - 0.005
            
            investment_fund_option_3end = investment_fund_option_3 
        
        elif option_3.upper() == "C" or "D":
            
            if stocks_rise_fall == 1:
                
                investment_fund_option_3end = investment_fund_option_3 * 1.20
            
                print(f"""
                  Invested amount in stocks or private equity fund has increased by 20% to 
                  {investment_fund_option_3end}    
                     """)
            elif stocks_rise_fall == 0:
                
                investment_fund_option_3end = investment_fund_option_3 * 0.95
            
                print(f"""
                  Invested amount in stocks or private equity fund has decreased by 5% to 
                  {investment_fund_option_3end} 
                  """)
    
    if economic_variable == 2: 
    
        if option_3.upper() == "A" or "B":
        
            three_tbonds_rate_3 = three_tbonds_rate + 0.005
        
            six_tbonds_rate_3 = six_tbonds_rate + 0.005
        
            twelve_tbonds_rate_3 = twelve_tbonds_rate + 0.005
        
            two_years_bonds_rate_3 = two_years_bonds_rate + 0.005
        
            three_years_bonds_rate_3 = three_years_bonds_rate + 0.005
        
            five_years_bonds_rate_3 = five_years_bonds_rate + 0.005
            
            investment_fund_option_3end = investment_fund_option_3 
        
        elif option_3.upper() == "C" or "D":
            
            if stocks_rise_fall == 1:
                
                investment_fund_option_3end = investment_fund_option_2 * 1.20
            
                print(f"""
                  Invested amount in stocks or private equity fund has increased by 20% to 
                  {investment_fund_option_3end}    
                     """)
            elif stocks_rise_fall == 0:
                
                investment_fund_option_3end = investment_fund_option_2 * 0.95
            
                print(f"""
                  Invested amount in stocks or private equity fund has decreased by 5% to 
                  {investment_fund_option_3end} 
                  """)           
    
    if economic_variable == 3: 
    
        if option_3.upper() == "A" or "B":
        
            three_tbonds_rate_3 = three_tbonds_rate - 0.005
        
            six_tbonds_rate_3 = six_tbonds_rate - 0.005
        
            twelve_tbonds_rate_3 = twelve_tbonds_rate - 0.005
        
            two_years_bonds_rate_3 = two_years_bonds_rate - 0.005
        
            three_years_bonds_rate_3 = three_years_bonds_rate - 0.005
        
            five_years_bonds_rate_3 = five_years_bonds_rate - 0.005
            
            investment_fund_option_3end = investment_fund_option_3 
        
        elif option_2.upper() == "C" or "D":
            
            investment_fund_option_3end = investment_fund_option_2 * 0.95
            
            print(f"""
                  Invested amount in stocks or private equity fund has decreased by 5% to 
                  {investment_fund_option_3end} 
                  """)
    if economic_variable == 4: 
    
        if option_3.upper() == "A" or "B":
        
            three_tbonds_rate_3 = three_tbonds_rate - 0.005
        
            six_tbonds_rate_3= six_tbonds_rate - 0.005
        
            twelve_tbonds_rate_3 = twelve_tbonds_rate - 0.005
        
            two_years_bonds_rate_3 = two_years_bonds_rate - 0.005
        
            three_years_bonds_rate_3 = three_years_bonds_rate - 0.005
        
            five_years_bonds_rate_3 = five_years_bonds_rate - 0.005
            
            investment_fund_option_3end = investment_fund_option_3 
            
        
        elif option_3.upper() == "C" or "D":
            
            investment_fund_option_3end = investment_fund_option_2 * 0.95
            
            print(f"""
                  Invested amount in stocks or private equity fund has decreased by 5% to 
                  {investment_fund_option_3end}
                  """)
    
    if economic_variable == 5: 
    
        if option_3.upper() == "A" or "B":
        
            three_tbonds_rate_3 = three_tbonds_rate + 0.005
        
            six_tbonds_rate_3 = six_tbonds_rate + 0.005
        
            twelve_tbonds_rate_3 = twelve_tbonds_rate + 0.005
        
            two_years_bonds_rate_3 = two_years_bonds_rate+ 0.005
        
            three_years_bonds_rate_3 = three_years_bonds_rate + 0.005
        
            five_years_bonds_rate_3 = five_years_bonds_rate + 0.005
            
            investment_fund_option_3end = investment_fund_option_3 
        
        elif option_3.upper() == "C" or "D":
                
                investment_fund_option_3end = investment_fund_option_2 * 1.20
            
                print(f"""
                  Invested amount in stocks or private equity fund has increased by 20% to 
                  {investment_fund_option_3end}    
                     """)
                     
                
    if economic_variable == 6: 
    
        if option_3.upper() == "A" or "B":
        
            three_tbonds_rate_3 = three_tbonds_rate + 0.005
        
            six_tbonds_rate_3 = six_tbonds_rate + 0.005
        
            twelve_tbonds_rate_3 = twelve_tbonds_rate + 0.005
        
            two_years_bonds_rate_3 = two_years_bonds_rate + 0.005
        
            three_years_bonds_rate_3 = three_years_bonds_rate + 0.005
        
            five_years_bonds_rate_3 = five_years_bonds_rate+ 0.005
            
            investment_fund_option_3end = investment_fund_option_3 
        
        elif option_3.upper() == "C" or "D":
            
            investment_fund_option_3end = investment_fund_option_2 * 0.95
            
            print(f"""
                  Invested amount in stocks or private equity fund has decreased by 5% to 
                  {investment_fund_option_3end}
                  """)
    
    if economic_variable == 7: 
    
        if option_3.upper() == "A" or "B":
        
            three_tbonds_rate_3 = three_tbonds_rate - 0.005
        
            six_tbonds_rate_3 = six_tbonds_rate - 0.005
        
            twelve_tbonds_rate_3 = twelve_tbonds_rate - 0.005
        
            two_years_bonds_rate_3 = two_years_bonds_rate - 0.005
        
            three_years_bonds_rate_3 = three_years_bonds_rate - 0.005
        
            five_years_bonds_rate_3 = five_years_bonds_rate - 0.005
            
            investment_fund_option_3end = investment_fund_option_3 
        
        elif option_2.upper() == "C" or "D":
             
            investment_fund_option_3end = investment_fund_option_2 * 1.20
            
            print(f"""
                  Invested amount in stocks or private equity fund has increased by 20% to 
                  {investment_fund_option_3end}    
                  """)
    
    
    if economic_variable == 8: 
    
        if option_3.upper() == "A" or "B":
        
            three_tbonds_rate_3 = three_tbonds_rate + 0.005
        
            six_tbonds_rate_3 = six_tbonds_rate + 0.005
        
            twelve_tbonds_rate_3 = twelve_tbonds_rate + 0.005
        
            two_years_bonds_rate_3 = two_years_bonds_rate + 0.005
        
            three_years_bonds_rate_3 = three_years_bonds_rate + 0.005
        
            five_years_bonds_rate_3 = five_years_bonds_rate + 0.005
            
            investment_fund_option_3end = investment_fund_option_3 
        
        elif option_3.upper() == "C" or "D":
            
            if stocks_rise_fall == 1:
                
                investment_fund_option_3end = investment_fund_option_2 * 1.20
            
                print(f"""
                  Invested amount in stocks or private equity fund has increased by 20% to 
                  {investment_fund_option_3end}    
                     """)
            if stocks_rise_fall == 0:
                
                investment_fund_option_3end = investment_fund_option_2 * 0.95
            
                print(f"""
                  Invested amount in stocks or private equity fund has decreased by 5% to 
                  {investment_fund_option_3end}
                  """) 
    
    if economic_variable == 9: 
        
        investment_fund_option_3end = investment_fund_option_3
       
        print (f"Economy is stable for now {player_name}.")
        
        
    input("Press enter to continue")
    
    total_value_round_3 = investment_fund_option_3end + third_interest
     
    print(f"""
          Dear {player_name},
          
          This the end of the first stage.
          
          I hope the news flash hasn't bogged you down one bit.
          
          I just want to give you an update on how you have done so far.
         
          
{'-'* 80} 
         
Stage   |       Investment value	                 Interest earned           Total value 

ROUND1  |       ${investment_fund_option_1end}     {first_interest}        {total_value_round_1}
	
ROUND2  |       ${investment_fund_option_2end}     {second_interest}       {total_value_round_2}

ROUND3  |       ${investment_fund_option_3end}     {third_interest}        {total_value_round_3}
	


{'-'* 80}     
          Sincerely,
          
          Jane
	
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
               A: 3 months treasury bonds @ {three_tbonds_rate_3}
               B: 6 months treasury bonds @ {six_tbonds_rate_3}
               C: 12 month treasury bonds @ {twelve_tbonds_rate_3}
               """)
                
                if t_bonds_option_4.upper()== "A":
            
                    fourth_interest = int(investment_fund_option_3) * three_tbonds_rate_3
            
                    print(f'Your expected interest is ${third_interest}. All things being equal. ')
                    break
                
                elif t_bonds_option_4.upper() == "B":
            
                    fourth_interest =  int(investment_fund_option_3) *six_tbonds_rate_3
            
                    print(f'Your expected interest is ${third_interest}. All things being equal.  ')
                    break
                
                elif t_bonds_option_4.upper() == "C":
            
                    fourth_interest = int(investment_fund_option_3) * twelve_tbonds_rate_3
            
                    print(f'Your expected interest is ${third_interest}.All things being equal.  ')
                    break
                
                else:
                    print("Error!! Please select option A, B or C")
                    
        
        if option_4.upper() == "B":
        
            bonds_option_4 = input (f"""
                                
               Would you like to invest in 
               A: 2 years bonds @ {two_years_bonds_rate_3}
               B: 3 years bonds @ {three_years_bonds_rate_3}
               C: 5 years bonds @ {five_years_bonds_rate_3}
               """)
        
            if bonds_option_4.upper()== "A":
            
                fourth_interest = int(investment_fund_option_4) * two_years_bonds_rate_3
            
                print(f'Your expected interest per annum is ${fourth_interest} for the next 2 years. All things being equal. ')
                break
            
            elif bonds_option_4.upper() == "B":
            
                fourth_interest = int(investment_fund_option_2) * three_years_bonds_rate_3
            
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
               A: 2 years bonds @ {two_years_bonds_rate_3}
               B: 3 years bonds @ {three_years_bonds_rate_3}
               C: 5 years bonds @ {five_years_bonds_rate_3}
               """)
                
        elif option_4.upper() == "C":
    
            print(f"""
                  You have invested ${investment_fund_option_4} in the S&P index stock fund.
                  """)
            SP_guess = random.randint(1,3)
            if SP_guess == 1:
                fourth_interest= -three_tbonds_rate_3 * investment_fund_option_1
            elif SP_guess == 2:
                fourth_interest = three_tbonds_rate_3 * investment_fund_option_1
                
            elif SP_guess == 3:
                fourth_interest = six_tbonds_rate_3 * investment_fund_option_1
            break
    
        elif option_4.upper() == "D":
            fourth_interest = six_tbonds_rate_3 * investment_fund_option_1
            print(f" You have invested ${investment_fund_option_4} in the Private equity fund.")
            break
    
        else:     
            print("\n Error!! Please select option A, B, C or D. ")
            continue
    
        
    input( '< Press enter to proceed > \n')
    
    balance_after_option_4 = player_investment_value - investment_fund_option_3-investment_fund_option_4
    
    total_value_round_2 = investment_fund_option_2 + second_interest
    
    print(f"""
          Your current invested amount in round one and two is  ${investment_fund_option_1} and ${investment_fund_option_2} respectively and you have ${balance_after_option_2} unused.
          
          Good Job {player_name}. Happy investing and always remember when life throws you lemon, you do what?
          
          That's right, you make lemonades.
          
          Good luck !!!
          
          """)
    
    input("Press enter to continue")
    
    total_value_round_1 = investment_fund_option_1 + first_interest
    total_value_round_2 = investment_fund_option_2end + second_interest
    total_value_round_3 = investment_fund_option_3end + third_interest
    total_value_round_4 = investment_fund_option_4 + fourth_interest
    
    print(f"""
          Dear {player_name},
          
          This the end of the first stage.
          
          I hope the news flash hasn't bogged you down one bit.
          
          I just want to give you an update on how you have done so far.
         
          
{'-'* 80} 
         
Stage   |       Investment value	                 Interest earned           Total value 

ROUND1  |       ${investment_fund_option_1end}     {first_interest}        {total_value_round_1}
	
ROUND2  |       ${investment_fund_option_2end}     {second_interest}       {total_value_round_2}

ROUND3  |       ${investment_fund_option_3end}     {third_interest}        {total_value_round_3}
	
ROUND4  |       ${investment_fund_option_4}        {fourth_interest}       {total_value_round_4}

{'-'* 80}     
          Sincerely,
          
          Jane
	
        """)
    
    input("Press enter to continue")
      
    print (balance_after_option_4)
    
    total_loan_repayment = int(investment_fund) * 1.07 + (player_investment_value * 1.07)
    
    print( f""" 
          {'-'* 50} 
    Total loan replayment amount is ${total_loan_repayment}"
          {'-'* 50} 
          """)
    
    
    player_investment_value_2 = investment_fund_option_1end +investment_fund_option_2end + investment_fund_option_3end +investment_fund_option_4+ first_interest + second_interest +third_interest+fourth_interest
    
    
    if player_investment_value_2 < total_loan_repayment:
        
        difference = total_loan_repayment - player_investment_value
        
        print (f"Game Over!!! You are ${difference} short.")
        
        fail()
        exit
        
    stage_3(stage_1,stage_2)

#ROUND 5 FINAL STAGE
        
def stage_3(stage_1,stage_2): 
    
    global player_investment_value_2
    global investment_fund_option_4
    global fourth_interest
    
    print (f"""" Welcome to the final stage 2!!! Congrats you made it
           You have ${player_investment_value_2}!!! Keep it up.
           """)
   
    input("Please press enter to continue")
    
    three_tbonds_rate = 0.01
    six_tbonds_rate = 0.015
    twelve_tbonds_rate = 0.025 
    two_years_bonds_rate = 0.035
    three_years_bonds_rate = 0.045
    five_years_bonds_rate = 0.055
    
    
    economic_variable = random.randint(1,9)
    
    #investment_fund_option_1 = investment_fund_option_1 + first_interest
    
    #other variables Economic conditions
    
    if economic_variable == 1 :
        
        print("""
               News Flash: Inflation!!!
              
              The Federal Bureau of Statistics reports a general increase in prices of goods and services.
              Typically this leads to increase in rates and stock prices might decrease or increase
              """)
    if economic_variable == 2 :
        
        print("""
              News Flash: Deflation!!!
              
              The Federal Bureau of Statistics reports a general decrease in prices of goods and services.
              Typically this leads to decrease in rates and stock prices might decrease or increase
              """)
    if economic_variable == 3 :
        
        print("""
               News Flash: Economic Meltdown !!!
              
              The Federal Bureau of Statistics reports an Economic Meltdown!!!.
              temporary disruption in economic activities which leads to rates decrease and fall in stock prices.
              """)
    if economic_variable == 4 :
        
        print("""
               News Flash: Unemployment rate: high!!!
              
              The Federal Bureau of Statistics reports an increase the Unemployment rate.
                A rise in unemployment rate leads to decrease in rate and a fall in stock prices.
              """)
        
    if economic_variable == 5 :
        
        print("""
               News Flash: Unemployment rate: low!!!
              
               The Federal Bureau of Statistics reports an decrease the Unemployment rate.
              A fall in unemployment rate leads to an increase in rate and an increase in stock prices.
              """)
        
    if economic_variable == 6 :
        
        print("""
               News Flash: GDP: lower!!!
        
              The Federal Bureau of Statistics reports a decrease in GDP.
              Gross Domestic product is the summation of all economic goods and services produced by nationals of a country. 
              A rise in GDP leads to rise in stocks and fall in rates. 
              A fall in GDP leads more likely to a fall in stock prices and a rise in rates
              """)    
    
    if economic_variable == 7 :
        
        print("""
               News Flash: GDP: higher!!!
              
              The Federal Bureau of Statistics reports an increase in GDP.
              Gross Domestic product is the summation of all economic goods and services produced by nationals of a country. 
              A rise in GDP leads to more likely to rise in stocks and fall in rates. 
              
              """)   
    if economic_variable == 8 :
        
        print("""
               News Flash: Fire harzard dirupts economic activities !!!
              
              The Federal Bureau of Statistics reports an environmental disruption in the economy.
              Typically this leads likely to increase in rates and stock prices might decrease or increase
              """)       
        
    if economic_variable == 9 :
        
                            
        three_tbonds_rate_4 = three_tbonds_rate
        
        six_tbonds_rate_4 = six_tbonds_rate
        
        twelve_tbonds_rate_4 = twelve_tbonds_rate
        
        two_years_bonds_rate_4 = two_years_bonds_rate 
        
        three_years_bonds_rate_4 = three_years_bonds_rate 
        
        five_years_bonds_rate_4 = five_years_bonds_rate
        
        investment_fund_option_4end = investment_fund_option_4
        
        print("""
               News Flash: Economy: Stable!!!
              
              The Federal Bureau of Statistics reports stabiliy and no threat to current status quo in the economy
              """)   
    
    print("economic variable: ", economic_variable)
    
    stocks_rise_fall = random.randint(0,1)
    
    print("stock rise or fall: ", stocks_rise_fall)
    
    if economic_variable == 1: 
    
        if option_4.upper() == "A" or "B":
        
            three_tbonds_rate_4 = three_tbonds_rate - 0.005
            six_tbonds_rate_4 = six_tbonds_rate - 0.005
        
            twelve_tbonds_rate_4= twelve_tbonds_rate - 0.005
        
            two_years_bonds_rate_4= two_years_bonds_rate - 0.005
        
            three_years_bonds_rate_4= three_years_bonds_rate - 0.005
        
            five_years_bonds_rate_4=  five_years_bonds_rate - 0.005
            
            investment_fund_option_4end = investment_fund_option_4
        
        if option_2.upper() == "C" or "D":
            
            if stocks_rise_fall == 1:
                
                investment_fund_option_4end = investment_fund_option_4 * 1.20
            
                print(f"""
                  Invested amount in stocks or private equity fund has increased by 20% to 
                  {investment_fund_option_4end}    
                     """)
            if stocks_rise_fall == 0:
                
                investment_fund_option_4end = investment_fund_option_4 * 0.95
            
                print(f"""
                  Invested amount in stocks or private equity fund has decreased by 5% to 
                  {investment_fund_option_4end} 
                  """)
    
    if economic_variable == 2: 
    
        if option_4.upper() == "A" or "B":
        
            three_tbonds_rate_4 = three_tbonds_rate + 0.005
        
            six_tbonds_rate_4 = six_tbonds_rate + 0.005
        
            twelve_tbonds_rate_4 = twelve_tbonds_rate + 0.005
        
            two_years_bonds_rate_4 = two_years_bonds_rate + 0.005
        
            three_years_bonds_rate_4 = three_years_bonds_rate + 0.005
        
            five_years_bonds_rate_4 = five_years_bonds_rate + 0.005
            
            investment_fund_option_4end = investment_fund_option_4
        
        if option_2.upper() == "C" or "D":
            
            if stocks_rise_fall == 1:
                
                investment_fund_option_4end = investment_fund_option_4 * 1.20
            
                print(f"""
                  Invested amount in stocks or private equity fund has increased by 20% to 
                  {investment_fund_option_4end}    
                     """)
            if stocks_rise_fall == 0:
                
                investment_fund_option_4end = investment_fund_option_4 * 0.95
            
                print(f"""
                  Invested amount in stocks or private equity fund has decreased by 5% to 
                  {investment_fund_option_4end} 
                  """)           
    
    if economic_variable == 3: 
    
        if option_2.upper() == "A" or "B":
        
            three_tbonds_rate_4 = three_tbonds_rate - 0.005
        
            six_tbonds_rate_4 = six_tbonds_rate - 0.005
        
            twelve_tbonds_rate_4 = twelve_tbonds_rate - 0.005
        
            two_years_bonds_rate_4 = two_years_bonds_rate - 0.005
        
            three_years_bonds_rate_4 = three_years_bonds_rate - 0.005
        
            five_years_bonds_rate_4 = five_years_bonds_rate - 0.005
            
            investment_fund_option_4end = investment_fund_option_4
        
        if option_2.upper() == "C" or "D":
            
            investment_fund_option_4end = investment_fund_option_4 * 0.95
            
            print(f"""
                  Invested amount in stocks or private equity fund has decreased by 5% to 
                  {investment_fund_option_4end} 
                  """)
    if economic_variable == 4: 
    
        if option_4.upper() == "A" or "B":
        
            three_tbonds_rate_4 = three_tbonds_rate - 0.005
        
            six_tbonds_rate_4= six_tbonds_rate - 0.005
        
            twelve_tbonds_rate_4 = twelve_tbonds_rate - 0.005
        
            two_years_bonds_rate_4 = two_years_bonds_rate - 0.005
        
            three_years_bonds_rate_4 = three_years_bonds_rate - 0.005
        
            five_years_bonds_rate_4 = five_years_bonds_rate - 0.005
            
            investment_fund_option_4end = investment_fund_option_4
            
        
        if option_4.upper() == "C" or "D":
            
            investment_fund_option_4end = investment_fund_option_4 * 0.95
            
            print(f"""
                  Invested amount in stocks or private equity fund has decreased by 5% to 
                  {investment_fund_option_4end}
                  """)
    
    if economic_variable == 5: 
    
        if option_4.upper() == "A" or "B":
        
            three_tbonds_rate_4 = three_tbonds_rate + 0.005
        
            six_tbonds_rate_4 = six_tbonds_rate + 0.005
        
            twelve_tbonds_rate_4 = twelve_tbonds_rate + 0.005
        
            two_years_bonds_rate_4 = two_years_bonds_rate+ 0.005
        
            three_years_bonds_rate_4 = three_years_bonds_rate + 0.005
        
            five_years_bonds_rate_4 = five_years_bonds_rate + 0.005
            
            investment_fund_option_4end = investment_fund_option_4
        
        if option_4.upper() == "C" or "D":
                
                investment_fund_option_4end = investment_fund_option_4 * 1.20
            
                print(f"""
                  Invested amount in stocks or private equity fund has increased by 20% to 
                  {investment_fund_option_4end}    
                     """)
                     
                
    if economic_variable == 6: 
    
        if option_4.upper() == "A" or "B":
        
            three_tbonds_rate_4 = three_tbonds_rate + 0.005
        
            six_tbonds_rate_4= six_tbonds_rate + 0.005
        
            twelve_tbonds_rate_4 = twelve_tbonds_rate + 0.005
        
            two_years_bonds_rate_4 = two_years_bonds_rate + 0.005
        
            three_years_bonds_rate_4 = three_years_bonds_rate + 0.005
        
            five_years_bonds_rate_4 = five_years_bonds_rate+ 0.005
            
            investment_fund_option_4end = investment_fund_option_3
        
        if option_3.upper() == "C" or "D":
            
            investment_fund_option_4end = investment_fund_option_4 * 0.95
            
            print(f"""
                  Invested amount in stocks or private equity fund has decreased by 5% to 
                  {investment_fund_option_4end}
                  """)
    
    if economic_variable == 7: 
    
        if option_4.upper() == "A" or "B":
        
            three_tbonds_rate_4 = three_tbonds_rate - 0.005
        
            six_tbonds_rate_4 = six_tbonds_rate - 0.005
        
            twelve_tbonds_rate_4 = twelve_tbonds_rate - 0.005
        
            two_years_bonds_rate_4 = two_years_bonds_rate - 0.005
        
            three_years_bonds_rate_4 = three_years_bonds_rate - 0.005
        
            five_years_bonds_rate_4 = five_years_bonds_rate - 0.005
            
            investment_fund_option_4end = investment_fund_option_4
        
        if option_4.upper() == "C" or "D":
             
            investment_fund_option_4end = investment_fund_option_4 * 1.20
            
            print(f"""
                  Invested amount in stocks or private equity fund has increased by 20% to 
                  {investment_fund_option_4end}    
                  """)
    
    
    if economic_variable == 8: 
    
        if option_4.upper() == "A" or "B":
        
            three_tbonds_rate_4 = three_tbonds_rate + 0.005
        
            six_tbonds_rate_4 = six_tbonds_rate + 0.005
        
            twelve_tbonds_rate_4 = twelve_tbonds_rate + 0.005
        
            two_years_bonds_rate_4 = two_years_bonds_rate + 0.005
        
            three_years_bonds_rate_4 = three_years_bonds_rate + 0.005
        
            five_years_bonds_rate_4 = five_years_bonds_rate + 0.005
            
            investment_fund_option_4end = investment_fund_option_4
        
        if option_4.upper() == "C" or "D":
            
            if stocks_rise_fall == 1:
                
                investment_fund_option_4end = investment_fund_option_4 * 1.20
            
                print(f"""
                  Invested amount in stocks or private equity fund has increased by 20% to 
                  {investment_fund_option_4end}    
                     """)
            if stocks_rise_fall == 0:
                
                investment_fund_option_4end = investment_fund_option_2 * 0.95
            
                print(f"""
                  Invested amount in stocks or private equity fund has decreased by 5% to 
                  {investment_fund_option_4end}
                  """) 
    
    if economic_variable == 9: 
       
        print (f"Economy is stable for now {player_name}.")
                    
        three_tbonds_rate_4 = three_tbonds_rate
        
        six_tbonds_rate_4 = six_tbonds_rate
        
        twelve_tbonds_rate_4 = twelve_tbonds_rate
        
        two_years_bonds_rate_4 = two_years_bonds_rate 
        
        three_years_bonds_rate_4 = three_years_bonds_rate 
        
        five_years_bonds_rate_4 = five_years_bonds_rate
        
        investment_fund_option_4end = investment_fund_option_4
        
        
    input("Press enter to continue")
    
    
    investment_fund_option_5 = input(f'How much would you like to invest from ${player_investment_value},your new approved loan amount: ')
    
    while True:
        
        try:
            investment_fund_option_5 = input('How much would you like to invest? Please enter a figure: ')  
        
            ValueError
            TypeError
            break
        
        except:
        
            print(f"Awesome!!! You have decided on investing {investment_fund_option_5}")
            break
    
    
    print(f"Awesome!!! You have decided on investing {investment_fund_option_3}")
    
    
    investment_fund_option_5 = int(float(f"{investment_fund_option_5}"))
        
    if investment_fund_option_5 >= player_investment_value_2:
        
        print(f""" Error!!! Please input value less than {player_investment_value}""")
        
        investment_fund_option_5 = input('How much would you like to invest: ')
            
    else:
        print(f"Awesome!!! You have decided on investing {investment_fund_option_5}")
    
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
               A: 3 months treasury bonds @ {three_tbonds_rate_4}
               B: 6 months treasury bonds @ {six_tbonds_rate_4}
               C: 12 month treasury bonds @ {twelve_tbonds_rate_4}
               """)
                
                if t_bonds_option_5.upper()== "A":
            
                    fifth_interest = int(investment_fund_option_5) * three_tbonds_rate_4
            
                    print(f'Your expected interest is ${fifth_interest}. All things being equal. ')
                    break
                
                elif t_bonds_option_5.upper() == "B":
            
                    fifth_interest =  int(investment_fund_option_5) *six_tbonds_rate_4
            
                    print(f'Your expected interest is ${fifth_interest}. All things being equal.  ')
                    break
                
                elif t_bonds_option_5.upper() == "C":
            
                    fifth_interest = int(investment_fund_option_5) * twelve_tbonds_rate_4
            
                    print(f'Your expected interest is ${fifth_interest}.All things being equal.  ')
                    break
                
                else:
                    print("Error!! Please select option A, B or C")
                    
        
        if option_5.upper() == "B":
        
            bonds_option_5 = input (f"""
                                
               Would you like to invest in 
               A: 2 years bonds @ {two_years_bonds_rate_4}
               B: 3 years bonds @ {three_years_bonds_rate_4}
               C: 5 years bonds @ {five_years_bonds_rate_4}
               """)
        
            if bonds_option_5.upper()== "A":
            
                fifth_interest = int(investment_fund_option_5) * two_years_bonds_rate_4
            
                print(f'Your expected interest per annum is ${fifth_interest} . All things being equal. ')
                break
            
            elif bonds_option_5.upper() == "B":
            
                fifth_interest = int(investment_fund_option_5) * three_years_bonds_rate_4
            
                print(f'Your expected interest per annum is ${fifth_interest} . All things being equal. ')   
                break
            
            elif bonds_option_5.upper() == "C":
            
                fifth_interest = int(investment_fund_option_5) * five_years_bonds_rate_4
            
                print(f'Your expected interest per annum is ${fifth_interest} . All things being equal. ')
                break
                
            else:
                print("Error!! Please select option A, B or C")
            
                bonds_option_5 = input (f"""
                                
                Would you like to invest in 
               A: 2 years bonds @ {two_years_bonds_rate_4}
               B: 3 years bonds @ {three_years_bonds_rate_4}
               C: 5 years bonds @ {five_years_bonds_rate_4}
               """)
        elif option_5.upper() == "C":
    
            print(f"""
                  You have invested ${investment_fund_option_5} in the S&P index stock fund.
                  """)
            SP_guess = random.randint(1,3)
            if SP_guess == 1:
                third_interest = three_tbonds_rate_4 * investment_fund_option_5
            elif SP_guess == 2:
                third_interest = three_tbonds_rate_4 * investment_fund_option_5
                
            elif SP_guess == 3:
                third_interest = six_tbonds_rate_4 * investment_fund_option_5
            break
    
        elif option_5.upper() == "D":
            third_interest = three_tbonds_rate_4 * investment_fund_option_5
            
            print(f" You have invested ${investment_fund_option_5} in the Private equity fund.")
            break
    
        else:     
            print("\n Error!! Please select option A, B, C or D. ")
            continue
    
        
    input( '< Press enter to proceed > \n')
    
    balance_after_option_5 = player_investment_value_2 - int(float(investment_fund_option_5))
    
    total_value_round_1 = investment_fund_option_1 + first_interest
    total_value_round_2 = investment_fund_option_2end + second_interest
    total_value_round_3 = investment_fund_option_3end + third_interest
    total_value_round_4 = investment_fund_option_4end + fourth_interest
    total_value_round_5a = investment_fund_option_5 + fifth_interest
    
    print(f"""
          Your current invested amount is you have ${balance_after_option_5} to invest in the next round.
          
          Good Job {player_name}. Happy investing and always remember when life throws you lemon, you do what?
          
          That's right, you make lemonades.
          
          Good luck on your next round of investments!!!
          
          """)
    
    input( '< Press enter to proceed > \n')
    
    print(f"""
          Dear {player_name},
          
          This the end of the round 5.
          
          I hope the news flash hasn't bogged you down one bit.
          
          I just want to give you an update on how you have done so far.
         
          
{'-'* 80} 
         
Stage   |       Investment value	                 Interest earned           Total value 

ROUND1  |       ${investment_fund_option_1}         {first_interest}        {total_value_round_1}
	
ROUND2  |       ${investment_fund_option_2end}      {second_interest}       {total_value_round_2}

ROUND3  |       ${investment_fund_option_3end}      {third_interest}        {total_value_round_3}

ROUND4  |       ${investment_fund_option_4end}      {fourth_interest}       {total_value_round_4}

ROUND5  |       ${investment_fund_option_5}         {fifth_interest}        {total_value_round_5a}

{'-'* 80}     
          Sincerely,
          
          Jane
	
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
    if economic_variable == 2 :
        
        print("""
              News Flash: Deflation!!!
              
              The Federal Bureau of Statistics reports a general decrease in prices of goods and services.
              Typically this leads to decrease in rates and stock prices might decrease or increase
              """)
    if economic_variable == 3 :
        
        print("""
               News Flash: Economic Meltdown !!!
              
              The Federal Bureau of Statistics reports an Economic Meltdown!!!.
              temporary disruption in economic activities which leads to rates decrease and fall in stock prices.
              """)
    if economic_variable == 4 :
        
        print("""
               News Flash: Unemployment rate: high!!!
              
              The Federal Bureau of Statistics reports an increase the Unemployment rate.
                A rise in unemployment rate leads to decrease in rate and a fall in stock prices.
              """)
        
    if economic_variable == 5 :
        
        print("""
               News Flash: Unemployment rate: low!!!
              
               The Federal Bureau of Statistics reports an decrease the Unemployment rate.
              A fall in unemployment rate leads to an increase in rate and an increase in stock prices.
              """)
        
    if economic_variable == 6 :
        
        print("""
               News Flash: GDP: lower!!!
        
              The Federal Bureau of Statistics reports a decrease in GDP.
              Gross Domestic product is the summation of all economic goods and services produced by nationals of a country. 
              A rise in GDP leads to rise in stocks and fall in rates. 
              A fall in GDP leads more likely to a fall in stock prices and a rise in rates
              """)    
    
    if economic_variable == 7 :
        
        print("""
               News Flash: GDP: higher!!!
              
              The Federal Bureau of Statistics reports an increase in GDP.
              Gross Domestic product is the summation of all economic goods and services produced by nationals of a country. 
              A rise in GDP leads to more likely to rise in stocks and fall in rates. 
              
              """)   
    if economic_variable == 8 :
        
        print("""
               News Flash: Fire harzard dirupts economic activities !!!
              
              The Federal Bureau of Statistics reports an environmental disruption in the economy.
              Typically this leads likely to increase in rates and stock prices might decrease or increase
              """)       
        
    if economic_variable == 9 :
        
        print("""
               News Flash: Economy: Stable!!!
              
              The Federal Bureau of Statistics reports stabiliy and no threat to current status quo
              """)   
    
    print("economic variable: ", economic_variable)
    
    stocks_rise_fall = random.randint(0,1)
    
    print("stock rise or fall: ", stocks_rise_fall)
    
    if economic_variable == 1: 
    
        if option_5.upper() == "A" or "B":
        
            three_tbonds_rate_5 = three_tbonds_rate - 0.005
            six_tbonds_rate_5 = six_tbonds_rate - 0.005
        
            twelve_tbonds_rate_5= twelve_tbonds_rate - 0.005
        
            two_years_bonds_rate_5= two_years_bonds_rate - 0.005
        
            three_years_bonds_rate_5= three_years_bonds_rate - 0.005
        
            five_years_bonds_rate_5=  five_years_bonds_rate - 0.005
            
            investment_fund_option_5end = investment_fund_option_5 
        
        if option_5.upper() == "C" or "D":
            
            if stocks_rise_fall == 1:
                
                investment_fund_option_5end = investment_fund_option_5 * 1.20
            
                print(f"""
                  Invested amount in stocks or private equity fund has increased by 20% to 
                  {investment_fund_option_5end}    
                     """)
            if stocks_rise_fall == 0:
                
                investment_fund_option_5end = investment_fund_option_5 * 0.95
            
                print(f"""
                  Invested amount in stocks or private equity fund has decreased by 5% to 
                  {investment_fund_option_5end} 
                  """)
    
    if economic_variable == 2: 
    
        if option_5.upper() == "A" or "B":
        
            three_tbonds_rate_5 = three_tbonds_rate + 0.005
        
            six_tbonds_rate_5 = six_tbonds_rate + 0.005
        
            twelve_tbonds_rate_5 = twelve_tbonds_rate + 0.005
        
            two_years_bonds_rate_5 = two_years_bonds_rate + 0.005
        
            three_years_bonds_rate_5 = three_years_bonds_rate + 0.005
        
            five_years_bonds_rate_5 = five_years_bonds_rate + 0.005
            
            investment_fund_option_5end = investment_fund_option_5 
        
        if option_5.upper() == "C" or "D":
            
            if stocks_rise_fall == 1:
                
                investment_fund_option_5end = investment_fund_option_5 * 1.20
            
                print(f"""
                  Invested amount in stocks or private equity fund has increased by 20% to 
                  {investment_fund_option_5end}    
                     """)
            elif stocks_rise_fall == 0:
                
                investment_fund_option_5end = investment_fund_option_5 * 0.95
            
                print(f"""
                  Invested amount in stocks or private equity fund has decreased by 5% to 
                  {investment_fund_option_5end} 
                  """)           
    
    if economic_variable == 3: 
    
        if option_5.upper() == "A" or "B":
        
            three_tbonds_rate_5 = three_tbonds_rate - 0.005
        
            six_tbonds_rate_5 = six_tbonds_rate - 0.005
        
            twelve_tbonds_rate_5 = twelve_tbonds_rate - 0.005
        
            two_years_bonds_rate_5= two_years_bonds_rate - 0.005
        
            three_years_bonds_rate_5 = three_years_bonds_rate - 0.005
        
            five_years_bonds_rate_5 = five_years_bonds_rate - 0.005
            
            investment_fund_option_5end = investment_fund_option_5 
        
        if option_5.upper() == "C" or "D":
            
            investment_fund_option_5end = investment_fund_option_5 * 0.95
            
            print(f"""
                  Invested amount in stocks or private equity fund has decreased by 5% to 
                  {investment_fund_option_5end} 
                  """)
    if economic_variable == 4: 
    
        if option_5.upper() == "A" or "B":
        
            three_tbonds_rate_5 = three_tbonds_rate - 0.005
        
            six_tbonds_rate_5= six_tbonds_rate - 0.005
        
            twelve_tbonds_rate_5 = twelve_tbonds_rate - 0.005
        
            two_years_bonds_rate_5 = two_years_bonds_rate - 0.005
        
            three_years_bonds_rate_5 = three_years_bonds_rate - 0.005
        
            five_years_bonds_rate_5 = five_years_bonds_rate - 0.005
            
            investment_fund_option_5end = investment_fund_option_5 
            
        
        if option_5.upper() == "C" or "D":
            
            investment_fund_option_5end = investment_fund_option_5 * 0.95
            
            print(f"""
                  Invested amount in stocks or private equity fund has decreased by 5% to 
                  {investment_fund_option_5end}
                  """)
    
    if economic_variable == 5: 
    
        if option_5.upper() == "A" or "B":
        
            three_tbonds_rate_5= three_tbonds_rate + 0.005
        
            six_tbonds_rate_5 = six_tbonds_rate + 0.005
        
            twelve_tbonds_rate_5 = twelve_tbonds_rate + 0.005
        
            two_years_bonds_rate_5 = two_years_bonds_rate+ 0.005
        
            three_years_bonds_rate_5 = three_years_bonds_rate + 0.005
        
            five_years_bonds_rate_5 = five_years_bonds_rate + 0.005
            
            investment_fund_option_5end = investment_fund_option_5
        
        if option_5.upper() == "C" or "D":
                
                investment_fund_option_5end = investment_fund_option_5 * 1.20
            
                print(f"""
                  Invested amount in stocks or private equity fund has increased by 20% to 
                  {investment_fund_option_5end}    
                     """)
                     
                
    if economic_variable == 6: 
    
        if option_5.upper() == "A" or "B":
        
            three_tbonds_rate_5 = three_tbonds_rate + 0.005
        
            six_tbonds_rate_5 = six_tbonds_rate + 0.005
        
            twelve_tbonds_rate_5 = twelve_tbonds_rate + 0.005
        
            two_years_bonds_rate_5 = two_years_bonds_rate + 0.005
        
            three_years_bonds_rate_5 = three_years_bonds_rate + 0.005
        
            five_years_bonds_rate_5 = five_years_bonds_rate+ 0.005
            
            investment_fund_option_5end = investment_fund_option_5 
        
        if option_5.upper() == "C" or "D":
            
            investment_fund_option_5end = investment_fund_option_5 * 0.95
            
            print(f"""
                  Invested amount in stocks or private equity fund has decreased by 5% to 
                  {investment_fund_option_5end}
                  """)
    
    if economic_variable == 7: 
    
        if option_5.upper() == "A" or "B":
        
            three_tbonds_rate_5 = three_tbonds_rate - 0.005
        
            six_tbonds_rate_5 = six_tbonds_rate - 0.005
        
            twelve_tbonds_rate_5 = twelve_tbonds_rate - 0.005
        
            two_years_bonds_rate_5 = two_years_bonds_rate - 0.005
        
            three_years_bonds_rate_5 = three_years_bonds_rate - 0.005
        
            five_years_bonds_rate_5 = five_years_bonds_rate - 0.005
            
            investment_fund_option_5end = investment_fund_option_5 
        
        if option_5.upper() == "C" or "D":
             
            investment_fund_option_5end = investment_fund_option_5 * 1.20
            
            print(f"""
                  Invested amount in stocks or private equity fund has increased by 20% to 
                  {investment_fund_option_5end}    
                  """)
    
    
    if economic_variable == 8: 
    
        if option_5.upper() == "A" or "B":
        
            three_tbonds_rate_5 = three_tbonds_rate + 0.005
        
            six_tbonds_rate_5 = six_tbonds_rate + 0.005
        
            twelve_tbonds_rate_5 = twelve_tbonds_rate + 0.005
        
            two_years_bonds_rate_5 = two_years_bonds_rate + 0.005
        
            three_years_bonds_rate_5 = three_years_bonds_rate + 0.005
        
            five_years_bonds_rate_5 = five_years_bonds_rate + 0.005
            
            investment_fund_option_5end = investment_fund_option_5 
        
        if option_5.upper() == "C" or "D":
            
            if stocks_rise_fall == 1:
                
                investment_fund_option_5end = investment_fund_option_5 * 1.15
            
                print(f"""
                  Invested amount in stocks or private equity fund has increased by 15% to 
                  {investment_fund_option_5end}    
                     """)
            if stocks_rise_fall == 0:
                
                investment_fund_option_5end = investment_fund_option_5 * 0.95
            
                print(f"""
                  Invested amount in stocks or private equity fund has decreased by 5% to 
                  {investment_fund_option_5end}
                  """) 
    
    if economic_variable == 9: 
        
        investment_fund_option_5end = investment_fund_option_5
       
        print (f"Economy is stable for now {player_name}.")
        
        
    input("Press enter to continue")
    
    total_value_round_5 = investment_fund_option_5end + fifth_interest
    
    print(f"""
          Dear {player_name},
          
          This the end of the first stage.
          
          I hope the news flash hasn't bogged you down one bit.
          
          I just want to give you an update on how you have done so far.
         
          
{'-'* 80} 
         
Stage   |       Investment value	                 Interest earned           Total value 

ROUND1  |       ${investment_fund_option_1end}     {first_interest}        {total_value_round_1}
	
ROUND2  |       ${investment_fund_option_2end}     {second_interest}       {total_value_round_2}

ROUND3  |       ${investment_fund_option_3end}     {third_interest}        {total_value_round_3}
	
ROUND4  |       ${investment_fund_option_4end}      {fourth_interest}       {total_value_round_4}

ROUND5  |       ${investment_fund_option_5end}     {fifth_interest}        {total_value_round_5}
	
{'-'* 80}     
          Sincerely,
          
          Jane
	
        """)
    

    investment_fund_option_6 = balance_after_option_5
    
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
               A: 3 months treasury bonds @ {three_tbonds_rate_5}
               B: 6 months treasury bonds @ {six_tbonds_rate_5}
               C: 12 month treasury bonds @ {twelve_tbonds_rate_5}
               """)
                
                if t_bonds_option_6.upper()== "A":
            
                    final_interest = int(investment_fund_option_6) * three_tbonds_rate_5
            
                    print(f'Your expected interest is ${final_interest}. All things being equal. ')
                    break
                
                elif t_bonds_option_6.upper() == "B":
            
                    final_interest =  int(investment_fund_option_6) *six_tbonds_rate_5
            
                    print(f'Your expected interest is ${final_interest}. All things being equal. ')
                    break
                
                elif t_bonds_option_6.upper() == "C":
            
                    final_interest = int(investment_fund_option_6) * twelve_tbonds_rate_5
            
                    print(f'Your expected interest is ${final_interest}. All things being equal. ')
                    break
                
                else:
                    print("Error!! Please select option A, B or C")
                    
        
        if option_6.upper() == "B":
        
            bonds_option_6 = input (f"""
                                
               Would you like to invest in 
               A: 2 years bonds @ {two_years_bonds_rate_5}
               B: 3 years bonds @ {three_years_bonds_rate_5}
               C: 5 years bonds @ {five_years_bonds_rate_5}
               """)
        
            if bonds_option_6.upper()== "A":
            
                final_interest = int(investment_fund_option_6) * two_years_bonds_rate_5
            
                print(f'Your expected interest is ${final_interest}. All things being equal. ')
                break
            
            elif bonds_option_6.upper() == "B":
            
                final_interest = int(investment_fund_option_6) * three_years_bonds_rate_5
            
                print(f'Your expected interest is ${final_interest}. All things being equal. ')
                break
            
            elif bonds_option_6.upper() == "C":
            
                final_interest = int(investment_fund_option_6) * five_years_bonds_rate_5
            
                print(f'Your expected interest is ${final_interest}. All things being equal. ')
                break
                
            else:
                print("Error!! Please select option A, B or C")
            
                bonds_option_6 = input (f"""
                                
                Would you like to invest in 
               A: 2 years bonds @ {two_years_bonds_rate_5}
               B: 3 years bonds @ {three_years_bonds_rate_5}
               C: 5 years bonds @ {five_years_bonds_rate_5}
               """)
                
        elif option_6.upper() == "C":
    
            print(f"""
                  You have invested ${investment_fund_option_6} in the S&P index stock fund.
                  """)
            SP_guess = random.randint(1,3)
            
            if SP_guess == 1:
                fourth_interest= -three_tbonds_rate_5 * investment_fund_option_6
                
            if SP_guess == 2:
                fourth_interest = three_tbonds_rate_5 * investment_fund_option_6
                
            if SP_guess == 3:
                fourth_interest = three_tbonds_rate_5 * investment_fund_option_6
            break
    
        elif option_6.upper() == "D":
            fourth_interest = six_tbonds_rate_5 * investment_fund_option_6
            print(f" You have invested ${investment_fund_option_6} in the Private equity fund.")
            break
    
        else:     
            print("\n Error!! Please select option A, B, C or D. ")
            continue
    
        
    input( '< Press enter to proceed > \n')
    
    balance_after_option_6 = player_investment_value_2 - investment_fund_option_5-investment_fund_option_6
    
    total_value_round_6 = investment_fund_option_6 + final_interest
    
    print(f"""
          Your current invested amount in round five and six is  ${investment_fund_option_5} and ${investment_fund_option_6} respectively and you have ${balance_after_option_6} unused.
          
          Good Job {player_name}. Happy investing and always remember when life throws you lemon, you do what?
          
          That's right, you make lemonades.
          
          Good luck !!!
          
          """)
    
    input("Press enter to continue")
    
    total_value_round_1 = investment_fund_option_1 + first_interest
    total_value_round_2 = investment_fund_option_2end + second_interest
    total_value_round_3 = investment_fund_option_3end + third_interest
    total_value_round_4 = investment_fund_option_4end + fourth_interest
    total_value_round_5 = investment_fund_option_5end + fifth_interest
    total_value_round_6 = investment_fund_option_6 + fifth_interest
    
    print(f"""
          Dear {player_name},
          
          This the end of the first stage.
          
          I hope the news flash hasn't bogged you down one bit.
          
          I just want to give you an update on how you have done so far.
         
          
{'-'* 80} 
         
Stage   |       Investment value	                 Interest earned           Total value 

ROUND1  |       ${investment_fund_option_1end}     {first_interest}        {total_value_round_1}
	
ROUND2  |       ${investment_fund_option_2end}     {second_interest}       {total_value_round_2}

ROUND3  |       ${investment_fund_option_3end}     {third_interest}        {total_value_round_3}
	
ROUND4  |       ${investment_fund_option_4end}      {fourth_interest}       {total_value_round_4}

ROUND5  |       ${investment_fund_option_5end}     {fifth_interest}        {total_value_round_5}
	
ROUND6  |       ${investment_fund_option_6}      {final_interest}       {total_value_round_6}

{'-'* 80}     
          Sincerely,
          
          Jane
	
        """)
    
    input("Press enter to continue")
      
    print (balance_after_option_6)
    
    total_loan_repayment = int(investment_fund) * 1.07 + (player_investment_value * 1.07) + (player_investment_value * 1.10)
    
    print( f""" 
          {'-'* 50} 
    Total loan replayment amount is ${total_loan_repayment}"
          {'-'* 50} 
          """)
    
    
    player_investment_value_3 = investment_fund_option_1end +investment_fund_option_2end + investment_fund_option_3end +investment_fund_option_4end + +investment_fund_option_5end + first_interest + second_interest +third_interest+fourth_interest
    
    
    if player_investment_value_3 < total_loan_repayment:
        
        difference = total_loan_repayment - player_investment_value
        
        print (f"Game Over!!! You are ${difference} short.")
        
        fail()
        exit

    print (""""
           __   __        __   __       ___  __    /
/  ` /  \ |\ | / _` |__)  /\   |  /__`  / 
\__, \__/ | \| \__> |  \ /~~\  |  .__/ .  
""")

    print("""
       __   __        __   __       ___                ___    __        __    /
/  ` /  \ |\ | / _` |__)  /\   |  |  | |     /\   |  | /  \ |\ | /__`  / 
\__, \__/ | \| \__> |  \ /~~\  |  \__/ |___ /~~\  |  | \__/ | \| .__/ .  
""")

    print("""" {player_name} \nYou made it to the end.
      
      Your resolve was tested and you stood tall.
      
      You deserve some accolades
      
      """)

    fail()



game_start()   