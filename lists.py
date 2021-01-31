# Create Lists
numbers = [1, 2, 3, 4, 5]
fruits = ["Apples", "Oranges", "Grapes", "Pears"]

# Constructors
numbers_2 = list((1, 2, 3, 4, 5))

# Get a value
print(fruits[1])

# Get length
print(len(fruits))

# Add to list
fruits.append("Mangoes")
print(fruits)

# Remove from list
fruits.remove("Oranges")
print(fruits)

# Insert to list
fruits.insert(2, "Straberries")
print(fruits)

# Change a value
fruits[0] = "Blueberries"
print(fruits)

# Remove with pop
fruits.pop(2)
print(fruits)

# Reverse the list
fruits.reverse()
print(fruits)

# Sort list
fruits.sort()
print(fruits)

# Reverse Sort
fruits.sort(reverse=True)
print(fruits)
