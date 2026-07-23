from typing import List, Dict, Set, Tuple

# This program analyzes survey responses by counting frequencies,
# finding unique items, and displaying the top N most frequent items.

# 1: Start with a list of items that represents survey responses
response: List[str] = [
    "Cat", "Dog", "Fish", "Cat", "Dog",
    "Cat", "Mango", "Fish", "Cat"
]

# 2: Write function that takes the list and returns a dictionary
# where keys are items and values are their frequencies
def calculate_frequencies(items: List[str]) -> Dict[str, int]:
    frequency_dict: Dict[str, int] = {}

    for item in items:
        frequency_dict[item] = frequency_dict.get(item, 0) + 1

    return frequency_dict

# 3: Write a function that returns a set of unique items from the list
def unique_items(items: List[str]) -> Set[str]:
    return set(items)

# 4: Write a function that returns the top N most frequent items
# using dictionary items and tuple unpacking
def top_n_frequent_item(frequency_dict: Dict[str, int], n: int) -> List[Tuple[str, int]]:
    sorted_items: List[Tuple[str, int]] = sorted(
        frequency_dict.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return sorted_items[:n]

# 5: Print a clear, readable summary
frequencies = calculate_frequencies(response)
unique = unique_items(response)
top_items = top_n_frequent_item(frequencies, 3)

print("Survey Summary")
print("-------------------------")

print("\nFrequencies:")
for item, count in frequencies.items():
    print(f"{item}: {count}")

print(f"\nUnique Item Count: {len(unique)}")

print("\nTop 3 Most Frequent Items:")
for item, count in top_items:   # tuple unpacking
    print(f"{item}: {count}")