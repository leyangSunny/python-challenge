# Dependencies
import os
import csv

# path
election_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'election_data.csv')

#set variables

total_count = 0
candidate_list = []
name = []
candidate_name =[]
vote = []
percentage_total = []
winning_vote = 0


# Open the file 
with open(election_data, newline="") as csvfile:
     # Initialize csv.writer
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    # loop
    for row in csvreader:
        # The total number of votes cast
        total_count += 1
        candidate_list.append(row[2])
        # A complete list of candidates who received votes
    for name in set(candidate_list):
        # The total number of votes each candidate won
        Each_Total = candidate_list.count(name)
        vote.append(Each_Total)
        # The percentage of votes each candidate won
        percentage = (Each_Total/total_count)*100
        percentage_total.append(percentage)
        # The winner of the election based on popular vote.
        candidate_name.append(name)
        winning_vote = max(vote)
        winner = candidate_name[vote.index(winning_vote)]
    
 
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(total_count))    
print("-------------------------")
for i in range(len(candidate_name)):
    print( str(candidate_name[i]) + ": " + format((percentage_total[i]),'.3f') + "%" + "  (" + str(vote[i]) + ")") 
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(total_count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(candidate_name)):
        text.write( str(candidate_name[i]) + ": " + format((percentage_total[i]),'.3f') + "%" + "  (" + str(vote[i]) + ")" + "\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")
