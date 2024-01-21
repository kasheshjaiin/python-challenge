import os
import csv


# Specify the path to the CSV file
election_csv = os.path.join("Resources", "election_data.csv")

# Read the CSV file
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    next(csvreader)

    # Initialize variables to store results
    total_votes = 0
    candidates = {}
    winner = {"name": "", "votes": 0}

    # Iterate through each row in the file
    for row in csvreader:
        # Count total votes
        total_votes += 1

        # Extract candidate name
        candidate_name = row[2]

        # Update candidate votes count
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

    # Find the winner
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        print(f"{candidate}: {percentage:.3f}% ({votes} votes)")

        # Update the winner
        if votes > winner["votes"]:
            winner["name"] = candidate
            winner["votes"] = votes

    # Print the output of the election
    print("Election Result")
    print("--------------------------------")
    print(f"Total Votes: {total_votes}")
    print("--------------------------------")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        print(f"{candidate}: {percentage:.3f}% ({votes} votes)")
    print("--------------------------------")
    print(f"Winner: {winner['name']}")
    
    print("--------------------------------")

     # Export result to a text file in the 'analysis' folder
    os.makedirs("analysis", exist_ok=True)
    output_path = os.path.join("analysis", "election_analysis.txt")
    with open(output_path, "w") as output_file:
      output_file.write("Election Result\n")
      output_file.write("--------------------------------\n")
      output_file.write(f"Total Votes: {total_votes}\n")
      output_file.write("--------------------------------\n")
      for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        output_file.write(f"{candidate}: {percentage:.3f}% ({votes} votes)\n")
      output_file.write("--------------------------------\n")
      output_file.write(f"Winner: {winner['name']}\n")
      output_file.write("--------------------------------\n")