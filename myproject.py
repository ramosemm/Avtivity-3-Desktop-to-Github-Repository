# Create a dataset with 30 strings
data_set = [
    "apple", "banana", "cherry", "date", "elderberry",
    "fig", "grape", "honeydew", "kiwi", "lemon",
    "mango", "nectarine", "orange", "papaya", "quince",
    "raspberry", "strawberry", "tangerine", "watermelon",
    "blueberry", "cranberry", "blackberry", "guava", "pineapple",
    "apricot", "lime", "plum", "pear", "grapefruit", "pomegranate"
]

# Function to perform sorting (you can use any sorting algorithm here)
def my_sort(data):
    return sorted(data)

# Sort the dataset
sorted_data = my_sort(data_set)

# Print the original and sorted dataset
print("Original Data:", data_set)
print("Sorted Data:", sorted_data)