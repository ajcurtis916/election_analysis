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

#open election results and read file
with open(file_to_load) as election_data:
    #read the file object with the reader function
    file_reader=csv.reader(election_data)
    
    #read and print the header row
    headers=next(file_reader)
    print(headers)

#write data to file
with open(file_to_save,"w") as txt_file:
    txt_file.write("Counties in the Election\n")
    txt_file.write("------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")

