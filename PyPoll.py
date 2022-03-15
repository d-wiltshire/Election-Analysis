#The data we need to retrieve

#Add our dependencies
import csv
import os

#Assign a variable to load the file from path
file_to_load=os.path.join("Resources", "election_results.csv")
#Assign a filename variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initializing total vote counter at 0
total_votes=0   

#Candidate options empty list
candidate_options=[]
#Candidate votes empty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results to read the file
with open(file_to_load) as election_data:

# Read the file object with the reader function.
    file_reader = csv.reader(election_data)

# Print the header row.
    headers = next(file_reader)
    #print(headers)

 # Print each row in the CSV file.
    for row in file_reader:
        total_votes=total_votes+1
    # Print the candidate name from each row
        candidate_name = row[2]
    #Add the candidate name to the candidate list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #begin tracking candidate vote count
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
    #print(f"{candidate_name}: received {votes} votes.")

    if (votes>winning_count) and (vote_percentage>winning_percentage):
        winning_count=votes
        winning_percentage=vote_percentage
        winning_candidate=candidate_name

    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
#print(f"The winning candidate is {winning_candidate}")
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)




#Print total votes
#print(total_votes)



#Perform the analysis
    #print(election_data)


# Using the open() function with the "w" mode we will write data to the file.
#with open(file_to_save, "w") as txt_file:
#write some data to it
    #txt_file.write("Counties in the Election\n---------------------------\nArapahoe\nDenver\nJefferson")

#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on the popular vote 