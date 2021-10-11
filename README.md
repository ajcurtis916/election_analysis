# Election Analysis

## Project Overview
A Colorado Board of Elections employee tasked us with completing an election audit following a recent local congressional election.  Major tasks as follows:

1. Calculate the total number of votes cast.
2. Get a complete list of candidates whom received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
* Data Source: election_results.csv (located in "resource" file)<br/>
* Software: Python 3.7.6 64-bit, Visual Studio Code, Version: 1.61.0

## Election Results
Our analysis of the election shows:<br/>
- There were 369,711 total votes cast in the election<br/>
- Charles Casper Stockham, Diana DeGette and Raymon Anthony Doane were the qualifying candidates (candidates with votes)<br/>
  - Charles Casper Stockham received 23.0% of the vote (85,213 votes total)<br/>
  - Diana DeGette received 73.8% of the vote (272,892 votes total)<br/>
  - Raymon Anthony Doane received 3.1% of the votes (11,606 votes total)<br/>
- The winner of the election was:<br/>
  - Diana DeGette, whom received 73.8% of the vote and 272,892 votes total
 
 ## Challenge Overview
 A Colorado Board of Elections employee asked us to expand our audit to breakdown the voter turnout by county.  Major tasks as follows:
 
 1. Calculate voter turnout for each county<br/>
 2. Calculate the percentage of votes from each county out of the total voter count<br/>
 3. Determine the county with the highest voter turnout<br/>

## Challenge Results
Our analysis of the election by county shows:<br/>
- The counties of Jefferson, Denver and Arapahoe participated in this election<br/>
  - 10.5% of the total votes came from Jefferson (38,855 votes total)<br/>
  - 82.8% of the total votes came from Denver (306,055 votes total)<br/>
  - 6.7% of the total cotes came from Arapahoe (24,801 votes total)<br/>
- Denver had the largest voter turnout out of all the particpating counties<br/>

## Resources
* Data Source: election_results.csv (located in "resource" file)<br/>
* Software: Python 3.7.6 64-bit, Visual Studio Code, Version: 1.61.0

## Challenge Summary
The Python code created by our team for the current analysis can be implemented for future elections, pending correct removal and insertion of the necessary data files and pathways. Once all data from future election(s) are compiled into a csv file, the correct local pathway for import and saving must be input on lines 9 and 11.</br></br>
If the Board prefers to assess different parameters than the voter turnout per county, etc., such variables may be swapped out for alternate data, such as political party turnout per county or per candidate.  This restructring will be more involved, requiring changes such as the variables on lines 21, 22, 31, 32, 33, 53, 112-114 to be adjusted, replaced on line 70, 73, 76, 79, 97, 99, 101, 104, 109, 117, 124 and the f-string statements on lines 105-106 and 119 to be changed accordingly.  This code will need further reworking if the data is not imported from a csv file.  You may contact us should you have any trouble during future implemetation.  
  
