#The data we need to retrieve

#Add our dependencies
import csv
import os

#Assign a variable to load the file from path
file_to_load=os.path.join("Resources", "election_results.csv")
#Assign a filename variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results to read the file
with open(file_to_load) as election_data:

# Read the file object with the reader function.
    file_reader = csv.reader(election_data)


# Print the header row.
    headers = next(file_reader)
    print(headers)

 # Print each row in the CSV file.
    #for row in file_reader:
        #print(row)



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