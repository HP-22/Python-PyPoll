import os
import csv

Electiondata = os.path.join('election_data.csv')

with open(Electiondata, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader)
   
    votetotal = 0
    candidate = {}
    votepercent = 0
    candtotal = 0
    Winner = ""
    votes = 0
    candvotes = 0
    voteridcol = []
    countycol = []
     
    for row in csvreader:
        
        candcol = row[2]
        candtotal = candtotal + 1

        if candcol in candidate.keys():
            candidate[candcol] = candidate[candcol] + 1
        else:
            candidate[candcol] = 1


    for candcol in candidate:
        candvotes = candtotal + candidate[candcol]
        votepercent = (candidate[candcol]) / (candtotal) * 100

        if candidate[candcol] > votes:
            Winner = candcol
            votes = candidate[candcol]

       

    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {candtotal}")
    print("--------------------------")
    print(f"{candidate}: {int(votepercent)}% {candvotes}")
    print("--------------------------")
    print(f"Winner: {Winner}")

file = open("Election_Results.txt", "w") 
file.write("Election Results\n")
file.write("--------------------------\n")
file.write(f"Total Votes: {candtotal}\n")
file.write("--------------------------\n")
file.write(f"{candidate}: {int(votepercent)}% {candvotes}\n")
file.write("--------------------------\n")
file.write(f"Winner: {Winner}")
file.close()



   