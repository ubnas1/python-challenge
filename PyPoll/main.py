# importing modules

import os
import csv

# providing file path to file_path variable

file_path = os.path.join("pypoll","Resources", "election_data.csv")

# opening file using open function

with open(file_path) as csv_file:

#   putting all the values in csv_reader variable seperated by a comma

    csv_reader = csv.reader(csv_file, delimiter=",")

#   skipping header using next function

    next(csv_reader)

#   initialising vote variables for each candidate

    charles_casper_stockham_votes = 0
    diana_degette_votes = 0
    raymon_anthony_doane_votes = 0

#   initialising name variable for each candidate

    charles_casper_stockham_name = "charles_casper_stockham"
    diana_degette_name = "diana_degette"
    raymon_anthony_doane_name = "raymon_anthony_doane"

#   initialising vote count variable

    vote_count = 0

#   now going through all values using for loop

    for row in csv_reader:

#   counting total votes

        vote_count += 1

#   counting individual votes

        if row[2] == "Charles Casper Stockham":
            charles_casper_stockham_votes += 1

        elif row[2] == "Diana DeGette":
            diana_degette_votes += 1
    
        elif row[2] == "Raymon Anthony Doane":
            raymon_anthony_doane_votes += 1

#   determining the winner using 'if' '>' 'and' and giving the value to winner function

    if charles_casper_stockham_votes > diana_degette_votes and charles_casper_stockham_votes > raymon_anthony_doane_votes:
        winner = charles_casper_stockham_name

    elif diana_degette_votes > charles_casper_stockham_votes and diana_degette_votes > raymon_anthony_doane_votes:
        winner = diana_degette_name

    elif raymon_anthony_doane_votes > charles_casper_stockham_votes and raymon_anthony_doane_votes > diana_degette_votes:
        winner = raymon_anthony_doane_name

#   calculating % for each candidate

    percentage_charles_casper_stockham_votes = round((charles_casper_stockham_votes/vote_count)*100,3)

    percentage_diana_degette_votes = round((diana_degette_votes/vote_count)*100,3)

    percentage_raymon_anthony_doane_votes = round((raymon_anthony_doane_votes/vote_count)*100,3)

#   printing results

    print("  ****************  ")
    print("  Election Results  ")
    print("  ****************  ")
    print("    ")
    print(f" Total Votes: {vote_count}")
    print("  ----------------  ")
    print("    ")
    print(f" {charles_casper_stockham_name}: {charles_casper_stockham_votes} | {percentage_charles_casper_stockham_votes}%")
    print("    ")
    print(f" {diana_degette_name}: {diana_degette_votes} | {percentage_diana_degette_votes}%")
    print("    ")
    print(f" {raymon_anthony_doane_name}: {raymon_anthony_doane_votes} | {percentage_raymon_anthony_doane_votes}%")
    print("    ")    
    print("  ----------------   ")
    print(f"  Winner: {winner} ")
    print("  ----------------  ")

#  providing text file path to variable

text_file_path = os.path.join("PyPoll","Analysis", "analysis.txt")

# print analysis to text file

with open(text_file_path,"w") as handle:
    handle.write(f" **************** \n Election Results \n **************** \n\n")
    handle.write(f' Total Votes: {vote_count}\n ----------------\n\n')
    handle.write(f" {charles_casper_stockham_name}: {charles_casper_stockham_votes} | {percentage_charles_casper_stockham_votes}%\n")
    handle.write(f" {diana_degette_name}: {diana_degette_votes} | {percentage_diana_degette_votes}%\n")
    handle.write(f" {raymon_anthony_doane_name}: {raymon_anthony_doane_votes} | {percentage_raymon_anthony_doane_votes}%\n\n")
    handle.write(f"----------------\n Winner: {winner} \n ----------------")
