import json

#  Sample JSON
userJSON = '{"first_name": "Ethan", "last_name": "Hunt", "age": 30}'

# Parse to dict
user = json.loads(userJSON)

print(user)
print(user['first_name'])

car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

carJSON = json.dumps(car)

print(carJSON)
