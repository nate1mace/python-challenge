import os
import csv
from collections import Counter

csvpath = os.path.join('Instructions','PyPoll','Resources','election_data.csv')
with open(csvpath, newline='') as csvfile:

    elec_data = csv.reader(csvfile)
    csv_header = next(elec_data)

    def votesummary(tot_votes,vote0,vote0perc,vote1,vote1perc,vote2,vote2perc,vote3,vote3perc):
        print("Election Results")
        print("-----------------------")
        print("Total Votes: " + str(tot_votes))
        print("-----------------------")
        print( candidate[0] + ": " + str("{0:.0%}".format(vote0perc)) + " (" + str(vote0) + ")")
        print( candidate[1] + ": " + str("{0:.0%}".format(vote1perc)) + " (" + str(vote1) + ")")
        print( candidate[2] + ": " + str("{0:.0%}".format(vote2perc)) + " (" + str(vote2) + ")")
        print( candidate[3] + ": " + str("{0:.0%}".format(vote3perc)) + " (" + str(vote3) + ")")
        print("-----------------------")
        print("Winner: " + winner )
        print("-----------------------")

    #set all variables to zero, create arrays
    tot_votes = 0
    vote0 = 0
    vote1 = 0
    vote2 = 0
    vote3 = 0
    candidate = []

    for i in elec_data:
        #create list of candidates
        if i[2] not in candidate:
            candidate.append(i[2])
        #if voter ID is over x tally votes
        if int(i[0]) > 10000000:
            tot_votes = tot_votes + 1
        #for loop to cycle thru candidates
        for x in range(0,len(candidate)):
            #match candidate from csv to candidate array, if candidate == string x in array, tally votes
            if i[2] == candidate[x] and x == 0:
                vote0 = vote0 + 1
                #calculate winner
                if vote0 > vote1 + vote2 + vote3:
                    winner = candidate[x]
            if i[2] == candidate[x] and x == 1:
                vote1 = vote1 + 1
                if vote1 > vote0 + vote2 + vote3:
                    winner = candidate[x]
            if i[2] == candidate[x] and x == 2:
                vote2 = vote2 + 1
                if vote2 > vote1 + vote0 + vote3:
                    winner = candidate[x]
            if i[2] == candidate[x] and x == 3:
                vote3 = vote3 + 1
                if vote3 > vote1 + vote2 + vote0:
                    winner = candidate[x]
    #calculate vote percentages
    vote0perc = vote0/tot_votes
    vote1perc = vote1/tot_votes
    vote2perc = vote2/tot_votes
    vote3perc = vote3/tot_votes

print(votesummary(tot_votes,vote0,vote0perc,vote1,vote1perc,vote2,vote2perc,vote3,vote3perc))

#output text file
with open("elec_results.txt","w") as txt_file:
    txt_file.write("Election Results" + '\n' +
        "-----------------------" + '\n' +
        "Total Votes: " + str(tot_votes) + '\n' +
        "-----------------------" + '\n' +
        candidate[0] + ": " + str("{0:.0%}".format(vote0perc)) + " (" + str(vote0) + ")" + '\n' +
        candidate[1] + ": " + str("{0:.0%}".format(vote1perc)) + " (" + str(vote1) + ")" + '\n' +
        candidate[2] + ": " + str("{0:.0%}".format(vote2perc)) + " (" + str(vote2) + ")" + '\n' +
        candidate[3] + ": " + str("{0:.0%}".format(vote3perc)) + " (" + str(vote3) + ")" + '\n' +
        "-----------------------" + '\n' +
        "Winner: " + winner  + '\n' +
        "-----------------------")