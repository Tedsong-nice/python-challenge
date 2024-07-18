import pandas as pd

file_path = 'python-challenge/PyPoll/Resources/election_data.csv'

data = pd.read_csv(file_path)

total_votes = data['Ballot ID'].nunique()

candidates = data['Candidate'].unique
candidate_votes = data['Candidate'].value_counts()
percentage = candidate_votes/total_votes*100
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate,votes in candidate_votes.items():
    percentage_can = percentage[candidate]
    print(f"{candidate}: {percentage_can:.3f}% ({votes})")

winner = candidate_votes.idxmax()
print("-------------------------")
print(f'Winner: {winner}')
print("-------------------------")
