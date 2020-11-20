#main.py
#script for python hw - PyPoll

#import our modules needed
import os
import csv

#load the file
pypoll_csv_path = os.path.join("resources","election_data.csv")

#create lists to store file data
list_of_candidates = []
candidate_x = []
number_of_votes =[]
unique_candidate = []

#create any other non-list variables
winner = ""

#create a row counter variable to advance for loop
row_count = 0

#open the csv
with open(pypoll_csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header =  next(csvreader)
    #print(csvreader)

    #initiate for loop and counter to go through rows
    for r in csvreader:
        row_count = row_count + 1

        #Append candidate names from file to list_of_candidates
        list_of_candidates.append(r[2])

    #define a function to get unique values
    def unique(list_of_candidates):

        #use the unique
        for x in list_of_candidates:
            if x not in unique_candidate:
                unique_candidate.append(x)
                votes_per_candidate = list_of_candidates.count(x)
                number_of_votes.append(votes_per_candidate)

#Outputs
print("---------------")
print("Election Results")
print("---------------")
print("Total Votes: " + str(row_count))
print("---------------")
for i in range(len(unique_candidate)):
    print(unique_candidate[i] + str(number_of_votes[i]))
print("---------------")
print("The winner is: " + str(winner))
print("---------------")
