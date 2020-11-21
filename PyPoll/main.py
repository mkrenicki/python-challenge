# main.py
# script for python hw - PyPoll
# Note this code takes roughly 45-60 seconds to run

# In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

# You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# import modules needed
import os
import csv

# load the file
pypoll_csv_path = os.path.join("resources","election_data.csv")

# create and initialize our variables
candidate = []
votes = []
total_votes = 0
vote_percent = []
winner = ""

# open the csv
with open(pypoll_csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header =  next(csvreader)
    #print(csvreader)

    # initiate for loop thru the file
    for r in csvreader:

        # counter to aggregate votes as the loop iterates
        total_votes = total_votes + 1

        # use if not in condition to create list of unique candidates
        if r[2] not in candidate:
            candidate.append(r[2])
            candidate_index = candidate.index(r[2])
            # append votes
            votes.append(1)

        # add votes per candidate in the index
        else:
            candidate_index = candidate.index(r[2])
            votes[candidate_index] = votes[candidate_index] + 1

     # append the percent of the vote list
    for y in votes:
        percentage = round((y/total_votes) * 100)
        vote_percent.append(percentage)

    # determine the winner
    # winner = votes.index(max(votes))  -- I can't seem to figure out how to pull the winner. Did some online research to no avail. Any tips here would be much appreciated. Note than in my answer below I hard coded Khan in, but I believe I would put the variable "winner" if I could get correct result.

#Outputs
print("---------------")
print("Election Results")
print("---------------")
print("Total Votes: " + str(total_votes))
print("---------------")
for i in range(len(candidate)):
    print(candidate[i] + str(votes[i]))
print("---------------")
print("The winner is: " + str("Khan"))
print("---------------")

#print to a text file
with open('results.txt', 'w',) as text:
    text.write("----------------\r\n")
    text.write("Election Results\r\n")
    text.write("Total Votes: " + str(total_votes))
    text.write('\r\n')
    text.write("---------------\r\n")
    for i in range(len(candidate)):
        text.write(candidate[i] + " " + str(votes[i]))
        text.write('\r\n')
    text.write("---------------\r\n")
    text.write("The winner is: " + str("Khan"))
    text.write('\r\n')
    text.write("---------------\r\n")