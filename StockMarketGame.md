## Stock Market Game Program

### Summary

In this game the user starts with $1000, then buys and sells stocks for six days. The goal is to finish with the highest cash balance

### Design Requirements

#### Basics
  There are three different stocks. They are: SouthEastern Individual (SEI), Orange (ORG), and Big Brother (BB)). The game starts with each stock's price at $50.
  The user starts with $1000 and the game runs for 6 days. 

##### Variable and Data Specifics
* acct (dictionary) holds the user's cash balance and how many shares of each stock they own
* stocks (list of dictionaries) each dictionary is one stock's information. This variable can be found in the Github repo
* maxDays = 6
* currentDay = 1

#### Gameplay loop
1. Print the daily report. Daily report must include the user's cash balance, their current holdings, and the current day's stock prices
2. Allow the user to buy and sell as much as they want until they decide to end the day
3. Finish the day by randomly changing the stock prices in some way, based off the current prices

## Functions Needed

### printDailyReport()
  prints the user's cash balance, their current holdings, and the day's prices

### userChoices()
Continually asks the user if they want to buy, sell, or end the day

Question: What should this do if the user enters something weird?

### buyStocks()
Asks the user which stock they want to buy, how many shares, then changes the user's account to reflect that

### sellStocks()
Asks the user which stock they want to sell, how many shares, then changes the user's account to reflect that

### endDay()
Tells the user the day is over, then changes the stock prices

### changePrices()
Change each stock's price by a random amount

## Backlog (In no particular order)



* Give the user an account update after they buy or sell
* Tell the user their percent of ownership in each company based off their shares
* Include a netWorth function that tells the user the current total value of their holdings
  * Use the netWorth function to end the game by telling the user their total money amount
* Include high/low risk stocks and inform the user about them
* Show the user each stock's recent history
* Add an "Easter egg" where the program collects the user's CC details
* Add a "stock market crash" ending where the last day of X % of runs end with the user losing all their non-cash holdings
* Record scores to a "Leaderboard" text file
* Make the game print in an easier-to-read way

## Finished Items
* Avoid cheating
  * User cannot sell more shares than they have
  * User cannot spend more money than they have
* When CurrentBalance is printed, round to the nearest cent
* Negative stock prices
