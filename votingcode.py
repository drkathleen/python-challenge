import os
import csv

election_csv = os.path.join(os.getcwd(), "Resources","election_data.csv")

##create dictionary key:value for each candidate
candidateList = {"1": "Khan", "2": "Correy", "3": "Li", "4": "O'Tooley"}

##create and initialize variables
totalVotes = 0
Cand1 = 0
Cand2 = 0
Cand3 = 0
Cand4 = 0
winnerNumVotes = 0

with open(election_csv, 'r')as csvfile:
        
     csvreader = csv.reader(csvfile,delimiter=',')
     ##get header info, first line in csv file
     header = next(csvreader)

     ##loop thru dataset row by row, counting votes per candidate
     for row in csvreader:
         if candidateList["1"] == row[2]:
             Cand1 = Cand1 + 1
         if candidateList["2"] == row[2]:
             Cand2 = Cand2 + 1
         if candidateList["3"] == row[2]:
             Cand3 = Cand3 + 1
         if candidateList["4"] == row[2]:
             Cand4 = Cand4 + 1
         totalVotes = totalVotes + 1

##put each total number of votes per candidate in a list object
candTotals = [Cand1,Cand2,Cand3,Cand4]

##get the max number of votes from list candTotals using list object method 'max'
winnerNumVotes = max(candTotals)

##using the max number value, indentify the index location of this value within list object (0,1,2,3)
winner = candTotals.index(winnerNumVotes)

##print out the winner value - this will be used as the key in dictionary object
##to find candidate's name - remember we must add 1 so key can find correct value in the dictionary 
print("winner index: " + str(winner))
winner = winner + 1

output = (    
    f"\n" 
    f"ELECTION RESULTS\n"
    f"-----------------------------------\n"
    f"Total Votes:  {totalVotes}\n"
    f"-----------------------------------\n"
    f"{candidateList[str(1)]} : {(Cand1/totalVotes*100):2f}% ({Cand1})\n" 
    f"{candidateList[str(2)]} : {Cand2/totalVotes*100:2f}% ({Cand2})\n" 
    f"{candidateList[str(3)]} : {Cand3/totalVotes*100:2f}% ({Cand3})\n" 
    f"{candidateList[str(4)]} : {Cand4/totalVotes*100:2f}% ({Cand4})\n"


    f"-----------------------------------\n"
    f"Winner: {candidateList[str(winner)]}\n"
    f"-----------------------------------" )
                
csvfile.close

print(output)

#export txt file
with open('file_to_output','w') as txt_file:
 txt_file.write(output)
print("\n") 
print("End of Script.")
