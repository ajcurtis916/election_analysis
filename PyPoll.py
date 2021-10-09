#data we need to retreive:
#1. total # of votes cast
#2. complete list of candidates who received votes
#3. % of votes ea candidate won
#4. total # of votes each candidate won
#5. winner of election based on pop vote

#import datetime class from datetime module
# import datetime as dt
# set variable and use now() attribute on datetime class to get present time
# now=dt.datetime.now()
#print present time
# print("The time right now is",now)

#importing the operating system module and defining the module's attributes
import csv
import os
# print(dir(os))

#submodule function discovery
# print(dir(os.path))

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
# load_election_data=os.path.join("resources", "election_results.csv")
load_election_data = "resources/election_results.csv"

# print(f"my input file: {load_election_data}")
# exit()

#open and read file
with open(load_election_data) as election_data:
    print(election_data)

    #read the file object with the reader function
    file_reader=csv.reader(election_data)
    #print header row
    headers=next(file_reader)
    print(headers)
    
    
#for loop using break exercise w/ tutor
# x = [1, 2, 3, 4]

# for num in x:
#     if num == 2:
#         print(f"if num= {num}")
#         exit()
#     elif num == 3: 
#         print(f"I am 3.")   
#         break
#     else:
#         print(f"else num= {num}")

# # exit()

# print(f"my input file: 1")

# print(f"my input file: 2")

# exit()

# print(f"my input file: 3")


#create filename variable to a path to save the file (format previously had issues so used r string)
file_to_save=r"C:\Users\acurt\OneDrive\Desktop\Data Analytics Bootcamp\M3 Python\election_analysis\analysis\election_results.txt"
#using the with statement open the file as a text file
# outfile=open(file_to_save, "w")
#write some data to the file
# outfile.write("Hello World")

#close the file
# outfile.close()

#using the with statement open the file as text (makes code cleaner more readable)
with open(file_to_save,"w") as txt_file:
    #write some data to the file
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")





