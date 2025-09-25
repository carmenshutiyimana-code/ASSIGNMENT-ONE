import array

# === INTEGERS ===
# Sample votes for features
feature_votes = [12, 25, 30, 18, 22, 10]

# Basic computations
total_votes = sum(feature_votes)
average_votes = total_votes / len(feature_votes)
min_votes = min(feature_votes)
max_votes = max(feature_votes)

# === STRINGS ===
# Report using f-strings
report = (
    f"Total Feature Request Votes: {total_votes}\n"
    f"Average Votes per Feature: {average_votes:.2f}\n"
)
print("=== String Report ===")
print(report)

# === BOOLEANS ===
# Threshold check using compound condition
threshold = 20
if average_votes > threshold and max_votes > 25:
    print("Status: Above Standard")
else:
    print("Status: Below Standard")

# === LISTS ===
print("\n=== List Modifications ===")
print("Original list:", feature_votes)

# Add a new vote count
feature_votes.append(27)

# Remove votes less than 15
feature_votes = [vote for vote in feature_votes if vote >= 15]

# Sort list
feature_votes.sort()
print("Modified list:", feature_votes)

# === ARRAYS ===
print("\n=== Array Operations ===")
# Use first 5 values for a fixed-size array
feature_array = array.array('i', feature_votes[:5])
array_sum = sum(feature_array)
list_sum = sum(feature_votes[:5])
print("Array sum:", array_sum)
print("List sum (for same values):", list_sum)

# === DICTIONARIES ===
print("\n=== Dictionary Operations ===")
features = [
    {'id': 1, 'name': 'Dark Mode', 'value': 30},
    {'id': 2, 'name': 'Offline Mode', 'value': 20},
    {'id': 3, 'name': 'Custom Themes', 'value': 25},
]

# Update one record
features[1]['value'] = 22  # Updated Offline Mode votes

# Delete one record by id
features = [f for f in features if f['id'] != 3]

# Compute total of 'value' field
total_value = sum(f['value'] for f in features)

# Display updated features
for feature in features:
    print(feature)

print(f"Total Votes (from dictionaries): {total_value}")
