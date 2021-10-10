# print ("Hello World")
#--------------------------------
#Setting list of key-pair dictionaries

#initializing list
# voting_data=[]

# #setting list of dictionaries
# voting_data=[{"county":"Arapahoe","registered voters":422829},{"county":"Denver","registered voters":463353},{"county":"Jefferson","registered voters":463353}]

# #print list of dictionaries output
# print(voting_data)
# print(len(voting_data))
# print(type(voting_data))

# #Add "El Paso" and voters to 2nd position
# voting_data.insert(1,{"county":"El Paso","registered_voters":461149})
# print(voting_data)

# #remove "Arapahoe"
# voting_data.pop(0)
# print(voting_data)

# #Make "Denver" 3rd position, keep "Jefferson" at 2nd position
# voting_data.pop(1)
# print(voting_data)
# voting_data.append({"county":"Denver","registered_voters":463353})
# print(voting_data)

# #Add "Arapahoe" at end
# voting_data.append({"country":"Arapahoe","registered_voters":422829})
# print(voting_data)
# #-------------------------------------------------
# #Decision Statements

# #Declare variables=input function
my_votes=int(input("How many votes did you get in the election?"))
total_votes=int(input("What is the total votes in the election?"))

# #Calculate % votes receieved per candidate
percentage_votes=(my_votes/total_votes)*100
# #Ask how to re-format to f-string
print(f"I received {percentage_votes} % of of the total votes.")

##IF STATEMENTS

# counties=["Arapahoe","Denver","Jefferson"]
# if counties[1]=="Denver":
#     print(counties[1])

##membership operators
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not in the list of counties")

##logical operators

#and
# if "Arapahoe" and "El Paso" in counties:
#     print ("Arapahoe and El Paso are in the list of counties")
# else:
#     print("Arapahoe and El Paso is not in the list of counties")

#or
# if "Arapahoe" or "El Paso" in counties:
#     print("Arapahoe or El Paso is in the list of counties.")
# else:
#     print("Arapahoe and El Paso are not in the list of counties")

#practice question
# if "Arapahoe" in counties and "El Paso" not in counties:
#     print("Only Arapahoe is in the list of counties.")
# else:
#     print("Arapahoe and El Paso are in the list of counties")
# 
# FOR LOOP
# for county in counties:
    # print(county)
       
# numbers=[0,1,2,3,4]
# for num in numbers:
#     print(num)

#with range
#determinging list order when you do not know the number of items in the list
# for index in range(len(counties)):
#     print(counties[index])

#ITERATE THROUGH DICTIONARY
counties_dict={"Arapahoe":422829,"Denver":463353,"Jefferson":432438}
# print(len(counties_dict))

#get keys only using for loop
# for county in counties_dict:
#     print(county)

#keys method
# for county in counties_dict.keys():
#     print(county)

#values method
# for voters in counties_dict.values():
#     print(voters)
#
#printing key-value pairs

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


#using the with statement open the file as a text file
# outfile=open(file_to_save, "w")
#write some data to the file
# outfile.write("Hello World")

#close the file
# outfile.close()