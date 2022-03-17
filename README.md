# Election-Analysis

## Overview

The purpose of this election audit analysis was to create a program that would review a spreadsheet listing individual votes, the county in which the vote was made, and the person for whom the vote was cast. The goal of the program is to iterate through each line in the spreadsheet and identify: 1) vote totals by candidate, 2) vote percentages by candidate, 3) vote totals by county, and 4) vote percentages by county. The program can be run on the command line to find these figures, but it will also print the results to a .txt file. 

The following is a screenshot of the program run on the command line: 

![Module 3 print to command line](https://user-images.githubusercontent.com/100863488/158888331-66dad3fc-5c84-432d-ad0b-fe6f84098ca8.png)


## Election Audit Results


- How many votes were cast in this congressional election?
  - There were 369,711 votes cast in this congressional election.
  - This was determined by initializing a `total_votes` variable at zero and increasing it by 1 for every row iterated in a for loop.

- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
  - County Votes:
    - Jefferson: 10.5% (38,855)
    - Denver: 82.8% (306,055)
    - Arapahoe: 6.7% (24,801)
  - The county and candidate votes were tallied using a for loop, extracting the candidate and county names by their positions in each .csv row, and increasing the count for each candidate/county for each iteration where their name appeared. Relevant code for printing the results by county also appears in the next bullet.


- Which county had the largest number of votes?
  - Denver County, with 306,055 votes, had the largest number of votes.
  - The county with the largest number of votes was also determined with a for loop. I initialized two sets of variables to count candidate and county votes. The variables without the "1" (like `votes`) refer to counting candidate votes, and the variables with "1" (as in `votes1`) were used for tracking county votes.
  ```
  for county_name in county_votes:

        # 6b: Retrieve the county vote count.
        votes1=county_votes.get(county_name)

        # 6c: Calculate the percentage of votes for the county.
        vote1_percentage = float(votes1) / float(total_votes) * 100

         # 6d: Print the county results to the terminal.
        county_results = (f"{county_name}: {vote1_percentage:.1f}% ({votes1:,})")
        print(county_results)

         # 6e: Save the county votes to a text file.
        txt_file.write(f"{county_results}\n")

         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (votes1 > votes_in_largest_county_turnout) and (vote1_percentage > winning1_percentage):
            votes_in_largest_county_turnout = votes1
            county_with_largest_turnout = county_name
            winning1_percentage = vote1_percentage
```

- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
  - Charles Casper Stockham: 23.0% (85,213 votes)
  - Diana DeGette: 73.8% (272,892 votes)
  - Raymon Anthony Doane: 3.1% (11,606 votes)
  - This information was gathered with a similar for loop:
  
```
 for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
```

- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
  - Diana DeGette won the election, with 272,892 votes (73.8% of the total votes).


## Election Audit Summary

This script was successful in evaluating the election results to identify the number and percentage of votes relative to the candidate and the county. It could be easily adapted for use in other elections. None of the candidate or county names are hard-coded into the script; the program derives the names of both the candidates and counties using an index. That is to say, the candidates are specified as being the third item in each list, while the counties are specified as being the second item in the list, and this program could be used as-is for any data input where the candidate's name is already included third (and the county second) in the "list" of information associated with each vote.

If a new dataset includes the candidate and county names in different locations in the list, we would need only to update the indices for candidate and county to use the new dataset. 

If the user wanted a different geographical breakdown of votes (for example, city or state), the needed changes would be minimal. Since "county" in this program refers simply to the second item in the list, if a new dataset contained names of states as the second item, the script would automatically pull in state information there. We could change the printed language to "Votes by State" and "Largest State Turnout" in lieu of "County Votes" and "Largest County Turnout" and otherwise leave the script the same to produce the same functionality, since the variable names are functional rather than prescriptive. 

In addition, if the user wanted to include other information associated with a vote (for example, the political party of the voter or the person running for office), this could be added to the script according to the existing template of creating variables and initializing them to zero, creating a new list and a new dictionary, and adjusting the if-statements and for loops.


