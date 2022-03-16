# Election-Analysis

## Overview

The purpose of this election audit analysis was to create a program that would review a spreadsheet listing individual votes, the county in which the vote was made, and the person for whom the vote was cast. The goal of the program is to iterate through each line in the spreadsheet and identify: 1) vote totals by candidate, 2) vote percentages by candidate, 3) vote totals by county, and 4) vote percentages by county. The program can be run in Terminal/GitBash to find these figures, but it will also print the results to a .txt file. 


## Election Audit Results
Election-Audit Results: Using a bulleted list, address the following election outcomes. Use images or examples of your code as support where necessary.

- How many votes were cast in this congressional election?
  - There were 369,711 votes cast in this congressional election.

- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
  - County Votes:
    - Jefferson: 10.5% (38,855)
    - Denver: 82.8% (306,055)
    - Arapahoe: 6.7% (24,801)

- Which county had the largest number of votes?
  - Denver County, with 306,055 votes, had the largest number of votes.

- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
  - Charles Casper Stockham: 23.0% (85,213 votes)
  - Diana DeGette: 73.8% (272,892 votes)
  - Raymon Anthony Doane: 3.1% (11,606 votes)

- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
  - Diana DeGette won the election, with 272,892 votes (73.8% of the total votes).


##Election Audit Summary:

This script was successful in evaluating the election results to identify the number and percentage of votes relative to the candidate and the county. It could be easily adapted for use in other elections. None of the candidate or county names are hard-coded into the script; the program derives the names of both the candidates and counties using an index. That is to say, the candidates are specified as being the third item in each list, while the counties are specified as being the second item in the list, and this program could be used as-is for any data input where the candidate's name is already included third (and the county second) in the "list" of information associated with each vote.

If a new dataset includes the candidate and county names in different locations in the list, we would need only to update the indices for candidate and county to use the new dataset. 

If the user wanted a different geographical breakdown of votes (for example, city or state), the needed changes would be minimal. Since "county" in this program refers simply to the second item in the list, if a new dataset contained names of states as the second item, the script would automatically pull in state information there. We could change the print language to "Votes by State" and "Largest State Turnout" in lieu of "County Votes" and "Largest County Turnout" and otherwise leave the script the same to produce the same functionality, since the variable names are functional rather than prescriptive. 

In addition, if the user wanted to include other information associated with a vote (for example, the political party of the voter or the person running for office), this could be added to the script according to the existing template of creating variables and initializing them to zero, creating a new list and a new dictionary, and adjusting the if-statements and for loops.

Election-Audit Summary: In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.
