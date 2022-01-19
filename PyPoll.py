#The data we need to retrieve
#1. Total number of votes
#2. A complete list of candidates who received votes
#3. Percentage of votes for each candidate
#4. Total number of votes for each candidate
#5. Winner of election based on pop vote

#import dependencies
import csv
import os

#assign variable to load a file from a path
file_to_load=os.path.join("resources","election_results.csv")
#assign variable to save the file to a path
file_to_save=os.path.join("analysis","election_analysis.txt")

#initialize total vote counter
total_votes=0
#initialize empty list for candidate names
candidate_options=[]
#initialize empty dictionary for votes per candidate name
candidate_votes={}

#initialize empty string value for winning candidate
winning_candidate=""
#initialize winning count variable
winning_count=0
#initialize winning percentage variable
winning_percentage=0

#open election results and read file
with open(file_to_load) as election_data:
    #read the file object with the reader function
    file_reader=csv.reader(election_data)
    
    #read the header row
    headers=next(file_reader)

    #print each row in the csv file
    for row in file_reader:
        #add to total vote count
        total_votes+=1

        #print candidate name from each row
        candidate_name=row[2]

        #add candidate name to list if not already added (unique names only)
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            #itialize votes per candidate counter
            candidate_votes[candidate_name]=0

        #add vote to that candidate's count
        candidate_votes[candidate_name]+=1

#determine percentage of votes for each candidate by looping through the counts
for candidate_name in candidate_votes:
    #retrieve vote count of a candidate
    votes=candidate_votes[candidate_name]
    #calculate percentage of votes
    vote_percentage=float(votes)/float(total_votes)*100
    #print each candidate's name and percentage of votes
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #determine winning vote count and candidate
    #determine if the votes is greater than the current winning count
    if (votes>winning_count) and (vote_percentage>winning_percentage):
        #if true, set winning_count=votes and winning_percentage=vote_percentage
        winning_count=votes
        winning_percentage=vote_percentage
        #and set winning_candidate=candidate_name
        winning_candidate=candidate_name

winning_candidate_summary=(
    f"-----------------------------\n"
    f"Winner:{winning_candidate}\n"
    f"Winning Vote Count:{winning_count:,}\n"
    f"Winning Percentage:{winning_percentage:.1f}%\n"
    f"-----------------------------\n"
)
print(winning_candidate_summary)

#write data to file
with open(file_to_save,"w") as txt_file:
    txt_file.write("Counties in the Election\n")
    txt_file.write("------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")

