import os
import csv

#Set filepath and import csv file
csvpath = os.path.join('..',"Homework","03-python","instruction","pypoll","raw_data")
with open(csvpath, newline = '') as csvfile:
    csvdata = csv.reader(csvfile, delimiter = ',')
    next(csvdata, none)
    
    #Create lists
    voterid = []
    county = []
    candidates = []
    names_of_candidates = []


    #Run a for loop for every row of data
    for row in csvdata:
        voterid.append(row[0])
        county.append(row[1])
        candidates.append(row[2])
    
    #Create variables. 
    voters_list = len(voterid)
    candidates_list = set(candidates)


    print("Election Results")
    print("-----------------------------------------------")
    print(f"The Total number of votes cast: {voters_list}")
    print("------------------------------------------------")



  
    for row in candidates_list:
        names_of_candidates.append(row)

    #Create a dictionary for the candidates
    dict_of_candidates = {}
    candidates_count = 0
    for row in names_of_candidates:
        candidate_name = str(names_of_candidates[candidates_count])
        votes = int(candidates.count(candidate_name))
        vote_share = round(votes/voters_list * 100, 2)
        dict_of_candidates.update({candidate_name: votes})
        print(f"{candidate_name}: {vote_share}%  ({votes})")
        candidates_count = candidates_count + 1

    

    winner = max(dict_of_candidates, key=lambda key: dict_of_candidates[key])
    
    print("--------------------")
    print("Winner: ", winner)
    print("--------------------")




