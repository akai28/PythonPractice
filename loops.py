people = ["Hema", "Rekha", "Jaya", "Sushma"]

# Simple for loop

for person in people:
    print(f'Current Person: {person}')

# Break

for person in people:
if person == "Jaya":
    break
print(f'Current Person: {person}')

# Continue

for person in people:
    if person == 'Jaya':
        continue
    print(f'Current Person: {person}')

# range

for i in range(len(people)):
    print(people[i])

for i in range(0, 5):
    print(f'Number: {i}')

#  While loops

count = 0
while count < 5:
    print(f'Count: {count}')
    count += 1
