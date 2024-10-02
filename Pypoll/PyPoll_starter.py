# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("resource", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidate_name = []
vote_counts = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_percentage = 0 
winning_count = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)
    print(f"header {header}")
    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        
        # print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate = row[2]


        # If the candidate is not already in the candidate list, add them
        if candidate not in candidate_name: 
            candidate_name.append(candidate)
            vote_counts[candidate]=0 
        
        # Add a vote to the candidate's count
        vote_counts[candidate] += 1
print(f"candidate name {candidate_name}")
# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    output = (
         f"\nElection Results\n"
         f"Total Votes: {total_votes}\n"
    )
    print(output)
    

    # Write the total vote count to the text file
    txt_file.write(output)

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in vote_counts:

        # Get the vote count and calculate the percentage
        votes = vote_counts[candidate]
        vote_percentage = (votes / total_votes) * 100

        # Update the winning candidate if this one has more votes
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

        # Print and save each candidate's vote count and percentage
        candidate_results = (
            f"{candidate}: {vote_percentage:.3f}% ({votes})\n"

        )
        print(candidate_results)
        txt_file.write(candidate_results)
    # Generate and print the winning candidate summary
    winning_candidate_summary = (
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count}\n"
        f"Winning Percentage: {winning_percentage: .3f}%\n"
    )
    print(winning_candidate_summary)
    # Save the winning candidate summary to the text file   
    with open(file_to_output, "w") as txt_file:
        txt_file.write(winning_candidate_summary)