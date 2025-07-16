## Stock Market Game Program

### Summary

In this game the user starts with $1000, then buys and sells stocks for six days. The goal is to finish with the highest cash balance

### Design Requirements

#### Basics
  There are three different stocks. They are: SouthEastern Individual (SEI), Orange (ORG), and Big Brother (BB)). The game starts with each stock's price at $50.
  The user starts with $1000 and the game runs for 6 days. 


## Backlog (In no particular order)

### Bugs and QoL That Need To Be Fixed
* Allow upper and lower case when inputting User Choices
  * allow is user choice contains "buy", "end" etc -> HB
* Give the user an account update after they buy or sell
* Instead of printing the list of syms, print how many shares of each

### New Features
* Tell the user their percent of ownership in each company based off their shares
* Show the user each stock's recent history
* Award prizes/tiers based on final networth

## "Finished" Items
* Avoid cheating
  * User cannot sell more shares than they have
  * User cannot spend more money than they have
* When CurrentBalance is printed, round to the nearest cent
* No negative stock prices
* Include a netWorth function that tells the user the current total value of their holdings
  * Use the netWorth function to end the game by telling the user their total money amount
* Include high/low risk stocks and inform the user about them
* Add an "Easter egg" where the program collects the user's CC details
* Add a "stock market crash" ending where the last day of X % of runs end with the user losing all their non-cash holdings
* Include ads


