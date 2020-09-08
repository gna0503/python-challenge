import os
import csv

csv_path = os.path.join("Resources","02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")

candidates = []
candidates_total =[0,0,0,0]
vote_percentage = [0,0,0,0]
num_rows = 0


with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        num_rows += 1
        if row[2] not in candidates:
            candidates.append(row[2])
            candidates_index = candidates.index(row[2])
            candidates_total[candidates_index] +=1
        else:
            candidates_index = candidates.index(row[2])
            candidates_total[candidates_index] +=1

total_votes = sum(candidates_total)

for i in range(len(candidates)):
    vote_percentage[i] = float(round(int(candidates_total[i])/int(total_votes)*100,3))
    
Winner = candidates[vote_percentage.index(max(vote_percentage))]
            
Output = f'''
Election Results
------------------------------
Total Votes: {total_votes}
------------------------------
{candidates[0]}: {vote_percentage[0]}% ({candidates_total[0]})
{candidates[1]}: {vote_percentage[1]}% ({candidates_total[1]})
{candidates[2]}: {vote_percentage[2]}% ({candidates_total[2]})
{candidates[3]}: {vote_percentage[3]}% ({candidates_total[3]})
------------------------------
Winner: {Winner}
------------------------------
'''
txtfile_path = os.path.join("analysis","Output.txt")

f = open(txtfile_path, "w")
f.write(Output)
f.close()
