import random

# Generate random candidate data
PARTIES = ['Party A', 'Party B', 'Party C', 'Party D', 'Party E']
CANDIDATE_TYPES = {
    'Presidential Candidates': 3,
    'Senatorial Candidates': 3,
    'House of Representatives Candidates': 3,
    'Governorship Candidates': 3,
    'House of Assembly Candidates': 3
}
candidates = {}
for ctype, num in CANDIDATE_TYPES.items():
    candidates[ctype] = [(f"{ctype[:-1]} {i}", random.choice(PARTIES))
                         for i in range(1, num+1)]

# Prompt user to insert Permanent Voters Card
print("Please insert your Permanent Voters Card.")

# Prompt user to select language
LANGUAGES = ['English', 'Yoruba', 'Igbo', 'Hausa']
selected_language = input(
    f"Please select your language: {', '.join(LANGUAGES)}\n")

# Display candidates and their parties for user to choose
for ctype, cands in candidates.items():
    print(f"{ctype}:")
    for i, candidate in enumerate(cands):
        print(f"{i+1}. {candidate[0]} - {candidate[1]}")
    selected_candidate = input(
        f"Please select your preferred {ctype[:-1]} (1-3): ")

# Eject Permanent Voters Card
print("\nThank you for voting. Your Permanent Voters Card is now ejected.")

# Log votes in Management site
voters_card_number = input("\nPlease enter your Voters Card Number: ")
print(
    f"\nYour vote has been recorded. To view the election results, please visit the Management site and enter your Voters Card Number: {voters_card_number}")
