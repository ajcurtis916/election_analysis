#data we need to retreive:
#1. total # of votes cast
#2. complete list of candidates who received votes
#3. % of votes ea candidate won
#4. total # of votes each candidate won
#5. winner of election based on pop vote


#importing the operating system module and defining the module's attributes
import csv
import os

#open file using different code
# with open('election_results.csv') as election_data:
#     reader=csv.reader(election_data)

#     count=0

#     for row in reader:
#         print(row)

#         if count> 5:
#             break
#         count +=1

#assign variable and path to csv
load_election_data=os.path.join("resources","election_results.csv")
#create filename variable to a path to save the file (format previously had issues so used r string)
file_to_save=os.path.join("analysis","election_results.txt")

# print(f"my input file: {load_election_data}")
# exit()

#Initialize total vote counter w/ variable
total_votes=0

#declare new list
candidates=[]

#declare dictionary to connect candidates w/ their votes
candidate_votes={}

#winning candidate and winning count tracker
winning_candidate=""
winning_count=0
winning_percentage=0

#open and read file
with open(load_election_data) as election_data:
    #read the file object with the reader function
    file_reader=csv.reader(election_data)
    
    #print header row
    headers=next(file_reader)
     
    #print ea row in the CSV file
    for rows in file_reader:
        #add to the total vote count
        total_votes+=1 
        
        #print the candidate name for ea row
        candidate_name=rows[2]  

            #if candidate does not match any existing candidate...
        if candidate_name not in candidates:
            #add to list of candidates
            candidates.append(candidate_name)

            #begin tracking ea candidate's vote count (initialize)
            candidate_votes[candidate_name]=0

        #add vote to that candidate's count
        candidate_votes[candidate_name]+=1

#save results to txt file
with open(file_to_save,"w") as txt_file:
    election_results=(
        f"\nElection Results \n"
        f"------------------------------\n"  
        f"Total Votes:{total_votes:}\n"
        f"------------------------------\n")
    print(election_results,end="") 
    txt_file.write(election_results) 
    
    
#determine the % of votes for ea candidate by looping through the counts
#1. Iterate through the candidate list
    for candidate_name in candidate_votes:
    #2. Retreive vote count of ea condidate
        votes=candidate_votes[candidate_name]
        #3. Calculate % of the votes
        vote_percentage=float(votes)/float(total_votes)*100
        
    #print each candidate, voter percentage and count to one decimal
    #save results to txt file
    # with open(file_to_save,"w") as txt_file:
        candidate_results=(f"{candidate_name}:{vote_percentage:.1f}%({votes:,})\n") 
        print(candidate_results)
        txt_file.write(candidate_results)

# with open(file_to_save,"w") as txt_file:
    # txt_file.write(candidate_results)
    # 4. Print the candidate name and % of votes
    # print(f"{candidate_name} received {vote_percentage}% of the votes.")
    # print(f"{vote_percentage:.1f}%")

# #Print total votes,candidates, votes per candidate (checking work)
# print(total_votes)
# print(candidates) 
# print(candidate_votes)


        #Determine winning vote count, winning % and candidate name IMPORTANTE
        #1. Determine if the votes are greater than the winning count
        if (votes>winning_count) and (vote_percentage>winning_percentage):
        #2 If true then set winning_count=votes and winning_percent=
        #vote+percentage
            winning_count=votes
            winning_percentage=vote_percentage
        #3 Set the winning_candidate equal to the candidate's name
            winning_candidate=candidate_name 

    winning_candidate_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------\n")
    print(winning_candidate_summary)
    #save the winning candidate's name to txt file
    txt_file.write(winning_candidate_summary)            




