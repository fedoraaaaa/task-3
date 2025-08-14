import copy

# Original nested list
original = [[1, 2, 3], [4, 5, 6]]

# Shallow copy - only copies references to nested lists
shallow = copy.copy(original)  

# Deep copy - creates new copies of all nested objects
deep = copy.deepcopy(original)  

# Modifying the first element of the first nested list
original[0][0] = 'X'

# Output comparison:
print("Original:", original)  # [['X', 2, 3], [4, 5, 6]]
print("Shallow:", shallow)    # [['X', 2, 3], [4, 5, 6]] 
# ^ Shallow copy affected because it shares nested lists

print("Deep:", deep)          # [[1, 2, 3], [4, 5, 6]]
# ^ Deep copy unaffected - completely independent

# Modifying the top-level structure
original.append([7, 8, 9])

print("\nAfter top-level modification:")
print("Original:", original)  # [['X', 2, 3], [4, 5, 6], [7, 8, 9]]
print("Shallow:", shallow)    # [['X', 2, 3], [4, 5, 6]]
# ^ Shallow copy not affected by top-level changes
print("Deep:", deep)          # [[1, 2, 3], [4, 5, 6]]