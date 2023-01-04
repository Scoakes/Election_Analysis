#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote

import csv
import os
dir(csv)

# Assign a variable for the file to load and the path.
file_to_load = '/Users/christopheroakes/Documents/Coding Bootcamp/Module 3/Election_Analysis/Resources /election_results.csv'

# Open the election results and read the file.
election_data = open(file_to_load, 'r')
election_data.close()

# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)

            #Alternate Indirect File Path Call
            #import csv
            #import os
            # Assign a variable for the file to load and the path.
            #file_to_load = os.path.join("Resources", "election_results.csv")
            # Open the election results and read the file.
            #with open(file_to_load) as election_data:

                # Print the file object.
            #    print(election_data)

 # Create a filename variable to a direct or indirect path to the file.
file_to_save = '/Users/christopheroakes/Documents/Coding Bootcamp/Module 3/Election_Analysis/Analysis /Election_Analysis.txt'

# Use the open statement to open the file as a text file.
with open(file_to_save, "w") as outfile:
# Write some data to the file.
    outfile.write("Hello World")

#Add more counties
#\n writes each item to its own line on the output file
    outfile.write("\nArapahoe\nDenver\nJefferson")

# Close the file
#outfile.close()

