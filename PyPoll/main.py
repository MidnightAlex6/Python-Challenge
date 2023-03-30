import os
import csv

#files to load and paste
File_to_Load = os.path.join("Resources/election_data.csv")
print(File_to_Load) #path for my file
File_to_Output = os.path.join("Analysis/Txt_File") #path to paste the text to a text file

#total vote counter
Total_Votes = 0

#candidate options and vote counters
Candiate_Options = []
Candiate_Votes = {}

#Wining candidate and winning count tracker
Winning_Candidate = ""
Winning_Count = 0 

#read the csv and convert it into a list of dictionarys
with open(File_to_Load) as Election_Data:
    reader = csv.DictReader(Election_Data)

    #for each row...
    for row in reader:

        #add to the total vote count
        Total_Votes = Total_Votes + 1

        #extract the candidate name from each of the rows
        Candidate_Name = row["Candidate"]

        #If the candidate does not match any exsisting candidates
        if Candidate_Name not in Candiate_Options:

            #add it to the list of candidate in the running
            Candiate_Options.append(Candidate_Name)

            #And begin tracking that candidates voter count
            Candiate_Votes[Candidate_Name] = 0
        
        #then add a vote to the candidtes vote count
        Candiate_Votes[Candidate_Name] += 1

#print the results and export the data to our file
with open(File_to_Output, "w") as Txt_file:

    #print the final vote count 
    Election_Results = (
        f"\n\nElection Results\n"
        f"-------------------------------------\n"
        f"Total Votes: {Total_Votes}\n"
        f"--------------------------------------\n"
    )
    print(Election_Results)

    #save the final vote count to the text file
    Txt_file.write(Election_Results)

    #determine the winner by loping through the counts 
    for candidate in Candiate_Votes:

        #grab the vote count and percentage
        votes = Candiate_Votes.get(candidate)
        Votes_Percentage = float(votes) / float(Total_Votes) * 100

        #find the winning vote count and candidate
        if (votes > Winning_Count):
            Winning_Count = votes
            Winning_Candidate = candidate
        
        #print each candidate's voter count and %
        Voter_Output = f"{candidate}: {Votes_Percentage:.3f}% ({votes})\n"
        print(Voter_Output)
        
        #save each candidte votes count and % to the text file
        Txt_file.write(Voter_Output)

    #print the winning candidate
    Winning_Candidate_Summary = f"""\n
-------------------------------------\n
Winner: {Winning_Candidate}\n
-------------------------------------\n
"""
    print(Winning_Candidate_Summary)

    #save the winning candidates name to the text file
    Txt_file.write(Winning_Candidate_Summary)