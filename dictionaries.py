# Create dict
person = {
    'first_name': 'Jack',
    'last_name': 'Jill',
    'age': 20
}

# Use constructor
person2 = dict(first_name='Sara', last_name='Williams')

# Get value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '022 8881212'

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict
person2 = person.copy()
person2['city'] = 'Turkey'

# Remove item
del(person['age'])
person.pop('phone')

# Clear
person.clear()

# Get length
print(len(person2))

# List of dict
people = [
    {'name': 'Martin', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people[1]['name'])
