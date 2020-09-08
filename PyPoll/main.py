import os
import csv

csv_path = os.path.join("Resources","02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")

candidates = []
candidates_total =[]
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
            

print(candidates)
print(candidates_total)


        


            

total_votes = num_rows
        

