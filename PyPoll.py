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

#save results to our text file
with open(file_to_save, "w") as txt_file:
    #print the final vote count to the terminal
    election_results=(
        #\n wrap ensures line will start on second line, w/ blank top line
        f"\nElection Results\n"
        f"----------------------------\n"
        f"Total Votes:{total_votes:,}\n"
        f"-----------------------------\n"
    )
    #end empty string prints a newline,ensures nothing will be printed on the last line
    print(election_results,end="")
    #save the final vote count to the text file
    txt_file.write(election_results)

    #determine percentage of votes for each candidate by looping through the counts
    for candidate_name in candidate_votes:
        #retrieve vote count of a candidate
        votes=candidate_votes[candidate_name]
        #calculate percentage of votes
        vote_percentage=float(votes)/float(total_votes)*100
        #declare variable for each candidate's name, percentage of votes and voter count
        candidate_results=(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        #print candidate results to terminal
        print(candidate_results)
        #save the candidate results to our text file
        txt_file.write(candidate_results)

        #determine winning vote count and candidate
        #determine if the votes is greater than the current winning count
        if (votes>winning_count) and (vote_percentage>winning_percentage):
            #if true, set winning_count=votes and winning_percentage=vote_percentage
            winning_count=votes
            winning_percentage=vote_percentage
            #and set winning_candidate=candidate_name
            winning_candidate=candidate_name

    #print the winning candidate's results to the terminal
    winning_candidate_summary=(
        f"-----------------------------\n"
        f"Winner:{winning_candidate}\n"
        f"Winning Vote Count:{winning_count:,}\n"
        f"Winning Percentage:{winning_percentage:.1f}%\n"
        f"-----------------------------\n"
    )
    print(winning_candidate_summary)
    #save the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)