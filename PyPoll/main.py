# Print the title
print("Election Results")
print("------------------------")

# Path to the CSV data
import os
import csv

pypoll_data = os.path.join("Resources/election_data.csv")

# Read the CSV data without the header
with open(pypoll_data, encoding='UTF-8') as csvfile:
    pypoll_data_csv = csv.reader(csvfile, delimiter=",")
    next(pypoll_data_csv)

    # The total number of votes cast
    voters = list(pypoll_data_csv)
    cast_voters = len(voters)
    print("Total Votes: ", cast_voters)
    print("------------------------")

    # A complete list of candidates who received votes
    candi_w_vote = list()
    count_candi = list()
    for x in range (0,cast_voters):
        candidate = voters[x][2]
        count_candi.append(candidate)
        if candidate not in candi_w_vote:
            candi_w_vote.append(candidate)
    complete_candi = len(candi_w_vote)
    
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    votes = list()
    percentage = list()
    for y in range (0,complete_candi):
        name = candi_w_vote[y]
        votes.append(count_candi.count(name))
        v_prct = votes[y]/cast_voters
        percentage.append(v_prct)
    
    for z in range (0,complete_candi): 
        print(f"{candi_w_vote[z]}: {percentage[z]:.3%} ({votes[z]:})")
    print("------------------------")
  
    # The winner of the election based on popular vote
    winner = votes.index(max(votes))
    print("Winner: ", candi_w_vote[winner])
    print("------------------------")

    # Print the results to txt file
    print("Election Results", file=open("analysis/Pypoll.txt", "a"))
    print("-------------------------", file=open("analysis/Pypoll.txt", "a"))
    print(f"Total Votes: {cast_voters:}", file=open("analysis/Pypoll.txt", "a"))
    print("-------------------------", file=open("analysis/Pypoll.txt", "a"))
    for z in range (0,complete_candi): 
        print(f"{candi_w_vote[z]}: {percentage[z]:.3%} ({votes[z]:})", file=open("analysis/Pypoll.txt", "a"))
    print("-------------------------", file=open("analysis/Pypoll.txt", "a"))
    print(f"Winner: {candi_w_vote[winner]}", file=open("analysis/Pypoll.txt", "a"))
    print("-------------------------", file=open("analysis/Pypoll.txt", "a"))
    